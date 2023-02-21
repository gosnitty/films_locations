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

def distance(file, latitude, longtitude):
    '''
    this function returns list with distance between coordinates
    '''
    distance_film = []
    for i, elem in enumerate(file):
        longt = file[i][-1]
        lat = file[i][-2]
        latitude, longtitude, longt, lat = map(radians, [latitude, longtitude, longt, lat])
        lon_n = longt - longtitude
        lat_n = lat - latitude
        distance_n = 2* asin(sqrt(sin(lat_n/2)**2 + cos(latitude)\
        * cos(lat) * sin(lon_n/2)**2))*6371
        distance_film.append([distance_n,file[i]])
    return sorted(distance_film)[:10]


def filling_map(points, latitude, longtitude):
    '''
    this function returns the map with points of place where films where made
    '''
    films_map = folium.Map()
    point_chosed = folium.FeatureGroup(name = 'Choosed point')
    films_chossed = folium.FeatureGroup(name = 'Films')
    films_map = folium.Map(tiles="Stamen Terrain",
                    location=[latitude, longtitude],
                    zoom_start=1)
    point_chosed.add_child(folium.CircleMarker(location=[latitude, longtitude],
                        popup = 'Chossed point',
                        radius=10,
                        fill_color='purple'))
    films_map.add_child(point_chosed)
    for i, elem in enumerate(points):
        films_chossed.add_child(folium.Marker(location = points[i][1][1:],
                                popup = points[i][1][0],
                                icon=folium.Icon('purple')))
    films_map.add_child(films_chossed)

    films_map.add_child(folium.LayerControl())
    films_map.save("Films_map.html")
    return films_map

def main():
    """
    This function uses arparse to get arguments from command line
    """
    parser = argparse.ArgumentParser(description="changes strings")
    parser.add_argument("year", type=str, help= "to make file shorter")
    parser.add_argument("path", type=str, help= "path to file")
    parser.add_argument("longtitude", type=float, help= "coordinates")
    parser.add_argument("latitude", type=float, help= "coordinates")

    args = parser.parse_args()
    print(filling_map(distance(coordinates(right_year(args.path,args.year))\
    ,args.latitude, args.longtitude), args.latitude, args.longtitude))

if __name__ == 'main':
    main()
