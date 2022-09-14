from tempcalc import *
from csvreader import *
from dataprocessing import *

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    objectsdictionary = datagenerator(csvtoarray('testdata.csv'))
    products = []
    for i in objectsdictionary['products']:
         products.append(i)
         print(i.name)
         print(i.shomate)
    Heatdistrobution(products, 500)
    print(products[0].temperature)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
