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

# python3 films.py '1991' C:\\Users\\USER\\Desktop\\piton\\labu\\locations.list 49.817545 24.023932 
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
