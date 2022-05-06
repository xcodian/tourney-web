import asyncio
from datetime import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from hypercorn.config import Config
from hypercorn.asyncio import serve

teams = {}

app = FastAPI()

class Member(BaseModel):
    name: str
    discord: str
    ign: str
    mg: int
    year: int
    sub: bool
    valid: bool

class Team(BaseModel):
    name: str
    members: list[Member]

@app.get("/")
async def hello():
    print("hello!")

@app.post("/register")
async def register(t: Team):
    print(datetime.utcnow().timestamp())
    if datetime.utcnow().timestamp() > 1652409000:
        raise HTTPException(status_code=400)

    t.name = t.name.strip()

    if not t.name.replace(' ', '').isalnum():
        print('rejecting submission: invalid team name: ' + t.name)
        raise HTTPException(status_code=400)

    for m in t.members:
        m.discord = m.discord.strip()
        m.ign = m.ign.strip()

        if not (m.name and m.discord and m.ign and m.valid):
            print('rejecting submission: invalid member name, discord, ign or validity flag')
            raise HTTPException(status_code=400)
        
        if not (0 <= m.mg <= 13):
            print('rejecting submission: out of range mentor group')
            raise HTTPException(status_code=400)
        
        if not (7 <= m.year <= 12):
            print('rejecting submission: out of range year level')
            raise HTTPException(status_code=400)

    if (teams.get(t.name) is not None):
        print('rejecting submission: already registered')
        raise HTTPException(status_code=409) # conflict
    
    teams[t.name] = t.members

if __name__ == '__main__':
    config = Config()
    config.bind = ["0.0.0.0:9000"]

    asyncio.run(serve(app, config))