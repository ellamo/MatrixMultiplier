# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:11:29 2019

@author: moorem24
"""


# A x B --- number of **columns of A** must be the same as number of **rows of B**
# if mA_columns != mB_rows --- error
mA_rows = 2
mA_columns = 3

mB_rows = 3
mB_columns = 2

mA = [ [0, 3, 5], 
       [5, 5, 2] 
     ]
mB = [ [3, 4],
       [3, -2], 
       [4, -2] 
     ]


# initialize resulting matrix to zeros
mC = []
for i in (0, mA_rows - 1):
    mC.append([])
    for j in (0, mB_columns - 1):
        mC[i].append(0)

print(mC)



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



# prints the resulting matrix
for r in mC:
    for c in r:
        print(c, end = " ")
    print()
