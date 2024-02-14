#!/bin/sh

for i in /data/Twitter\ dataset/geoTwitter20*; do
    nohup ./src/map.py --input_path="$i" &
done


