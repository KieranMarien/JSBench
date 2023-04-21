
https://bun.sh/async function main() {
    Bun.serve({
  port: 5001,
  websocket: {
    message(ws, msg) {
      ws.send( msg);
    },
  },

  fetch(req, server) {
    if (
      server.upgrade(req, {
        data: {
          name: 'client'
        },
      })
    )
      return;
    return new Response("Error");
  },
});
}

main()