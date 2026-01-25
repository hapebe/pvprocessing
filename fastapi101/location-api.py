#!/usr/bin/env python3
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
import importlib.machinery
import importlib.util
from pathlib import Path

# Get path to mymodule
script_dir = Path( __file__ ).parent
mymodule_path = str( script_dir.joinpath( '..', 'sonnenstand-jupy', 'sonnenstand.py' ) )

# Import mymodule
loader = importlib.machinery.SourceFileLoader( 'sonnenstand', mymodule_path )
spec = importlib.util.spec_from_loader( 'sonnenstand', loader )
sonnenstand = importlib.util.module_from_spec( spec )
loader.exec_module( sonnenstand )

# examples = sonnenstand.getSonnenstaende(lat = 52.52, lon = 13.405, timezone = "Europe/Berlin")
# examples.to_csv("sun_position_10min.csv")

app = FastAPI(title="PV location data API",description="Several data retrieval functions regarding sun und locations on earth.",version="1",contact={"name":"Hans-Peter Bergner"})

@app.get("/year", tags=["Read"])
async def sunpositions(lat: float = 52.52, lon: float = 13.405, timezone: str = "Etc/UTC"):
    data = sonnenstand.getSonnenstaende(lat, lon, timezone)
    return JSONResponse(content=jsonable_encoder(data))

@app.get("/now", tags=["Read"])
async def hereandnow(lat: float = 52.52, lon: float = 13.405, timezone: str = "Etc/UTC"):
    data = sonnenstand.getHereAndNow(lat, lon, timezone)
    return JSONResponse(content=jsonable_encoder(data))

# Run the application with Uvicorn when this script is executed directly.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
