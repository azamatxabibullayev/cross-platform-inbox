import os
import token
from fastapi import FastAPI, WebSocketDisconnect, Depends
from starlette.websockets import WebSocket
from auth import create_access_token, verify_password
import jwt

app = FastAPI()

SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")


@app.get("/")
def home():
    return {"message": "Cross-Platform Inbox API"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
