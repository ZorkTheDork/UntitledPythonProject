import pandas as pd
import json
import os.path as path

def read_excel(filename, sort_by):
    if path.isfile(filename):
        excel_in = pd.read_excel(filename)
        data_dict = excel_in.to_dict(sort_by)
        return data_dict
    return -1

def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def overwrite_json(filename, data_dict):
    with open(filename, 'w') as outfile:
        json.dump(data_dict, outfile)