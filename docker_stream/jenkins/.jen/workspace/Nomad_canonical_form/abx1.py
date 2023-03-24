# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:08:38 2023

@author: GuptaR
"""




import os 
import sys
from pathlib import Path
from rdflib import Graph
from rdflib.compare import to_isomorphic, graph_diff, similar
import re

####### Nomad data here

t =[]

with open('query_nomad.txt') as f:
    for line in f:
        line = line.strip('\n')
        t.append(line)

formulas = []
for i in t:
    i1 = (i.split('matvoc-core/')[-1])  
    formulas.append(i1)
    
#print(formulas)
#print(len(formulas))




list1 = ['Ge','Sn','Pb']
list2 = ['F3','Cl3','Br3','I3']
B = []
X = []
A=[]
ABX = []
A2 = []
X2 = []
B2=[]
for i2 in formulas:
    # print(i2)
    i3 = i2.split(',')[0]
    i3 = re.sub("[^A-Za-z0-9]", '', i3)



    i3= re.sub( r"([A-Z])", r" \1", i3).split()

    # print(i3)
    # break
    
    
    for i in i3:
        if i in list1:
            B.append(i)
        if i in list2:
            X.append(i)
        
    BX = B + X
    # print(BX)
    # break
    X2.append(X[0])
    B2.append(B[0])
    A = (list((set(i3)-set(BX))))
    
    A = sorted(A)
    A1 = ''.join(A)
    
    A2.append(A1)
    # print(A)
    C = A + B + X
    # A1.append(A)
    print(A)
    C1 = ''.join(C)
    ABX.append(C1)
    B = []
    X = []
    A = []
    # C = []
    
#print((ABX))


#print(len(set(ABX)))
    
#print((A2))

O_atoms = ((set(A2)))
      



g = sorted(O_atoms)
#print(g)

#print(len(B2))
#print(len(X2))
#print(X2)




result = []
result1 = []

for i in O_atoms:
    for j in list1:
        for k in list2:
            result.append((str(i)+str(j)+ str(k)))
            result1.append((i,j,k))

#print((result))




with open("result.txt", "w") as f:
    for item in result:
        f.write(str(item) + "\n")




            







