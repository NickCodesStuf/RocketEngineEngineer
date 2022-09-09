from sympy import *
import numpy as np

#these 2 objects will be used later when have the free time to implement Phase 1
#The calculation is pretty ez to do on paper or if you are an especially lazy dumbfuck just google enthalpy of combustion
# class Reactant:
#     def __init__(self, name, molarmass, state, formationheat):
#         self.name = name #Name of the species
#         self.molarmass = molarmass #atomic mass in g/mol
#         self.formationheat = formationheat #Enthalpy of formation in kJ/mol
# class Combustion:
#     def __init__(self, reactants, products):
#         self.reactants = reactants
#         self. products = products

class Product:
    def __init__(self, name, mols, temperature, shomate):
        self.name = name #Chemical formula
        self.mols = mols #The Moles produced in a reactuion
        self.temperature = temperature #the temperature of the substance in k
        #Get this from the NIST database, and for best results get all your other data there as well
        self.shomate = shomate #The shomate equation variables in a list of ascending order [[a, b, c, d, e, mintememp, maxtemp],(...)]

def Shomate(species, equation, a, b):
    #This function will Integrate shomate equation from a to b
    #Set up the shomate equation
    # Reset shomate value
    shomate = "0"
    # Populate the shomate equation
    shomate += "+(" + str(equation[0]) + ") "
    shomate += "+(" + str(equation[1]) + ")*(x/1000) "
    shomate += "+(" + str(equation[2]) + ")*(x/1000)**2 "
    shomate += "+(" + str(equation[3]) + ")*(x/1000)**3 "
    shomate += "+(" + str(equation[4]) + ")*(x/1000)**(-2) "
    # Integrate and export value
    x = symbols("x")
    energy = integrate(shomate, (x, a, b)) * species.mols
    #My physics teacher is dissapointed, No sig figs???
    #For now I repent and promise to add a sig fig function later
    print("changing temperatures between " + str(equation[5]) + " : " + str(equation[6]) + " energy is " + str(energy))
    return(energy)

def Heatdistrobution(products, energy):
    #This Dictionary keeps track of the partition we are in
    #Since the key is the product object, the active partition in a for loop can be called with loadedpart[i]
    loadedpart = {}

    #Calc.1
    print("calc1")
    # integrate to unify temperatures
    testtemp = []
    # determine largest starting temperature
    for i in products:
        testtemp.append(i.temperature)
    # integrate shomate to the lowest temperature to get to a starting point
    # loop through every shomate under mintemp
    for i in products:
        s = 0
        tempcount = 0
        # Consolodate shomate
        while tempcount < max(testtemp):
            #Integrate the partition and subtract it from energy
            energy -= Shomate(i, i.shomate[s], i.shomate[s][5], i.shomate[s][6])
            #sets tempcount new mintemp and cycles partitions
            tempcount = i.shomate[s][6]
            s += 1
            #Breaks loop if tempcount
        #adds back excess and update the loaded partition for the object
        #-1 self esteem
        energy += Shomate(i, i.shomate[s-1], max(testtemp), i.shomate[s-1][6])
        loadedpart[i] = s-1


    #Calc.2
    print("calc2 -------------------------------------------------")
    #lowerbound is equilibrium
    lowerbound = max(testtemp)

    #Loop will either break at if statement or with lack of data error (I prob should of done that with calc 1)
    while true:
        denergy = 0
        #the actual upper bound of the subpartition is min(upperbounds)
        upperbounds = []
        #find the upperbound from the smallest loaded partition
        #This doubles to mark the object whose partition we later update
        try:
            for i in loadedpart:
                upperbounds.append(i.shomate[loadedpart[i]][6])
                #updates smallest value
                if min(upperbounds) == i.shomate[loadedpart[i]][6]:
                    aloaded = i
        except:
            #This exception will occur if data isnt valid or if not eno
            print(str(energy) + " > 0 and out of data")
            break
        #Update the partition
        #Integrate across entire subpartition and remove energy
        for i in products:
            denergy += Shomate(i, i.shomate[loadedpart[i]], lowerbound, min(upperbounds))
        if denergy > energy:
            break
        #otherwise remove energy, reset, and repeat with new subpartition
        energy-=denergy
        lowerbound = min(upperbounds)
        #here we cycle to the next partion for the reactant marked as "aloaded"
        loadedpart[aloaded] += 1

    #Calc 3.





#Given
#C2H5OH + 3O2 -> 3H20 + 2CO2
Water = Product("H20", 1 , 300,[[-203.6060,1523.290,-3196.413,2474.455,3.855326,298,500],[30.09200, 6.832514, 6.793435, -2.534480, 0.082139, 500, 1700]])
substances = [Water]


#Unknown
#Equations
#C6H12O6+
#Substitution
print(Shomate(substances[0], substances[0].shomate[0], 298, 500))
print(Shomate(substances[0], substances[0].shomate[1], substances[0].shomate[1][5], substances[0].shomate[1][6]))
print("Heat Distro ----------------------------------------------------")
Heatdistrobution(substances, 17000)
#Solution
