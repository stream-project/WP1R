# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:26:16 2022

@author: GuptaR
"""



import time
import pandas as pd
import pickle
from nomad.client import ArchiveQuery
from nomad.metainfo import units
import numpy as np
import urllib.parse
import validators
import os
import re
import requests

from nomad.client import ArchiveQuery
from nomad.metainfo import units


from nomad import client, config
# config.client.url = 'http://nomad-lab.eu/prod/rae/api'
# results = client.query_archive(query={
#     'upload_id': ['5TM3DMqGTtKtP5qfQ7havg'],
#     'calc_id': ['pieH9n6qoVbsOnH7bTdjtPeVo6QM']})
# print(results)


import logging
from rdflib import Graph


results = ArchiveQuery(
    # url='http://nomad-lab.eu/prod/rae/beta/api',
  
    required={
        'section_run': '*',
        'section_workflow': '*',
        'section_metadata': '*'
            },
    max=None)

print(results)


# un = [] 
if os.path.isfile('un.txt'):
    pass
else:
    with open('un.txt', "wb") as fp:   
        un=[]
        pickle.dump(un, fp)
    
with open('un.txt', "rb") as fp:
    v = pickle.load(fp)

un = v
# print(un)
number = 100
length = len(un) + number
print(length)
total = 0



for i, result in enumerate(results):
    if i not in un:
        un.append(i)
        
    
        if i <length:
            metadata = result.section_metadata
            
            if metadata != None:        
                for attn, valuen in (metadata.__dict__.items()): 
                    if attn.startswith(('calc_id')):
                        
                        
                        pid_name = getattr(metadata,'calc_id')
                        print(pid_name)
                        
                        with open('un.txt', "wb") as fp:   
                            pickle.dump(un, fp)
                        
                        headers = {
                                'Content-Type': 'text/turtle',
                            }
                        
                        params = {
                                'format': 'turtle',
                            }
                        
                        
                            
                        # data = g.serialize(format='turtle').decode('UTF-8')
                        response = requests.get('https://nomad-lab.eu/prod/rae/dcat/datasets/'+str(pid_name), headers=headers,params=params)
                        # print(response.content)
                        g1 = response.content
                        g = Graph()
                        g.parse(g1)
                      
                        g.serialize('dcat'+str(i)+'.ttl',format='turtle')
                        
                          
                        # headers1 = {
                        #       'Content-Type': 'application/x-turtle',
                        #       }
                 
                        # # # data = g.serialize(format='turtle').decode('UTF-8') data=open('metadata_v1_' + str(i) + '.ttl','r').read()
                        # response = requests.post('http://localhost:7200/repositories/test/statements', data=open('rdf' + str(i) + '.ttl','r').read(), headers=headers1)
                        # print('graphdb')
                        # print(response)
                        
        else:
            break
                        
                        
                
                        
                        