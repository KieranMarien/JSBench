#!/usr/bin/env python

import argparse
import csv
import json
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file", help="JSON file with benchmark results")
parser.add_argument("output", help="Output CSV file")
args = parser.parse_args()

with open(args.file) as f:
    results = json.load(f)["results"]

commands = [b["command"] for b in results]
times = [b["times"] for b in results]

with open(args.output, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["Command", "Runs", "Mean", "StdDev", "Median", "Min", "Max", "P05", "P25", "P75", "P95"])

    for command, ts in zip(commands, times):
        p05 = np.percentile(ts, 5)
        p25 = np.percentile(ts, 25)
        p75 = np.percentile(ts, 75)
        p95 = np.percentile(ts, 95)

        iqr = p75 - p25

        writer.writerow([
            command,
            len(ts),
            np.mean(ts),
            np.std(ts, ddof=1),
            np.median(ts),
            np.min(ts),
            np.max(ts),
            p05,
            p25,
            p75,
            p95
        ])
