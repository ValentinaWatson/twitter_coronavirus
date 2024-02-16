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
    hashtags = set()  # Store unique hashtags
    
    for path in input_paths:
        print(f"Processing input path: {path}")
        with open(path) as f:
            data = json.load(f)
            for day, hashtags_per_day in data.items():
                try:
                    day_int = int(day)
                except ValueError:
                    continue  # Skip keys that cannot be converted to integers
                for hashtag, counts_per_country in hashtags_per_day.items():
                    hashtag_counts[hashtag][day_int] += counts_per_country
                    hashtags.add(hashtag)
    
    # Print the loaded data for debugging
    print("Loaded data:")
    for hashtag, counts_per_day in hashtag_counts.items():
        print(f"Hashtag: {hashtag}, Counts Length: {len(counts_per_day)}")
    
    return hashtag_counts, hashtags


def extract_hashtags(data):
    """
    Extract unique hashtags from the loaded data.
    """
    hashtags = set()
    for hashtags_by_country in data.values():
        for hashtags_per_day in hashtags_by_country.values():
            for hashtag in hashtags_per_day.keys():
                hashtags.add(hashtag)
    return hashtags

def plot_hashtags(counts_per_hashtag, hashtags):
    """
    Plot the change in frequency of hashtags throughout the years.
    """
    lines = []  # Store lines for legend

    for hashtag in hashtags:
        counts_per_day = counts_per_hashtag[hashtag]
        days = sorted(counts_per_day.keys())
        counts = [counts_per_day[day] for day in days]

        print(f'Hashtag: {hashtag}, Counts: {counts}')  # Debugging statement

        line, = plt.plot(days, counts, label=f'#{hashtag}')  # Store line object
        lines.append(line)  # Add line to list

    plt.xlabel('Day of the Year')
    plt.ylabel('Number of Tweets')
    plt.title('Change in Frequency of Hashtags Over Time')

    # Add legend with lines and labels
    plt.legend()

    plt.savefig('hashtags_over_time.png')
    plt.show()  # Display the plot



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_paths', nargs='+', required=True)
    args = parser.parse_args()

    counts_per_hashtag, hashtags = load_data(args.input_paths)
    plot_hashtags(counts_per_hashtag, hashtags)


if __name__ == "__main__":
    main()
