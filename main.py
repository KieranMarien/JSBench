import os
import subprocess
import sys
import json
import numpy as np
import inquirer
from datetime import datetime
import time
from scripts.WebSocketBench import *
from scripts.SQLiteBench import *
from scripts.FetchBench import *
from scripts.httpserver import *



if sys.platform.startswith("linux") or sys.platform == "darwin":
    Runtimes = [
        inquirer.Checkbox('runtimes',
                          message='What runtimes would you like to test?',
                          choices=[('Node', 0), ('Deno', 1), ('Bun', 2)], ), ]
else:
    Runtimes = [
        inquirer.Checkbox('runtimes',
                          message='What runtimes would you like to test?',
                          choices=[('Node', 0), ('Deno', 1)], ), ]

Tests = [
    inquirer.Checkbox('tests',
                      message='What parts would you like to benchmark?',
                      choices=[('Fetch', 0), ('SQLiteRead', 1), ('SQLiteWrite',2), ('Websocket', 3), ('httpserver', 4)], ), ]

commandsWrite = ["node benchmark/node/sqlite/sqlite-write.js ",
                 "deno run --allow-read --allow-write benchmark/deno/sqlite/sqlite-write.ts ",
                 "bun benchmark/bun/sqlite/sqlite-write.ts "]
commandsRead = ["node benchmark/node/sqlite/sqlite-read.js ",
                "deno run --allow-read benchmark/deno/sqlite/sqlite-read.ts ",
                "bun benchmark/bun/sqlite/sqlite-read.ts "]

commandsFetch =["node benchmark/node/fetching/fetch.js ",
                'deno run --allow-net benchmark/deno/fetching/fetch.ts ',
                "bun benchmark/bun/fetching/fetch.js "]

commandsHttpServer= [

]
def CommandBuilder(runtimes, arr):
    res = []
    for runtime in runtimes:
        res.append(arr[runtime])
    return res


if __name__ == '__main__':
    date = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    os.makedirs('./results/' + date)
    path = './results/' + date

    # runtimesAnswers = inquirer.prompt(Runtimes)['runtimes']
    runtimesAnswers = [0, 1]
    print(runtimesAnswers)
    noderes = NodeWebsocket()
    print(noderes)
    denores = DenoWebsocket()
    print(denores)
    bunres = BunWebsocket()
    print(bunres)
    # benchAnswers = inquirer.prompt(Tests)['tests']
    benchAnswers = ['Fetch', 'SQLiteRead', 'SQLiteWrite', 'httpserver']
    benchAnswers = []
    print(benchAnswers)

    if len(runtimesAnswers) == 0:
        print('MIN 1 value for runtimes')
        runtimesAnswers = inquirer.prompt(Runtimes)

    if len(benchAnswers) == 0:
        print('MIN 1 value for benchmarks')
        runtimesAnswers = inquirer.prompt(Runtimes)

    if 0 in benchAnswers:
        fetch = CommandBuilder(runtimesAnswers, commandsFetch)
        HyperfineFetchTest(fetch, path + '/fetch.json')
    if 1 in benchAnswers:
        read = CommandBuilder(runtimesAnswers, commandsRead)
        HyperfineReadTest(read, path + "/sqliteread.json")
    if 2 in benchAnswers:
        write = CommandBuilder(runtimesAnswers, commandsWrite)
        HyperfineWriteTest(write, path + "/sqlitewrite.json")
    if 4 in benchAnswers:
        os.makedirs(path + '/httpserver')
        http = ohaTests(runtimesAnswers, path + '/httpserver/')







""" if __name__ == '__main__':
    print('warning: BUN WEBSOCKET DOES NOT WORK')
    jsonserver = subprocess.Popen(['json-server', 'db.json'], shell=True)
    time.sleep(10)

    start_time = time.time()

    print('bun sqlite write result')
    #runtimesAnswers = inquirer.prompt(Runtimes)['runtimes']
    runtimesAnswers = ['Node', 'Deno']
    print(runtimesAnswers)
    #benchAnswers = inquirer.prompt(Tests)['tests']
    benchAnswers = ['Fetch', 'SQLiteRead', 'SQLiteWrite', 'httpserver']
    print(benchAnswers)

    if len(runtimesAnswers) == 0:
        print('MIN 1 value for runtimes')
        runtimesAnswers = inquirer.prompt(Runtimes)

    if len(benchAnswers) == 0:
        print('MIN 1 value for benchmarks')
        runtimesAnswers = inquirer.prompt(Runtimes)
    print(globals())
    allResults = dict()
    for runtime in runtimesAnswers:
        for bench in benchAnswers:
            function = runtime + bench
            if function in globals() and callable(globals()[function]):
                res = globals()[function]()
                allResults.update({function: res})
    print(allResults)

    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d-%H-%M-%S.json")

    with open(filename, 'w') as fp:
        json.dump(allResults, fp, sort_keys=True, indent=4)

    jsonserver.kill()
    end = time.time() - start_time
    print("--- %s seconds ---" % end)

    '''
    df = FetchBench.DenoJSON()
    nf = FetchBench.NodeJSON()
    if (sys.platform.startswith("linux") or sys.platform == "darwin"):
        bf = FetchBench.BunJSON()
        print("--- %s seconds ---" % np.mean(bf))
        print('bun fetch json result')

    print("--- %s seconds ---" % np.mean(df))
    print('deno fetch json result')

    print("--- %s seconds ---" % np.mean(nf))
    print('node fetch json result')
    '''

"""
"""
    dr = SQLiteBench.Deno_Read()
    dw = SQLiteBench.Deno_Write()
    nr = SQLiteBench.Node_Read()
    nw = SQLiteBench.Node_Write()

    if (sys.platform.startswith("linux") or sys.platform == "darwin"):
        br = SQLiteBench.Bun_Read()
        bw = SQLiteBench.Bun_Write()

        print("--- %s seconds ---" % np.mean(br))
        print('Bun sqlite read result')
        print("--- %s seconds ---" % np.mean(bw))
        print('Bun sqlite write result')

    print("--- %s seconds ---" % np.mean(dr))
    print('deno sqlite read result')

    print("--- %s seconds ---" % np.mean(dw))
    print('deno sqlite write result')

    print("--- %s seconds ---" % np.mean(nr))
    print('node sqlite read result')

    print("--- %s seconds ---" % np.mean(nw))
    print('node sqlite write result')
    """
