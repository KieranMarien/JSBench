#!/usr/bin/env python

import argparse
import json
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("file", help="JSON file with benchmark results")
parser.add_argument("--title", help="Plot Title")
parser.add_argument("--labels", help="Comma-separated list of entries for the plot legend")
parser.add_argument("-o", "--output", help="Save image to the given filename.")

args = parser.parse_args()

with open(args.file) as f:
    results = json.load(f)["results"]

if args.labels:
    labels = args.labels.split(",")
else:
    labels = [b["command"] for b in results]
times = [b["times"] for b in results]

fig, axs = plt.subplots(len(times), 1, figsize=(8, 6 * len(times)))

for i in range(len(times)):
    min_time = min(times[i]) - 0.05 * min(times[i])
    max_time = max(times[i]) + 0.05 * max(times[i])
    cmap = plt.get_cmap("rainbow")
    color = cmap(i / len(times))

    boxplot = axs[i].boxplot([times[i]], vert=False, patch_artist=True, boxprops=dict(facecolor=color, linewidth=1.5))

    axs[i].set_xlabel("Time [s]")
    axs[i].set_ylabel("Benchmark")
    axs[i].set_xlim(min_time, max_time)  # Set x-axis limits based on maximum time value
    axs[i].set_yticks([])
    axs[i].set_title(args.title)
    axs[i].legend(handles=boxplot["boxes"], labels=[labels[i][:4]], loc="upper left", fontsize="medium")
if args.output:
    plt.savefig(args.output)
else:
    plt.subplots_adjust(hspace=0.30)
    plt.show()
