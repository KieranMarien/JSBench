import os
import subprocess


def HyperfineMongoReadTest(command, path):
    arr = ['hyperfine', '--warmup', '3', '--runs', '10', '--show-output', '--export-json',
                              os.path.abspath(path)]
    for el in command:
        arr.insert(5, el)
    result = subprocess.call(arr)

def HyperfineMongoWriteTest(command, path):
    arr = ['hyperfine', '--warmup', '3', '--runs', '10', '--show-output', '--export-json',
                              os.path.abspath(path)]
    for el in command:
        arr.insert(5, el)
    result = subprocess.call(arr)
