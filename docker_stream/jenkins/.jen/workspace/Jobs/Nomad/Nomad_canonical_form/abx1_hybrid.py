# -*- coding: utf-8 -*-


import os 
import sys

from pathlib import Path

from rdflib import Graph
from rdflib.compare import to_isomorphic, graph_diff, similar


import re



####### Nomad data here


t =[]
with open('result.txt') as f:
    for line in f:
        line = line.strip('\n')
        t.append(line)

#print(t)





t1 = []
for i1 in t:
    # print(i2)
    # i1 = i1.split(',')[0]
    # print(i3)
    i1 = re.sub("[^A-Za-z0-9]", '', i1)
#    print(i1)


    i1= re.sub( r"([A-Z])", r" \1", i1).split()

#    print(i1)

    i1 = sorted(i1)

    i1 = ''.join(i1)


#    print(i1)
    # break
    
    t1.append(i1)

#print(t1)
#print(type(t1[0]))



######  Hybrid data here

t2 =[]
with open('query_hybrid.txt') as f:

    for line in f:
        string = (line.split('matvoc-core/')[-1])  
        # print(string)
            
        if "%" in string:
            # print('true')
            
            
            index = string.index("%")
            # print(index)
            while index+2 < len(string):
                string = string[:index] + string[index+3:]
                try:
                    index = string.index("%")
                except ValueError:
                    break
            
            
    
            t2.append(string)
        else:
            t2.append(string)
            
       
#print(t2)


t3 = []
for i2 in t2:
    # print(i2)
    i3 = i2.split(',')[0]
    # print(i3)
    i3 = re.sub("[^A-Za-z0-9]", '', i3)
   # print(i3)


    i3= re.sub( r"([A-Z])", r" \1", i3).split()

    print(i3)
    

    i3 = sorted(i3)
    

    i3 = ''.join(i3)


    #print(i3)
    # break
    
    t3.append(i3)

#print(t3)
#print(type(t3[0]))
#print(len(set(t3)))

def common_formula(a,b):   
    a_set = set(a)
    b_set = set(b)
     
    # print(a_set)
    # print(b_set)
    # check length
    if len(a_set.intersection(b_set)) > 0:
        return(a_set.intersection(b_set)) 
    else:
        return("no common formula's")




print("finding common formula's")


a7 = list(common_formula(t1,t3))

#print((a7))



t4 = []

t6 = []


for i6 in t2:
    # print(i6)
# print(i2)
    i10 = i6.split(',')[0]
    # print(i3)
    i10 = re.sub("[^A-Za-z0-9]", '', i10)
    # print(i6)


    i10= re.sub( r"([A-Z])", r" \1", i10).split()

    # print(i6)
    

    i10 = sorted(i10)
    
    i10 = ''.join(i10)
    
    if i10 in a7:
        print(i6)
        # i6.replace('\n','')
        t6.append(i6.replace('\n',''))
        
common_hybrid = (list(set(t6)))  

print('common_formulas')
print(common_hybrid)
        

with open("result_hybrid_common.txt", "w") as f:
    for item in common_hybrid:
        f.write(str(item) + "\n")    
        
        








    
#     t3.append(i3)

# print(t3)
# print(type(t3[0]))




















            







