#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

import argparse
import os
import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

def load_data(input_paths):
    total = defaultdict(list)
    max_length = 0  
    for path in input_paths:
        with open(path) as f:
            data = json.load(f)
            for counts_per_day in data.values():
                for hashtag, count in counts_per_day.items():
                    total[hashtag].append(count)
                max_length = max(max_length, len(counts_per_day))

    for counts in total.values():
        while len(counts) < max_length:
            counts.append(0)

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
