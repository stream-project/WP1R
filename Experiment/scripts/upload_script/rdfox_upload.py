# -*- coding: utf-8 -*-

# import libraries
import requests
import time


# helper function to raise exception if the REST endpoint returns an
# unexpected status code
def assert_reponse_ok(response, message):
    if not response.ok:
        raise Exception(
            message + "\nStatus received={}\n{}".format(response.status_code, response.text))

rdfox_server = "http://localhost:12110"


# List data stores
response = requests.get(rdfox_server + "/datastores")
assert_reponse_ok(response, "Failed to obtain list of datastores")
print("== Data store list ==")
print(response.text)


## importing turtle data into repo1

start = time.time()


turtle_data = r'C:\Users\GuptaR\Desktop\sparql\person.ttl'


headers = {
  'Content-type': 'text/turtle',
}


response = requests.post(
    rdfox_server + "/datastores/repo1/content", headers = headers, data=open(turtle_data,'r',encoding='utf-8').read())
assert_reponse_ok(response, "Failed to add facts to data store.")

end = time.time()

print('time taken to upload :', end -   start)


## importing turtle data into repo2

start = time.time()


turtle_data = r'C:\Users\GuptaR\Desktop\sparql\relation.ttl'


headers = {
  'Content-type': 'text/turtle',
}


response = requests.post(
    rdfox_server + "/datastores/repo2/content", headers = headers, data=open(turtle_data,'r',encoding='utf-8').read())
assert_reponse_ok(response, "Failed to add facts to data store.")

end = time.time()

print('time taken to upload :', end -   start)

## importing turtle data into repo3

start = time.time()


turtle_data = r'C:\Users\GuptaR\Desktop\sparql\company.ttl'


headers = {
  'Content-type': 'text/turtle',
}


response = requests.post(
    rdfox_server + "/datastores/repo3/content", headers = headers, data=open(turtle_data,'r',encoding='utf-8').read())
assert_reponse_ok(response, "Failed to add facts to data store.")

end = time.time()

print('time taken to upload :', end -   start)


## importing turtle data into repo4 

start = time.time()


turtle_data = r'C:\Users\GuptaR\Desktop\sparql\company_relation.ttl'


headers = {
  'Content-type': 'text/turtle',
}


response = requests.post(
    rdfox_server + "/datastores/two_repo/content", headers = headers, data=open(turtle_data,'r',encoding='utf-8').read())
assert_reponse_ok(response, "Failed to add facts to data store.")

end = time.time()

print('time taken to upload :', end -   start)





