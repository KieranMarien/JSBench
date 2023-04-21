import requests
import time
import numpy as np
from scripts.js import bun, deno, node

def Nodehttpserver():
    # node.call(['-v'])
    node_process = node.Popen(['benchmark/node/http-server/http-server.js'])
    time.sleep(3)
    result = []
    for i in range(10):
        start_time = time.time()
        res = requests.get('http://127.0.0.1:3000')
        result.append(time.time() - start_time)
    node_process.kill()
    print(res.text)
    print("--- %s seconds ---" % np.mean(result))
    print('node result  ^')
    return result

def Denohttpserver():
    # deno.call(['--version'])
    deno_process = deno.Popen(['run', '--allow-net', 'benchmark/deno/http-server.ts'])
    time.sleep(3)
    result = []
    for i in range(10):
        start_time = time.time()
        res = requests.get('http://127.0.0.1:4000')
        result.append(time.time() - start_time)
    deno_process.kill()

    print(res.text)
    print("--- %s seconds ---" % np.mean(result))
    print('deno result  ^')
    return result

def Bunhttpserver():
    bun.run(['-v'])
    bun_process = bun.Popen(['./benchmark/bun/http-server.js'])
    time.sleep(2)
    result = []
    for i in range(10):
        start_time = time.time()
        res = requests.get('http://localhost:5000')
        result.append(time.time() - start_time)
    print(res.text)
    print("--- %s seconds ---" % np.mean(result))
    print('bun result  ^')
    bun_process.kill()
    return result
