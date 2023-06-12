#!/usr/bin/env python

import argparse
import json
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("file", help="JSON file with benchmark results")
args = parser.parse_args()

with open(args.file) as f:
    results = json.load(f)["results"]

commands = [b["command"] for b in results]
times = [b["times"] for b in results]

# Create a list of time data for each command
data = [np.array(ts) for ts in times]

# Plotting the box graph with swapped axes
plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=commands, sym='k+')
plt.title("Execution Time Distribution")
plt.xlabel("Command")
plt.ylabel("Time (s)")
plt.grid(True)

# Move the legend to the bottom
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=len(commands))

plt.show()
