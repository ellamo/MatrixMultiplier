# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 21:36:00 2019

@author: moorem24
"""
import sys

# variables
mA_array = []
mB_array = []
mAxB_array = []
mA = {'name': "left matrix", 'rows': 0, 'columns': 0, 'matrix': mA_array}
mB = {'name': "right matrix", 'rows': 0, 'columns': 0, 'matrix': mB_array}
mAxB = {'name': "resulting matrix", 'rows': 0, 'columns': 0, 'matrix': mAxB_array}



class Error(Exception):
    '''Base class for other exceptions'''
    pass

class ValueTooSmallError(Error):
    '''Raised if input value is too small'''
    pass

class SizeMismatch(Error):
    '''Raised if number of columns in A is not the same as the number of rows in B'''
    pass


def checkNum(dimension):
    if dimension <= 0:
        raise ValueTooSmallError

        
def printMatrix(m):
    print("\n", m['name'], " is ", m['rows'], " by ", m['columns'])
    if not m['matrix']:
        print("[]")
    else: 
        for r in m['matrix']:
            for c in r:
                print(c, end = " ")
            print()

''' this doesn't work and i'm not sure why '''
#def initMatrix(mAxB):
#    for i in range(0, mAxB['rows'] - 1, 1):
#        mAxB['matrix'].append([])
#        for j in range(0, mAxB['columns'] - 1, 1):
#            mAxB['matrix'][i].append(0)
#            print("i = ", i, " j = ", j, "matrix = ", mAxB['matrix'])


def initMatrix(r, c):
    mC = []
    for i in (0, r - 1):
        mC.append([])
        for j in (0, c - 1):
            mC[i].append(0)
#    print(mC)
    return(mC)


# Get user input of rows and columns of matrix
def getSizes(a, b):
    loop = True
    while loop:
        try:
            a['rows'] = int(input("number of rows of first matrix?"))
            checkNum(a['rows'])
            a['columns'] = int(input("number of columns of first matrix?"))
            checkNum(a['columns'])
            b['rows'] = int(input("number of rows of second matrix?"))
            checkNum(b['rows'])
            b['columns'] = int(input("number of columns of first matrix?"))
            checkNum(b['columns'])
            
            # check that sizes are compatible
            if a['columns'] != b['rows']:
                raise SizeMismatch
            
            # set resulting matrix sizes
            mAxB['rows'] = mA['rows']
            mAxB['columns'] = mB['columns']
            
            # print matrices
#            printMatrix(mA)
#            printMatrix(mB)
#            printMatrix(mAxB)
            
            # break
            loop = False
        
        except ValueError:
            print("Could not convert data to an integer.  Input whole numbers")
            
        except ValueTooSmallError:
            print("the number you entered is too small.  numbers must be greater than 0")
       
        except SizeMismatch:
            print("the first matrix must have the same number of columns as rows of the second matrix")
 
    
def getMatrixData(m):
    for i in range(0, m['rows'], 1):
        m['matrix'].append([])
        for j in range(0, m['columns'], 1):
            loop = True
            while loop:
                try:
                    print(m['name'], " row ", i + 1, " column ", j + 1, end = " ")
                    value = int(input("input number: "))
                    m['matrix'][i].append(value)
                    print("i = ", i, " j = ", j, " ", m['matrix'])
                    loop = False
                except ValueError:
                    print("Could not convert data to an integer.  Input whole numbers\n")
                    

def multiply(mA, mB, mAxB):
    for rA in range(0, mA['rows'], 1):
        for cB in range(0, mB['columns'], 1):
            for cA in range(0, mA['columns'], 1):
                mAxB['matrix'][rA][cB] += (mA['matrix'][rA][cA] * mB['matrix'][cA][cB]) 
    

    
    
'''    
# loop through to do the multiplication
for rA in range(0, mA_rows, 1):             #mA_rows - 1
#    print("rA = ", rA)
    for cB in range(0, mB_columns, 1):         #mB_columns - 1
#        print("cB = ", cB)
        for cA in range (0, mA_columns, 1):          #mA_columns -1
#            print("cA = ", cA)
#            print("mC[", rA, "][", cB, "] = ", mC[rA][cB] )
#            print("mA[", rA, "][", cA, "] = ", mA[rA][cA] )
#            print("mB[", cA, "][", cB, "] = ", mB[cA][cB] )
            mC[rA][cB] = mC[rA][cB] + (mA[rA][cA] * mB[cA][cB])
#            print(mC)
'''    
    
    
    
    
def main():
    getSizes(mA, mB)
    mAxB['matrix'] = initMatrix(mAxB['rows'], mAxB['columns'])
#    initMatrix(mAxB)       '''Doesn't work'''    
    printMatrix(mAxB)
    
    getMatrixData(mA)
    getMatrixData(mB)
    printMatrix(mA)
    printMatrix(mB)
    
    multiply(mA, mB, mAxB)
    printMatrix(mAxB)


main()
    
print("\nfinal line reached")