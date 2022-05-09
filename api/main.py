import asyncio
from datetime import datetime
import json

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
    
    print(f'{t.name} has registered')
    teams[t.name] = t.members

async def save_data_occasionally():
     while True:
         print('[every 30s] writing team data to disk...')
         with open('teams.json', 'w+') as f:
            json.dump(teams, f)
         await asyncio.sleep(30)

async def main():
    asyncio.create_task(save_data_occasionally())
    
    config = Config()
    config.bind = ["0.0.0.0:9000"]
    
    await serve(app, config)
    
if __name__ == '__main__':
    asyncio.run(main())