#!/usr/bin/env bash

#count and sort  each species in all files

for filename in data_*.txt
do
    echo $filename
    python species_counts.py $filename | sort -k 2 -n
done
