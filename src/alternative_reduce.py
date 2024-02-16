#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
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
for dayFile in args.input_path:
  with open(dayFile) as f:
    data = json.load(f)
    for hashtag, country_counts in data.items():
      countryCombine = sum(country_counts.values())
      hashtagDict[hashtag] += Counter({len(hashtagDict[hashtag]) + 1: countryCombine})

# traverse through each counted file and plot the hashtags
for hashtag, counts_per_day in hashtagDict.items():
    x_values = list(range(1, len(counts_per_day) + 1))
    y_values = list(counts_per_day.values())
    plt.plot(x_values, y_values, label=hashtag)

plt.xlabel('Days')
plt.ylabel('Number of Occurrences')
plt.title('Number of Occurrences of Hashtags Over Time')
plt.legend()

# save the plot
plt.savefig('hashtags_over_time.png')
