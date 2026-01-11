from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hallo Welt!"}

# Run the application with Uvicorn when this script is executed directly.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
