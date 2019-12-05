import csv
import pandas as pd
import numpy

def regular2gcoords():
    gcoords = []
    with open('seaports.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            coords = row['Lat/Long']
            split_coords = coords.split('/')
            lat_coord = split_coords[0]
            long_coord = split_coords[1]
            split_lat = lat_coord.split(' ') 
            split_long = long_coord.split(' ')
            print(split_lat)
            latitude = 0
            longitude = 0            
            if len(split_lat) == 3:
                lat_degree_str = split_lat[0][0:-1]
                lat_degree = int(lat_degree_str)
                lat_min = 0
                lat_sec = 0
                if split_lat[1] == 'S':
                    lat_degree = -lat_degree
                latitude = round(lat_degree + lat_min + lat_sec, 8)
            elif len(split_lat) == 4:
                lat_degree_str = split_lat[0][0:-1]
                lat_min_str = split_lat[1][0:-1]
                lat_degree = int(lat_degree_str)
                lat_min = int(lat_min_str)/60
                lat_sec = 0
                if split_lat[2] == 'S':
                    lat_degree = -lat_degree
                latitude = round(lat_degree + lat_min + lat_sec, 8)
            else:
                lat_degree_str = split_lat[0][0:-1]
                lat_min_str = split_lat[1][0:-1]
                lat_sec_str = split_lat[2][0:-1]
                lat_degree = int(lat_degree_str)
                lat_min = int(lat_min_str)/60
                lat_sec = int(lat_sec_str)/3600
                if split_lat[3] == 'S':
                    lat_degree = -lat_degree
                latitude = round(lat_degree + lat_min + lat_sec, 8)

            if len(split_long) == 3:
                long_degree_str = split_long[1][0:-1]
                long_degree = int(long_degree_str)
                long_min = 0
                long_sec = 0
                if split_long[2] == 'W':
                    long_degree = -long_degree
                longitude = round(long_degree + long_min + long_sec, 8)
            elif len(split_long) == 4:
                long_degree_str = split_long[1][0:-1]
                long_min_str = split_long[2][0:-1]
                long_degree = int(long_degree_str)
                long_min = int(long_min_str)/60
                long_sec = 0
                if split_long[3] == 'W':
                    long_degree = -long_degree
                longitude = round(long_degree + long_min + long_sec, 8)
            else:
                long_degree_str = split_long[1][0:-1]
                long_min_str = split_long[2][0:-1]
                long_sec_str = split_long[3][0:-1]
                long_degree = int(long_degree_str)
                long_min = int(long_min_str)/60
                long_sec = int(long_sec_str)/3600
                if split_long[4] == 'W':
                    long_degree = -long_degree
                longitude = round(long_degree + long_min + long_sec, 8)

            coordinates_str = str(latitude) + ", " + str(longitude)
            gcoords.append(coordinates_str)
    return gcoords

csv_reader = csv.DictReader(open('seaports1.csv', mode='r'))

def update_csv():
    gcodes = regular2gcoords()
    data = pd.read_csv("seaports1.csv")
    data['Google coordinates'] = gcodes
    print(data.head())
    data.to_csv(r'/home/medo-bills/DataScience/pdf-extract/gc.csv')


update_csv()