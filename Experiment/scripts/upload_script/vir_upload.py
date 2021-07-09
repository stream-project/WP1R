# -*- coding: utf-8 -*-


# import libraries

import requests
import time
from requests.auth import HTTPBasicAuth


def insert_by_put(rdf, endpoint_url,username,passwd):
    r = requests.put(endpoint_url,
            data=rdf,
            auth=HTTPBasicAuth(username, passwd),
            headers = {'Content-Type': 'text/turtle'}
           

        )
    print(r)

''' inserting dataset1 (person dataset)'''    

start = time.time()


insert_by_put(open(r'C:\Users\GuptaR\Desktop\sparql\person.ttl').read(),'http://localhost:8890/DAV/person','dba','rohit') 

end = time.time()

print('time taken to upload :', end -   start)

''' inserting dataset2 (relation between person and company)'''    

start = time.time()


insert_by_put(open(r'C:\Users\GuptaR\Desktop\sparql\relation.ttl').read(),'http://localhost:8890/DAV/com_ids','dba','rohit') 

end = time.time()

print('time taken to upload :', end -   start)

''' inserting dataset3 (company dataset) '''    

start = time.time()


insert_by_put(open(r'C:\Users\GuptaR\Desktop\sparql\company.ttl').read(),'http://localhost:8890/DAV/company','dba','rohit') 
# insert_by_put(open('book1.ttl').read(),'http://localhost:8890/sparql','dba','rohit') 

end = time.time()

print('time taken to upload :', end -   start)

''' inserting dataset4 (combined all dataset)'''    

start = time.time()


insert_by_put(open(r'C:\Users\GuptaR\Desktop\sparql\relation and company dataset.ttl').read(),'http://localhost:8890/DAV/two_data','dba','rohit') 

end = time.time()

print('time taken to upload :', end -   start)

