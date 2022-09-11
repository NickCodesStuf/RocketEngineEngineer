from tempcalc import *
from csvreader import *

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def tempcalc():
    # Given
    # C2H5OH + 3O2 -> 3H20 + 2CO2
    Water = Product("H20", 3, 300, [[-203.6060, 1523.290, -3196.413, 2474.455, 3.855326, 298, 500], [30.09200, 6.832514, 6.793435, -2.534480, 0.082139, 500, 1700], [41.96426, 8.622053, -1.499780, 0.098119, -11.15764, 1700, 6000]])
    CarbonDioxide = Product("CO2", 2, 300, [[24.99735, 24.99735, -33.69137, 7.948387, -0.136638, 298, 1200], [58.16639, 2.720074, -0.492289, 0.038844, -6.447293, 1200, 6000]])
    substances = [Water, CarbonDioxide]
    Heatdistrobution(substances, 1366910)
    print(Water.temperature)
    # Solution

if __name__ == '__main__':
    objectbuilder(csvtoarray('testdata.csv'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
