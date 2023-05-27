import os
import subprocess
import time

import numpy as np

from scripts import settings
from scripts.js import node, deno, bun

def NodeFetch():
    result = []
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        deno_process = node.run(['benchmark/node/fetching/fetch.js'])
        result.append(time.time() - start_time)

    print("--- %s seconds ---" % np.mean(result))
    print('node fetch json result')
    return result
def DenoFetch():
    result = []
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        deno_process = deno.run(['run', '--allow-net', 'benchmark/deno/fetching/fetch.ts'])
        result.append(time.time() - start_time)
    print("--- %s seconds ---" % np.mean(result))
    print('deno fetch json result')
    return result

def BunFetch():
    result = []
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        deno_process = bun.run(['benchmark/bun/fetching/fetch.js'])
        result.append(time.time() - start_time)
    print("--- %s seconds ---" % np.mean(result))
    print('bun fetch json result')
    return result


def HyperfineFetchTest(command, path):
    if settings.os == 'linux':
        jsonserver = subprocess.Popen(['json-server', 'db.json', '-q'])
    else:
        jsonserver = subprocess.Popen(['json-server', 'db.json', '-q'], shell=True)
    time.sleep(5)
    arr = ['hyperfine', '--warmup', '3', '--runs', '10', '--show-output', '--export-json',
                              os.path.abspath(path)]
    for el in command:
        arr.insert(5, el)
    result = subprocess.call(arr)
    jsonserver.kill()
