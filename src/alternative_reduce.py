#!/usr/bin/env python3

import argparse
import os
import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')

def load_data(input_paths):
    total = Counter()
    for path in input_paths:
        with open(path) as f:
            data = json.load(f)
            for counts_per_day in data.values():
                total.update(counts_per_day)
    return total

def plot_hashtags(counts_per_hashtag):
    plt.plot(range(1, len(counts_per_hashtag) + 1), list(counts_per_hashtag.values()))

    plt.xlabel('Days')
    plt.ylabel('Number of Occurrences')
    plt.title('Number of Occurrences of Hashtags Over Time')
    plt.savefig('hashtags_over_time.png')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_paths', nargs='+', required=True)
    parser.add_argument('--output_path', required=True)
    args = parser.parse_args()

    counts_per_hashtag = load_data(args.input_paths)
    plot_hashtags(counts_per_hashtag)

if __name__ == "__main__":
    main()
