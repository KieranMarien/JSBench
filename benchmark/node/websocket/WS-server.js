var WebSocketServer = require("ws").Server,
  config = {
    host: "127.0.0.1",
    port: 3001
  },
  wss = new WebSocketServer(config, function () {
  });

let clients = [];
wss.on('connection', function(ws) {
  clients.push(ws);
  ws.on('message', function (message) {
    for(let client of clients){
      client.send(message);
    }
  });
  ws.on('close', function(){
        console.log(clients.length)
  })
});
