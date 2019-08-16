#!/bin/bash

# cut first 12 lines from xvg file

tail -200 histo.xvg > hist.csv

# chop up file into 5 files with 5 histograms each (first one contains the z values as well)

awk '{print $1, $2, $3, $4, $5, $6}' hist.csv > hist1_5.csv
awk '{print $7,	$8, $9,	$10, $11}' hist.csv > hist6_10.csv
awk '{print $12, $13, $14, $15, $16}' hist.csv > hist11_15.csv
awk '{print $17, $18, $19, $20, $21, $22}' hist.csv > hist16_21.csv




