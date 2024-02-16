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
    max_length = max(len(counts) for counts in counts_per_hashtag.values())
    days = range(1, max_length + 1)  # Ensure days cover the entire range of data
    
    for hashtag, counts in counts_per_hashtag.items():
        # Ensure counts cover all days, fill missing data with zeros
        counts += [0] * (max_length - len(counts))
        plt.plot(days, counts, label=hashtag)

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
