import os
import time

import numpy as np

from scripts import settings
from scripts.js import bun, deno, node


def DenoSQLiteRead():
    result = []
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        deno_process = deno.run(['run', '--import-map=benchmark/deno/sqlite/vendor/import_map.json', '--allow-read', 'benchmark/deno/sqlite/sqlite-read.ts'])
        result.append(time.time() - start_time)

    print("--- %s seconds ---" % np.mean(result))
    print('deno sqlite read result')
    return result


def DenoSQLiteWrite():
    file_path = 'deno.sqlite'
    result = []
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        deno_process = deno.run(['run', '--import-map=benchmark/deno/sqlite/vendor/import_map.json', '--allow-read', '--allow-write', 'benchmark/deno/sqlite/sqlite-write.ts'])
        result.append(time.time() - start_time)
        if os.path.isfile(file_path):
            os.remove(file_path)

    print("--- %s seconds ---" % np.mean(result))
    print('deno sqlite write result')
    return result



def NodeSQLiteRead():
    result = []
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        node_process = node.run(['benchmark/node/sqlite/sqlite-read.js'])
        result.append(time.time() - start_time)

    print("--- %s seconds ---" % np.mean(result))
    print('node sqlite read result')
    return result

def NodeSQLiteWrite():
    file_path = 'node.sqlite'

    result = []
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        node_process = node.run(['benchmark/node/sqlite/sqlite-write.js'])
        result.append(time.time() - start_time)
        if os.path.isfile(file_path):
            os.remove(file_path)

    print("--- %s seconds ---" % np.mean(result))
    print('node sqlite write result')
    return result


def BunSQLiteRead():
    result = []
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        bun_process = bun.run(['benchmark/bun/sqlite/sqlite-read.ts'])
        result.append(time.time() - start_time)

    print("--- %s seconds ---" % np.mean(result))
    print('bun sqlite read result')
    return result

def BunSQLiteWrite():
    file_path = 'bun.sqlite'

    result = []
    for i in range(settings.NumberOfTests):
        if os.path.isfile(file_path):
            os.remove(file_path)
        start_time = time.time()
        bun_process = bun.run(['benchmark/bun/sqlite/sqlite-read.ts'])
        result.append(time.time() - start_time)

    print("--- %s seconds ---" % np.mean(result))
    print('bun sqlite write result')
    return result

