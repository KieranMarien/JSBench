
import sys

import numpy as np

from scripts import WebSocketBench
from scripts import SQLiteBench
from scripts import FetchBench

if sys.platform.startswith("linux") or sys.platform == "darwin":
    pass


if __name__ == '__main__':
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

