def right_year(path, year):
    '''
    this function returns list with films of certain year
    '''
    file = [i for i in read_file(path) for j in i if year in j ]
    return file

