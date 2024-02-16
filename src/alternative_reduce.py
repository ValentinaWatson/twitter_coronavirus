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



def plot_hashtags(hashtag_counts):
    """
    Plot the number of tweets for each hashtag over time.
    """
    for hashtag, counts_per_day in hashtag_counts.items():
        days = sorted(counts_per_day.keys())
        counts = [counts_per_day[day] for day in days]
        plt.plot(days, counts, label=f'#{hashtag}')  # Add label for legend

    plt.xlabel('Day of the Year')
    plt.ylabel('Number of Tweets')
    plt.title('Number of Tweets for Each Hashtag Over Time')
    plt.legend()  # Add legend

    plt.show()  # Display the plot



def main():
    parser = argparse.ArgumentParser(description="Plot tweet counts for specified hashtags.")
    parser.add_argument('--input_paths', nargs='+', required=True, help="List of input paths containing tweet data.")
    args = parser.parse_args()

    # Load data from input paths
    hashtag_counts = load_data(args.input_paths)

    # Plot tweet counts per hashtag per day
    plot_hashtags(hashtag_counts)

if __name__ == "__main__":
    main()
