#!/usr/bin/env python3

# Script to read the Arriba output and write a Mavis compatible file
# (with extra comments for Python beginners)

import argparse, csv, re

# define functions first; in a script, functions must be defined before they are called

def parse_arriba_breakpoint(bp):
    # split the arriba breakpoint string
    # return a list with the chromosome and two copies of the position
    [chromosome, position] = re.split(':', bp)
    return [chromosome, position, position]

def read_arriba(input_path):
    # open the input file and parse the contents
    # output a list of lists with the desired output fields
    output = []
    with open(input_path) as fusions:
        # use the DictReader object to read each input line into a dictionary
        fusion_reader = csv.DictReader(fusions, delimiter='\t')
        for input_row in fusion_reader:
            output_row = []
            # we are only interested in the 'breakpoint1' and 'breakpoint2' input columns
            # 'extend' a list with the contents of another list
            # 'append' a list with a single item (which may itself be a list, to make a two-dimensional list of lists)
            output_row.extend(parse_arriba_breakpoint(input_row['breakpoint1']))
            output_row.extend(parse_arriba_breakpoint(input_row['breakpoint2']))
            output_row.append('arriba')
            output.append(output_row)
    return output

# define two command-line arguments: one positional (input), and one named (output)
parser = argparse.ArgumentParser(description='Convert Arriba output to Mavis compatible format')
parser.add_argument('input_path', help='Input path')
parser.add_argument('-o','--output', help='output file path',required=True)
# store the command-line arguments in a variable called "args"
args = parser.parse_args()

# read input and write output
# first construct the header line
output_header_fields = [
    'break1_chromosome',
    'break1_position_start',
    'break1_position_end',
    'break2_chromosome',
    'break2_position_start',
    'break2_position_end',
    'tools']
# 'join' is a method of String objects in Python
# '+'  is the string concatenation operator
output_header = '#'+"\t".join(output_header_fields)
# read input using the functions defined above
output = read_arriba(args.input_path)
# open the chosen output path; write the header line, followed by the output data
with open(args.output, 'w') as output_file:
    print(output_header, file=output_file)
    for row in output:
        print("\t".join(row), file=output_file)
