import time

import numpy as np

from scripts.js import node, deno, bun

def NodeFetch():
    result = []
    for i in range(10):
        start_time = time.time()
        deno_process = node.run(['benchmark/node/fetching/fetch.js'])
        result.append(time.time() - start_time)

    print("--- %s seconds ---" % np.mean(result))
    print('node fetch json result')
    return result
def DenoFetch():
    result = []
    for i in range(10):
        start_time = time.time()
        deno_process = deno.run(['run', '--allow-net', 'benchmark/deno/fetching/fetch.ts'])
        result.append(time.time() - start_time)
    print("--- %s seconds ---" % np.mean(result))
    print('deno fetch json result')
    return result

def BunFetch():
    result = []
    for i in range(10):
        start_time = time.time()
        deno_process = bun.run(['benchmark/bun/fetching/fetch.js'])
        result.append(time.time() - start_time)
    print("--- %s seconds ---" % np.mean(result))
    print('bun fetch json result')
    return result
