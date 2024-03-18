#!/bin/bash

# # Define input and output file paths
# input_file="./README.md"
# output_file="./docs/source/readme.md"

# # Copy input file to output file overwriting it
# cp $input_file $output_file

# Build the docs locally
sphinx-build -M html docs/source/ docs/build/ -a