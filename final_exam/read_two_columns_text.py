"""
Read two columns of data from a text file.
"""

__author__ = 'Cristian Marquez'

import numpy as np

def read_two_column_text(file_name):
    try:
        data = open(file_name, 'r')
    except OSError as e:
        print("Error opening file:", e)
        return None

    data_contents = data.readlines()
    data.close()
    data_list_one = []
    data_list_two = []
    for line in data_contents:
        columns = line.split()
        if len(columns) != 2:
            print("Error: Line does not contain two columns:", line)
            continue
        try:
            column_one = float(columns[0])
            column_two = float(columns[1])
            data_list_one.append(column_one)
            data_list_two.append(column_two)
        except ValueError:
            print("Error: Failed to convert columns to float:", line)
            continue

    data_array = np.array([data_list_one, data_list_two])
    return data_array
