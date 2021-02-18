import uvicorn

from src import api

if __name__ == "__main__":
    uvicorn.run("api:api", port=8000, host="0.0.0.0", reload=True)
