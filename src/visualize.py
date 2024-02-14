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
import matplotlib
matplotlib.use('Agg')
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

# build horizontal bar chart for .country_code files
if "country_code" in args.input_path:
    plt.barh(topKeys, topValues)
    plt.xlabel('Number of Instances')
    plt.ylabel('Country')
    plt.savefig(args.key + '_fig-country_code.png')
    plt.close()

# build horizontal bar chart for .lang files
if "lang" in args.input_path:
    plt.barh(topKeys, topValues)
    plt.xlabel('Number of Instances')
    plt.ylabel('Language')
    plt.savefig(args.key + '_fig-lang.png')
    plt.close()
