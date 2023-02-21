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

