import csv
from tempcalc import *
import re

def csvtoarray(file):
    array = []
    with open(file, 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            temparray = []
            if row[0] != '':
                for i in row:
                    temparray.append(i)
                array.append(temparray)
    return array

def objectbuilder(listlib):
    #determine type of variable
    for i in listlib:
        #build classes
        #i is the name of the lib
        objectlist = []
        if i == 'products':
            for s in listlib[i]:
                #s is species of thing
                objectlist.append(Product(s[0], s[1], s[2], []))
            listlib[i] = objectlist
            #for future reference a object looks like this with s as the name
            # listlib['products'][s].name
        #build Objects
        if i == 'shomate':
            #exececutes for every shomate in list
            for s in listlib[i]:
                #s is specific shomate equation
                #find modifying function
                name = s[0]
                s.pop(0)
                index = ''
                for m, v in enumerate(listlib['products']):
                    #m is modified equation and v is value
                    if name == v.name:
                        index = m
                        listlib['products'][m].shomate+=[s]
                # print(index)
                # print(str(listlib[i].index(s))+'-->'+str(s))
    return listlib



def datagenerator(array):
    #definitions is a 2 dimentional array in a dictionary
    # definitions[key] = [[data1], [data2]]
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
                if re.search('[a-zA-Z]', e):
                    templist.append(e)
                elif e == '':
                    templist.append(e)
                else:
                    templist.append(float(e))
            definitions[classname] += [templist]

    # append to classes
    return(objectbuilder(definitions))
