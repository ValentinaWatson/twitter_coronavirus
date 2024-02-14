#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# get top 10 keys and values separately
topKeys = []
topValues = []
for key, value in items[:10]:
    topKeys.append(key)
    topValues.append(value)
numDatapoints = len(topKeys)

fig, ax = plt.subplots()

# build horizontal bar chart for .lang files
if args.input_path[-1] == "g":
    ax.barh(range(numDatapoints), topValues, align='center')
    ax.set_yticks(range(numDatapoints))
    ax.set_yticklabels(topKeys)
    ax.set_xlabel('Number of Instances')
    ax.set_title('Instances of '#coronavirus' per language')

# build horizontal bar chart for .country_code files
if args.input_path[-1] == "e":
    ax.barh(range(numDatapoints), topValues, align='center')
    ax.set_yticks(range(numDatapoints))
    ax.set_yticklabels(topKeys)
    ax.set_xlabel('Number of Instances')
    ax.set_title('Instances of '#coronavirus' per country')

plt.show()
