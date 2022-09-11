import csv
from tempcalc import *

def csvtoarray(file):
    array = []
    with open(file, 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            temparray = []
            for i in row:
                temparray.append(i)
            array.append(temparray)
    return array

def objectbuilder(array):
    definitions = {}
    # i is index and x is data in array, I never knew I could do this!
    for i, x in enumerate(array):

        templist = []
        # Check if it is the end/start to new data
        if x[1] == '':
            # sets up datarange to read from
            classname = x[0]
            min = i+2
            definitions[classname] = []
        # append data to object
        elif i >= min:
            for e in x:
                templist.append(e)
            definitions[classname] += [templist]

    # append to classes
    objectlibrary = {}
    for i in definitions:
        # x is original product
        if i == 'products':
            objectlibrary['products'] = []
            for s in definitions[i]:
                objectlibrary['products']+=[Product(s[0], s[1], s[2], [])]
        print(objectlibrary)
        if i == 'shomate':
            # Anonymus variable where x is product object and s is new shomate equation
            #iterate for every shmate
            for s in definitions[i]:
                # find matching object
                name = s[0]
                for n, f in enumerate(objectlibrary['products']):
                    if f.name == name:
                        s.pop(0)
                        objectlibrary['products'][n].shomate+=[s]
                        #update shomate
                    continue