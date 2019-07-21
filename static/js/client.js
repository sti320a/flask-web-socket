const ws = new WebSocket("ws://localhost:5000/pipe");

ws.onmessage = function(e) {
    document.getElementById("text").innerHTML = e.data;
}