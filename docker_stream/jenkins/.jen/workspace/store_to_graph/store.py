# -*- coding: utf-8 -*-



import requests


files = {
    'config': open('repo-config.ttl', 'rb'),
}

response = requests.post('http://graphdb:7200/rest/repositories',  files=files)

print(response)


import time

#### importing data into repositories


'''insering data into repo diaspora'''
# start = time.time()


import os
import natsort
from pathlib import Path

p_list = ['Nomad_metadata','Nomad_method','Nomad_observation','Nomad_dcat']

for p in p_list:

    path = '../'+ str(p)
    
    print(path)
    
    dirs = os.listdir(path)
    dirs = natsort.natsorted(dirs)
    
    # print(dirs)
    
    start = time.time()
    
    for i_path in dirs:
        a = (os.path.join(path,i_path))
        # print(a)
        suff = (Path(a).suffixes)
        # print(type(suff))
        
        
        if suff[0] == '.ttl':
            print(a)
    
            # headers = {
            #     'Content-Type': 'text/plain',
            # }
            
            headers = {
                    'Content-Type': 'application/x-turtle',
                }
                
            
            rdf = open(a,'r',encoding='utf-8').read()
            
            
            # response = requests.post('http://localhost:7200/repositories/observation/statements', data=rdf.encode('utf-8'), headers = headers)
           
            # data = open(r'C:\Users\GuptaR\Desktop\rml_rdf\SDM-RDFizer\exam\output\sam.nt').read()
        
        
            response = requests.post('http://graphdb:7200/repositories/Nomad/statements', data=rdf.encode('utf-8'), headers = headers)
        
            print(response)
    
    end = time.time()
    
    print('time taken to upload triples :', end -   start)
      
