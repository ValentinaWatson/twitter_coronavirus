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
    hashtags = set()
    
    for path in input_paths:
        print(f"Processing input path: {path}")
        with open(path) as f:
            data = json.load(f)
            for hashtags_by_country in data.values():
                for hashtags_per_day in hashtags_by_country.values():
                    for hashtag, counts_per_country in hashtags_per_day.items():
                        for country, count in counts_per_country.items():
                            hashtag_counts[hashtag][country] += count
                            hashtags.add(hashtag)
    
    # Print the loaded data for debugging
    print("Loaded data:")
    for hashtag, counts_per_country in hashtag_counts.items():
        print(f"Hashtag: {hashtag}, Counts Length: {len(counts_per_country)}")
    
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
    labels = []  # Store corresponding labels for legend

    for hashtag in hashtags:
        counts_per_country = counts_per_hashtag.get(hashtag, {})
        countries = sorted(counts_per_country.keys())
        counts = [counts_per_country[country] for country in countries]

        print(f'Hashtag: {hashtag}, Counts: {counts}')  # Debugging statement

        line, = plt.plot(countries, counts)  # Store line object
        lines.append(line)  # Add line to list

        labels.append(f'#{hashtag}')  # Add label for the line

    plt.xlabel('Country Code')
    plt.ylabel('Number of Tweets')
    plt.title('Tweet Counts for Selected Hashtags by Country')

    # Add legend with lines and labels
    plt.legend(lines, labels)

    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels

    plt.savefig('hashtags_by_country.png')
    plt.show()  # Display the plot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_paths', nargs='+', required=True)
    args = parser.parse_args()

    counts_per_hashtag, hashtags = load_data(args.input_paths)
    plot_hashtags(counts_per_hashtag, hashtags)

if __name__ == "__main__":
    main()
