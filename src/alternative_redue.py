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

# combine values of each hashtag in each day's file
hashtagDict = defaultdict(lambda: Counter())
yAxisPoints = []
xAxisPoints = []
for dayFile in args.input_paths:
  with open(dayFile) as f:
    data = json.load(f)
    for hashtag, country_counts in data.items():
      countryCombine = sum(country_counts.values())
      hashtagDict[hashtag] += countryCombine
    yAxisPoints.append(hashtagDict[hashtag])
    xAxisPoints.append(dayFile[10:18])
    
# traverse through each counted file and find the most popular hashtags


# plot them




