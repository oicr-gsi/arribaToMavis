#!/usr/bin/env python3

# script to read in arriba and output Mavis compatible file

import sys
import csv
import argparse

parser = argparse.ArgumentParser(description='output file')

parser.add_argument('-o','--output', help='output file path',required=True)
args = parser.parse_args()

print(args.name)

def parse_arriba(row):
    fusion_list = {}

    with open(sys.argv[1], newline='') as fusions:
        fusion_reader = csv.DictReader(fusions, delimiter='\t')
        for row in fusion_reader:
           fusion_list.append(dict(row))
        
        return(fusion_list)
