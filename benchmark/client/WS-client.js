var WebSocket  = require('ws');
console.log('start');
let clients = [];
let clientid = 0
let messageCount = 0;
const NUMBEROFCLIENTS = 64

for (let i = 0; i < NUMBEROFCLIENTS; i++) {
  let client = new WebSocket('ws://127.0.0.1:3001');
  client.on('open', function(){
    clients.push(client);
    if(clients.length == NUMBEROFCLIENTS){
      sendMessage()
    }
  });
  client.on('message', function (){
    messageCount +=1;
    if(messageCount == NUMBEROFCLIENTS){
      clientid +=1
      sendMessage()
    }
  });
}

function sendMessage(){
    messageCount = 0;
    if(clientid < NUMBEROFCLIENTS){
      clients[clientid].send('message');
    }else{
      process.exit()
    }
};


