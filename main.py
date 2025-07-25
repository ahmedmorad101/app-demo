from fastapi import FastAPI
import uvicorn
from datetime import datetime
import socket

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World","hostname":socket.gethostname()}

@app.get("/now")
async def now():
    return {"now":datetime.now()}

if __name__ == "__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=9000)
