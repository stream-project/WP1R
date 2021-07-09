# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV

import requests
import time

#### importing data into repositories


'''insering data intp repo1'''
start = time.time()

headers = {
    'Content-Type': 'application/x-turtle',
}

data = open(r'C:\Users\GuptaR\Desktop\sparql\person.ttl')


response = requests.post('http://localhost:7200/repositories/repo1/statements', data=data, headers = headers)

print(response)

end = time.time()

print('time taken to upload :', end -   start)


''' inserting data into repo2 '''


start = time.time()


headers = {
    'Content-Type': 'application/x-turtle',
}

data = open(r'C:\Users\GuptaR\Desktop\sparql\relation.ttl')


response = requests.post('http://localhost:7200/repositories/repo2/statements', data=data, headers = headers)

print(response)

end = time.time()
print('time taken to upload :', end -   start)


''' inserting data into repo3 '''
start = time.time()


headers = {
    'Content-Type': 'application/x-turtle',
}

data = open(r'C:\Users\GuptaR\Desktop\sparql\company.ttl')


response = requests.post('http://localhost:7200/repositories/repo3/statements', data=data, headers = headers)

print(response)
end = time.time()
print('time taken to upload :', end -   start)



''' inserting data into repo4 '''
start = time.time()


headers = {
    'Content-Type': 'application/x-turtle',
}



response = requests.post('http://localhost:7200/repositories/repo4/statements', data=open(r'C:\Users\GuptaR\Desktop\sparql\company_relation.ttl','r').read(), headers = headers)

print(response)
end = time.time()
print('time taken to upload :', end -   start)





























    
    
    
    
    