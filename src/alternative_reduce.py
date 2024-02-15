#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

import argparse
import os
import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

def load_data(input_paths):
    total = Counter()
    for path in input_paths:
        with open(path) as f:
            data = json.load(f)
            for counts_per_day in data.values():
                total.update(counts_per_day)
    return total

def plot_hashtags(counts_per_hashtag):
    # Sort the dictionary keys (days)
    sorted_days = sorted(counts_per_hashtag.keys())
    
    for hashtag, counts in counts_per_hashtag.items():
        print(f"Hashtag: {hashtag}, Counts: {counts}")
        # Extract the counts for the current hashtag and sort them based on the corresponding days
        sorted_counts = [counts[day] for day in sorted_days]
        plt.plot(sorted_days, sorted_counts, label=hashtag)
    
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
