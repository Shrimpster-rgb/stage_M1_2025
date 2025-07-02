#! /usr/bin/bash

# All the path of the ms2nexus script
input_file=/c/Users/Nicolas/Desktop/Masters/M1_bioinfo/Stage/Stage_2025/BEAST/BEAST/test_BEAST_dengue/genome/250_genomes/raw_data/20250603-VKadh2msEU-0selection.msa
output_file=/c/Users/Nicolas/Desktop/Masters/M1_bioinfo/Stage/Stage_2025/BEAST/BEAST/test_BEAST_dengue/genome/250_genomes/input_data/test.nex

# All the path of the exctract_dates_location script
input_df=/c/Users/Nicolas/Desktop/Masters/M1_bioinfo/Stage/Stage_2025/BEAST/BEAST/test_BEAST_dengue/genome/250_genomes/raw_data/20250603-VKadh2msEU-0selection.tsv
output_dates=/c/Users/Nicolas/Desktop/Masters/M1_bioinfo/Stage/Stage_2025/BEAST/BEAST/test_BEAST_dengue/genome/250_genomes/input_data/test_dates.dat
output_locations=/c/Users/Nicolas/Desktop/Masters/M1_bioinfo/Stage/Stage_2025/BEAST/BEAST/test_BEAST_dengue/genome/250_genomes/input_data/test_location.dat
output_coords=/c/Users/Nicolas/Desktop/Masters/M1_bioinfo/Stage/Stage_2025/BEAST/BEAST/test_BEAST_dengue/genome/250_genomes/input_data/test_coords.csv

# The command line of the scripts

python msa2nexus.py $input_file $output_file
echo "conversion to nexus finished"

python extract_dates_location.py $input_df $output_dates $output_locations $output_coords
echo "conversion of the metadata finished"
