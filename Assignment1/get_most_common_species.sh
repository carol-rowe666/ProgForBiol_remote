#!/bin/bash
curl -O http://www.programmingforbiologists.org/data/data_drycanyon_2013.txt
sort -k 3 -n data_drycanyon_2013.txt | tail -1 > most_common_species.txt

