# -*- coding: utf-8 -*-



import requests


files = {
    'config': open('repo-config.ttl', 'rb'),
}

response = requests.post('http://graphdb:7200/rest/repositories',  files=files)

print(response)


import requests
import time

#### importing data into repositories


'''insering data into repo hybrid'''
# start = time.time()


import os
import natsort
from pathlib import Path

path = '../Hybrid_rdf_map/SDM-RDFizer/exam/output'

dirs = os.listdir(path)
dirs = natsort.natsorted(dirs)

# print(dirs)

start = time.time()

for i_path in dirs:
    a = (os.path.join(path,i_path))
    # print(a)
    suff = (Path(a).suffixes)
    
    
    if suff[0] == '.nt':
        print(a)

        headers = {
            'Content-Type': 'text/plain',
        }
        
        rdf = open(a,'r',encoding='utf-8').read()
        
        
        # response = requests.post('http://localhost:7200/repositories/observation/statements', data=rdf.encode('utf-8'), headers = headers)
       
        # data = open(r'C:\Users\GuptaR\Desktop\rml_rdf\SDM-RDFizer\exam\output\sam.nt').read()
    
    
        response = requests.post('http://graphdb:7200/repositories/Hybrid3/statements', data=rdf.encode('utf-8'), headers = headers)
    
        print(response)

end = time.time()

print('time taken to upload triples :', end -   start)
  




















    
    
    
    
    