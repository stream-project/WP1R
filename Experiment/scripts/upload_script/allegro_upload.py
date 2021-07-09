# -*- coding: utf-8 -*-

# import libraries

import os
import sys
from franz.openrdf.repository.repository import Repository
import requests
import time
from franz.openrdf.sail.allegrographserver import AllegroGraphServer
from franz.openrdf.connect import ag_connect
from franz.openrdf.rio.rdfformat import RDFFormat

# connecting to repositories

print("Connecting to AllegroGraph server --",
      "host:'%s' port:%s" % ('127.0.0.1', '10035'))
server = AllegroGraphServer('127.0.0.1', '10035',
                            'test', 'rohit')



print("Available catalogs:")
for cat_name in server.listCatalogs():
    if cat_name is None:
        print('  - <root catalog>')
    else:
        print('  - ' + str(cat_name))
        
        
catalog = server.openCatalog('')
print("Available repositories in catalog '%s':" % catalog.getName())
for repo_name in catalog.listRepositories():
    print('  - ' + repo_name)
    



#### Importing file to repo1

'''connection to repo1'''

conn = ag_connect('repo1', host='127.0.0.1', port='10035',
                user='test', password='rohit', create=True, clear=True) 

start = time.time()

conn.add(r'C:\Users\GuptaR\Desktop\sparql\person.ttl', base=None, format=RDFFormat.TURTLE, contexts=None)


end = time.time()

print('time taken to upload :', end -   start)

print('triples size (default graph): {count}'.format(count=conn.size()))


#### Importing file to repo2

'''connection to repo2'''

conn = ag_connect('repo2', host='127.0.0.1', port='10035',
                user='test', password='rohit', create=True, clear=True) 

start = time.time()

conn.add(r'C:\Users\GuptaR\Desktop\sparql\company_relation.ttl', base=None, format=RDFFormat.TURTLE, contexts=None)


end = time.time()

print('time taken to upload :', end -   start)

print('triples size (default graph): {count}'.format(count=conn.size()))












