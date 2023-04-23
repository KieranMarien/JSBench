import time

import numpy as np
import websocket
from scripts.js import bun, deno, node
from scripts import settings
import os
import asyncio
import json

SERVER_NODE = 'http://127.0.0.1:3001'
SERVER_DENO = 'ws://127.0.0.1:4001'
SERVER_BUN = 'ws://127.0.0.1:5001'



def create_messages(n, word):
    messages = []
    for i in range(1, n + 1):
        message = word + str(i)
        messages.append(message)
    return messages



def webSocketTester(SERVER):
    MESSAGES_TO_SEND = create_messages(50, 'message')
    NAMES = create_messages(16, 'name')
    finshed = False


    clients = []
    numberOfConnectedClients = 0
    numberOfMessages = 0
    def start_messages():
        global numberOfMessages
        for client in clients:
            client.send('message')
            while numberOfMessages < 16:
                time.sleep(0.1)
            numberOfMessages = 0
        return
    def on_client_message():
        global numberOfMessages
        numberOfMessages += 1
    def on_client_connect(ws):
        ws.run_forever()
        clients.append(ws)
        global numberOfConnectedClients
        numberOfConnectedClients +=1

    for w in range(16):
        print(w)
        print('ws')
        ws = websocket.WebSocketApp(SERVER,
                                    on_open=lambda: on_client_connect(ws),
                                    on_message=on_client_message)

    while numberOfConnectedClients < 16:
        time.sleep(1)
    start_messages()
    return True

def NodeWebsocket():
    result = []
    for i in range(settings.NumberOfTests):
        print(i)
        node_process = node.Popen(['benchmark/node/websocket/WS-server.js'])
        time.sleep(3)
        start_time = time.time()
        node_client_process = node.run(['benchmark/client/WS-client.js'])
        result.append(time.time() - start_time)
        node_process.kill()
        while(node_process.poll()):
            time.sleep(0.1)
    return np.mean(result)

def DenoWebsocket():
    result = []
    for i in range(settings.NumberOfTests):
        print(i)
        deno_process = deno.Popen(['run', '--allow-net', 'benchmark/deno/websocket/WS-server.ts'])
        time.sleep(3)
        start_time = time.time()
        node_client_process = node.run(['benchmark/client/WS-client.js'])
        result.append(time.time() - start_time)
        deno_process.kill()
        while(deno_process.poll()):
            time.sleep(0.1)
    return np.mean(result)

def BunWebsocket():
    result = []
    for i in range(settings.NumberOfTests):
        bun_process = bun.Popen(['benchmark/bun/websocket/WS-server.js'])
        time.sleep(3)
        start_time = time.time()
        webSocketTester(SERVER_BUN)
        result.append(time.time() - start_time)
        bun_process.kill()
    return result
