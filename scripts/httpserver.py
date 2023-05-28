import subprocess

import requests
import time
import numpy as np
from scripts.js import bun, deno, node
from scripts import settings


def Nodehttpserver():
    node_process = node.Popen(['benchmark/node/http-server/http-server.js'])
    time.sleep(3)
    result = []
    for i in range(settings.NumberOfTests):
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
    for i in range(settings.NumberOfTests):
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
    for i in range(settings.NumberOfTests):
        start_time = time.time()
        res = requests.get('http://localhost:5000')
        result.append(time.time() - start_time)
    print(res.text)
    print("--- %s seconds ---" % np.mean(result))
    print('bun result  ^')
    bun_process.kill()
    return result


def ohaTests(runtimes, path):
    out = []
    if 0 in runtimes:
        nodeServer = node.Popen(['benchmark/node/http-server/http-server.js'])
        f = open(path + 'httpnode.json', 'a')
        if settings.os == 'linux':
            result = subprocess.call(
                ["oha", 'http://127.0.0.1:3000', '-n', '1000', '-c', '100', '-j'], stdout=f)
        else:
            result = subprocess.call(
                ["oha.exe", 'http://127.0.0.1:3000', '-n', '1000', '-c', '100', '-j'], stdout=f, shell=True)
        f.close()
        nodeServer.kill()
    if 1 in runtimes:
        denoServer = deno.Popen(['run', '--allow-net', 'benchmark/deno/http-server.ts'])
        f = open(path + 'httpdeno.json', 'a')
        if(settings.os == 'linux'):
            result = subprocess.call(
            ["oha", 'http://127.0.0.1:4000', '-n', '1000', '-c', '100', '-j'], stdout=f)
        else:
            result = subprocess.call(
                ["oha.exe", 'http://127.0.0.1:4000', '-n', '1000', '-c', '100', '-j'], stdout=f, shell=True)
        f.close()
        denoServer.kill()
    if 2 in runtimes:
        bunServer = bun.Popen(['benchmark/bun/http-server.ts'])
        f = open(path + 'httpbun.json', 'a')
        if(settings.os == 'linux'):
            result = subprocess.call(
                ["oha", 'http://127.0.0.1:3000', '-n', '1000', '-c', '100', '-j'], stdout=f)
        else:
            result = subprocess.call(
                ["oha.exe", 'http://127.0.0.1:3000', '-n', '1000', '-c', '100', '-j'], stdout=f, shell=True)
        f.close
        bunServer.kill()
