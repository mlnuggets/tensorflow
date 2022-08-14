import json
import argparse
import os
from urllib.request import urlretrieve

# A Utility to prepare the Face-Dataset
# This script will download the images from the cloud via the links provided in the JSON file
# 
# Arguments: JSON File Path
# Returns: Folder called "assets" containing the images corresponding to the links
# 
# By Ango AI
output_folder = "assets"
parser = argparse.ArgumentParser(description='A Utility to fetch asset data')
parser.add_argument('-j','--json', type=str, default="Data.json" ,
                    help='The path to the JSON file containing asset URLs')

args = vars(parser.parse_args())
f = open(args['json'])
data = json.load(f)

if not os.path.exists('assets'):
    os.makedirs('assets')
asset_index = 0
out_file_name = ''
for datum in data:
    out_file_name = output_folder + "/" + datum['asset'].split('/')[-1]    
    urlretrieve(datum['asset'], out_file_name)
    if (asset_index % 10) == 0:
        print(f"Fetching {asset_index}th Asset and storing as {out_file_name} ")
    asset_index+=1
 

