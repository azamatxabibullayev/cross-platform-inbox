const ws = new WebSocket("ws://localhost:8000/ws");

ws.onopen = function () {
    console.log("Connected to server");
};

ws.onmessage = function (event) {
    console.log("New message:", event.data);
};

function sendMessage(text) {
    ws.send(text);
}
