
let clients = [];

const server = Bun.serve({
  port: 3001,
  fetch(req, server) {
    // upgrade the request to a WebSocket
    if (server.upgrade(req)) {
      return; // do not return a Response
    }
    return new Response("Upgrade failed :(", { status: 500 });
  },
  websocket: {
    open(ws) {
      clients.push(ws);
    },
    message(ws, msg) {
      for (const client of clients) {
        client.send(msg);
      }
    },
    close(ws) {
          clients = []

    },
  },
});