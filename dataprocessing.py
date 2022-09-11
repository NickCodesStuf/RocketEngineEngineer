from sympy import *



def calclsd(x):
    #find the largest trailing zero/number
    #put all the digits in a list
    digits = []
    for i in x:
        digits.append(i)
    #Reverse to bring trailing zeros to the front
    digits.reverse()
    #find the first non zero degit
    lsd = 0
    while digits[lsd] == '0':
        lsd+=1
    dindex = 0
    if '.' in digits:
        dindex = digits.index('.')
    #least significant degit is difference
    #LSD is digits after the decimal place negative is smaller and positive is larger than
    return(lsd-dindex)

def fixlsd(x, lsd):
    # put all the digits in a list
    digits = []
    for i in x:
        digits.append(i)
    #if lsd > 0 the decimal is -1

def sigfig(operators):
    lsdlist = []
    print(operators)
    for i in operators:
        lsdlist.append(calclsd(str(i)))
    #align to largest significant digit

