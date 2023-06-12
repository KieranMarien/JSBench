
let clients = [];

const server = Bun.serve({
  port: 3001,
  fetch(req, server) {
    if (server.upgrade(req)) {
      return;
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