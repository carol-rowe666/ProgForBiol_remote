#!/bin/bash

#Assignment2 concatenate, sort with unique only, and run through python code.

cat areas*.txt | python rich_pred.py | sort -t',' -nk2 -u > predicted_diversities.txt

