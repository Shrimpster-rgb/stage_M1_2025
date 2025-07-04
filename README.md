# Internship M1 Bioinformatics
This repository contain all the code used during my internship

# Context of the internship
The intership consist in a phylodynamic study of the dengue virus using the open source software [BEAST2](https://www.beast2.org/). 
This software use Bayesian inference to create numerous possible tree. Those tree can be used afterward to reconstruct all the phylogeny of the virus.
The goal of this study consist in a comparison between this method and the maximum likelihood to see if the maximum likelihood are as rosbust as the Byesian inference.

# Version and packages needed

Those script are write in the `Python 3.12.3` version. Be aware that if you use an older version some tools used here may be not working.

To run those scripts we need the following packages :

- `argparse` : Used to parse all the arguments in the command line
- `pandas` : Used to manipulate the metadata
- `geopy` : Used to collect all the coordinates needed for phylogeography
- `biopython` : Used to process the FASTA file in a more compact and clear way


# Code used 
In this repository we have 3 scripts :

- `msa2nexus.py` : This script convert a FASTA file in input into a NEXUS one in output.

### The usage of this script is :

`python msa2nexus.py input_file_path output_file_path`

  *input_file_path* : The path and name of the input file (.FASTA, .MSA...)
  
  *output_file_path* : The path and name of the output file 

- `extract_dates_location.py` : This script extract all the metadata of an additionnal file that be needed by BEAST to do phylogenic analysis (dates, location).
This script create also a file that contain all the geographic informations needed by the software SPREADgl to do phylogeographic analysis.

### The usage of this script is :

`python extract_dates_location.py input_df_name_path output_dates_df_name_path output_locations_df_name_path output_df_coords_path`

  *input_df_name_path* : The path and name of the input metadata (**Note that the header need to be *"Accession ID"* for the sample, *"date"* for the tip dates and *"Geo_loc"* for the locations**)
  
  *output_dates_df_name_path* : The path and name of the output file that contain all the tip dates corresponding to the sample
  
  *output_locations_df_name_path* : The path and name of the output file that contain all the locations corresponding to the sample
  
  *output_df_coords_path* : The path and name of the output file that contain all the locations and geographical coordinates corresponding to the sample for phylogeographic analysis

- `launch_all.sh` : This script allow us to launch all the script in one command line. 

### The usage of this script is :
Put all the path in the corresponding variables (if needed refer to previous explanation about all the scripts)

  
