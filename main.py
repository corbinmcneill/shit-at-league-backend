import uvicorn
from fastapi import FastAPI

import config

config.settings
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "shit at league"}


@app.get("/get_player/{region}/{summoner_id}")
async def get_player(region: str, summoner_id: str):
    return {}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
