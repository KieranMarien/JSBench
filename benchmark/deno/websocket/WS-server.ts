import { WebSocketClient, WebSocketServer } from "https://deno.land/x/websocket@v0.1.4/mod.ts";


const wss = new WebSocketServer(3001);
let clients : WebSocketClient[] = []
wss.on("connection", function (ws: WebSocketClient) {
  ws.on("message", function (message: string) {
    for(let client of clients){
      client.send('message')
    }
  });
  ws.on('close', function(){
    console.log(clients.length)
  })
  clients.push(ws)
});