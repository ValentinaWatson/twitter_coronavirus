#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

import argparse
import os
import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

def load_data(input_paths):
    total = defaultdict(lambda: Counter())
    for path in input_paths:
        with open(path) as f:
            data = json.load(f)
            for hashtag, counts_per_day in data.items():
                total[hashtag].update(counts_per_day)
    return total

def plot_hashtags(counts_per_hashtag):
    days = range(1, len(next(iter(counts_per_hashtag.values()))) + 1)
    for hashtag, counts in counts_per_hashtag.items():
        plt.plot(days, list(counts), label=hashtag)

    plt.xlabel('Days')
    plt.ylabel('Number of Occurrences')
    plt.title('Number of Occurrences of Hashtags Over Time')
    plt.legend()

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
