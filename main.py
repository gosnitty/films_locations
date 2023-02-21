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
