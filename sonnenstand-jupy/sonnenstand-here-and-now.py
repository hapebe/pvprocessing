#!/usr/bin/env python3
import pandas as pd
import pvlib
import json

timezone = "Europe/Berlin"

# Berlin:
latitude = 52.52
longitude = 13.405

# Sassnitz:
latitude = 54.5188613
longitude = 13.646231

# get the current timestamp (in the specified timezone)
time = pd.Timestamp.now(tz=timezone)

location = pvlib.location.Location(latitude, longitude, tz=timezone)

solar_pos = location.get_solarposition(time)

azimuth = solar_pos["azimuth"].iloc[0]
elevation = solar_pos["elevation"].iloc[0]

timestring = time.isoformat()[0:19]
timestring = timestring.replace(":", "-")

# Prepare the data for JSON output
output_data = {
    'lat': latitude,
    'lon': longitude,
    'isotime': time.isoformat(),
    'time': timestring,
    'timezone': timezone,
    'azimuth': azimuth,
    'azimuth_int': int(round(azimuth)),
    'elevation': elevation,
    'elevation_int': int(round(elevation)),
}

# Output the data as JSON
json_output = json.dumps(output_data)
print(json_output)

