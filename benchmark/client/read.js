import { setImmediate } from "https://deno.land/std@0.140.0/node/timers.ts";

Deno.readFile('./file.txt', () => {
  setTimeout(() => console.log('setTimeout'), 0);
  setImmediate(() => console.log('setImmediate'));
});
