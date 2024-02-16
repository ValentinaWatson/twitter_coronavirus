#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

import argparse
import os
import json
from collections import defaultdict
import matplotlib.pyplot as plt

def load_data(input_folder):
    """
    Load data from input folder and aggregate tweet counts per hashtag per day.
    """
    hashtag_counts = defaultdict(lambda: defaultdict(int))

    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            path = os.path.join(input_folder, filename)
            print(f"Processing input file: {path}")
            with open(path) as f:
                data = json.load(f)
                for day, hashtags in data.items():
                    try:
                        day_int = int(day)
                    except ValueError:
                        continue  # Skip keys that cannot be converted to integers
                    for hashtag, count in hashtags.items():
                        hashtag_counts[hashtag][day_int] += count

    # Print the loaded data for debugging
    print("Loaded data:")
    for hashtag, counts_per_day in hashtag_counts.items():
        print(f"Hashtag: {hashtag}, Counts Length: {len(counts_per_day)}")

    return hashtag_counts


def plot_hashtags(counts_per_hashtag, hashtags):
    """
    Plot the change in frequency of specified hashtags throughout the year.
    """
    lines = []  # Store lines for legend
    labels = []  # Store corresponding labels for legend

    for hashtag in hashtags:
        counts_per_day = counts_per_hashtag.get(hashtag, {})
        days = sorted(counts_per_day.keys())
        counts = [counts_per_day[day] for day in days]

        print(f'Hashtag: {hashtag}, Counts: {counts}')  # Debugging statement

        line, = plt.plot(days, counts)  # Store line object
        lines.append(line)  # Add line to list

        labels.append(f'#{hashtag}')  # Add label for the line

    plt.xlabel('Day of the Year')
    plt.ylabel('Number of Tweets')
    plt.title('Change in Frequency of Specified Hashtags Over Time')

    # Add legend with lines and labels
    plt.legend(lines, labels)

    plt.savefig('specified_hashtags_over_time.png')
    plt.show()  # Display the plot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', required=True)
    parser.add_argument('--hashtags', nargs='+', required=True)
    args = parser.parse_args()

    counts_per_hashtag = load_data(args.input_folder)
    plot_hashtags(counts_per_hashtag, args.hashtags)

if __name__ == "__main__":
    main()
