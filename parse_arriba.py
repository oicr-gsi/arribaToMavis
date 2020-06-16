#!/.mounts/labs/gsi/modulator/sw/Ubuntu18.04/python-3.6/bin/python3

# script to read in arriba and output Mavis compatible file

import sys
import csv

def parse_arriba(row):
    fusion_list = {}

    with open(sys.argv[1], newline='') as fusions:
        fusion_reader = csv.DictReader(fusions, delimiter='\t')
        for row in fusion_reader:
           fusion_list.append(dict(row))

    return fusion_list
