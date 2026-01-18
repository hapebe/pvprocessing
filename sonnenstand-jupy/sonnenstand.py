#!/usr/bin/env python3
import pandas as pd
import pvlib
import pytz

def dataframe_to_records(df, time_key="datetime", iso=True):
    """
    Convert a time-indexed DataFrame to a list of dicts.
    If iso=True, the timestamp is converted to ISO strings.
    """
    # preserve index (time) as a column
    df2 = df.reset_index()
    # find the name of the index column produced by reset_index()
    idx_col = df.index.name if df.index.name is not None else "index"
    df2 = df2.rename(columns={idx_col: time_key})
    if iso:
        df2[time_key] = df2[time_key].apply(lambda t: t.isoformat() if hasattr(t, "isoformat") else t)
    return df2.to_dict(orient="records")

def getSonnenstaende(lat, lon, timezone="Etc/UTC"):
    # timezone = "Etc/UTC"
    # timezone = "Europe/Berlin"

    # --- Time range - should be not a leap year ---
    year = 2025
    start = pd.Timestamp(f"{year}-01-01 00:00:00", tz=timezone)
    end   = pd.Timestamp(f"{year}-12-31 23:59:00", tz=timezone)
    # create datetime samples by given resolution:
    # times = pd.date_range(start=start, end=end, freq="10min")
    times = pd.date_range(start=start, end=end, freq="720min")

    # Create location object
    location = pvlib.location.Location(lat, lon, tz=timezone)
    # Calculate solar positions for all the times
    solar_positions = location.get_solarposition(times)
    solar_positions.head()

    sun_data = solar_positions[["azimuth", "elevation"]].copy()
    sun_data.head()

    # optional: Remove nighttime values (sun below horizon):
    # sun_data = sun_data[sun_data["elevation"] > 0]
    # return sun_data
    return dataframe_to_records(sun_data)

def main():
    sun_data = getSonnenstaende(
        lat = 52.52, lon = 13.405, timezone = "Europe/Berlin"
    )
    sun_data.to_csv("sun_position_10min.csv")

if __name__ == "__main__":
    main()