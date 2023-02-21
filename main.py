'''
imports modules
'''
from math import radians, cos, sin, asin, sqrt
import argparse
from geopy.geocoders import Nominatim
import folium


def read_file(path):
    '''
    this function reads file
    '''
    file = open(path, 'r', encoding= 'UTF-8')
    file = file.read().strip().split('\n')
    file = [i.split('\t') for i in file]
    return file[10:]

def right_year(path, year):
    '''
    this function returns list with films of certain year
    '''
    file = [i for i in read_file(path) for j in i if year in j ]
    return file


def coordinates(file):
    '''
    this function returns list with coordinates where films where made
    '''
    locations, coordinat = '', []
    geolocator = Nominatim(user_agent= "films")
    for i, j in enumerate(file):
        if '(' in file[i][-1]:
            if file[i][-2].count(',') >2:
                file[i][-2] = ','.join(file[i][-2].split(',')[1:])
            locations = (geolocator.geocode(file[i][-2]))
        else:
            if file[i][-1].count(',') >2:
                file[i][-1] = ','.join(file[i][-1].split(',')[1:])
            locations= (geolocator.geocode(file[i][-1]))
        coordinat.append([file[i][0],locations.latitude,locations.longitude])
    return coordinat