const ws = new WebSocket("ws://localhost:8080/pipe");

ws.onmessage = function(e) {
    document.getElementById("text").innerHTML = e.data;
}