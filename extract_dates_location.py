'''

Script to extract the dates, the location, and the coordinates of the countries from metadata

'''

import argparse
import pandas as pd
from geopy.geocoders import Nominatim


# Definition of the arguments we need to execute the script
argument_to_use = argparse.ArgumentParser()
argument_to_use.add_argument("input_df", type=str,
                             help="The path to the file that contain the metadata")
argument_to_use.add_argument("output_dates", type=str,
                             help="The path and the name of the output file that contain the dates of the samples")
argument_to_use.add_argument("output_location", type=str,
                             help="The path and the name of the output file that contain the countries of the samples")
argument_to_use.add_argument("output_coords", type=str,
                             help="The path and the name of the output file that contain the coordinates of the differents countries")

# Extraction of the input arguments
args = argument_to_use.parse_args()
df_to_use  = pd.read_table(args.input_df, sep="\t")
output_dates = args.output_dates
output_location = args.output_location
output_coords = args.output_coords

def write_df_dates_only():
    '''Function to write the output file with the accession id and dates only'''
    with open(output_dates, "w") as file:
        file.write(df_to_use[["Accession ID", "date"]].to_csv(index=False, 
                                                              header=False, 
                                                              sep="\t"))
        


# Filter the dataset with only Geo_loc and accession ID
def write_df_geo_loc_only():
    '''Function to write the output file with the accession id and the country'''
    with open(output_location, "w") as file:
        file.write(df_to_use[["Accession ID", "Geo_loc"]].to_csv(index=False, 
                                                                 header=False,
                                                                 sep="\t"))

# Useful constants to extract coords
geolocator = Nominatim(user_agent="Nicolas")
df_with_location = set(df_to_use["Geo_loc"])
dict_of_loc = dict.fromkeys(df_with_location)

def get_coords():
    '''Function to write the output file with the coords and the country of interest'''
    for loc in df_with_location:
        location = geolocator.geocode(loc)
        coord = location.latitude, location.longitude
        dict_of_loc[loc] = coord
    
    df_transposed = pd.DataFrame(dict_of_loc).T.reset_index()
    df_transposed.columns = ['location', 'latitude', 'longitude']
    with open(output_coords, 'w') as file:
        file.write(df_transposed.to_csv(index=False, sep=","))

# dict_of_loc ={'Nauru': (-0.5252306, 166.9324426), 'Brazil': (-10.3333333, -53.2), 'India': (22.3511148, 78.6677428)}



if __name__ == "__main__":
    get_coords()
    write_df_dates_only()
    write_df_geo_loc_only()
    







