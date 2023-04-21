async function main() {
    Bun.serve({
        port: 5000,
        fetch(request) {
          return new Response('Hello World! From Bun');
        },
      });
}

main()
