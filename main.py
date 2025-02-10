from fastapi import FastAPI
from starlette.websockets import WebSocket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Cross-Platform Inbox API"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")
