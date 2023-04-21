import { serve } from "https://deno.land/std@0.181.0/http/server.ts";

async function main() {
    const port = 4000
    function handler(_req: Request): Response {
      return new Response('Hello World! From Deno');
    }
    serve(handler, {port});
}

main()


