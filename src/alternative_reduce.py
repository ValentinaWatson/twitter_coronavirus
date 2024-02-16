#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

import argparse
import os
import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

def load_data(input_paths):
    """
    Load data from input paths and aggregate tweet counts per hashtag per day.
    """
    hashtag_counts = defaultdict(lambda: defaultdict(int))
    
    for path in input_paths:
        with open(path) as f:
            data = json.load(f)
            for day, hashtags in data.items():
                try:
                    day_int = int(day)
                except ValueError:
                    continue  # Skip keys that cannot be converted to integers
                for hashtag, count in hashtags.items():
                    hashtag_counts[hashtag][day_int] += count
    
    return hashtag_counts

def plot_hashtags(counts_per_hashtag):
    """
    Plot the change in frequency of hashtags throughout the years.
    """
    lines = []  # Store lines for legend
    labels = []  # Store corresponding labels for legend

    for hashtag, counts_per_day in counts_per_hashtag.items():
        days = sorted(counts_per_day.keys())
        counts = [counts_per_day[day] for day in days]

        print(f'Hashtag: {hashtag}, Counts: {counts}')  # Debugging statement

        line, = plt.plot(days, counts)  # Store line object
        lines.append(line)  # Add line to list

        labels.append(f'#{hashtag}')  # Add label for the line

    plt.xlabel('Day of the Year')
    plt.ylabel('Number of Tweets')
    plt.title('Change in Frequency of Hashtags Over Time')

    # Add legend with lines and labels
    plt.legend(lines, labels)

    plt.savefig('hashtags_over_time.png')
    plt.show()  # Display the plot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_paths', nargs='+', required=True)
    args = parser.parse_args()

    counts_per_hashtag = load_data(args.input_paths)
    plot_hashtags(counts_per_hashtag)

if __name__ == "__main__":
    main()
