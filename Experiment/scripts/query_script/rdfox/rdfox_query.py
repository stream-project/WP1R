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


''' query1 '''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#>
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT (COUNT(*) as ?Triples) where {?s a ab:Person; ?p ?o.}'''
query1 = requests.get(
    rdfox_server + "/datastores/repo1/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")
# print(query1.text)

end = time.time()

print('time taken to execute the query',end -   start)
'''storing results locally'''
file = open(r"C:\Users\GuptaR\Desktop\results\rdfox\query1.txt","w")
file.write(query1.text)
file.close()

# print(results)  


'''query2'''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT ?first ?last
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}
'''
query2 = requests.get(
    rdfox_server + "/datastores/repo1/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''

file = open(r"C:\Users\GuptaR\Desktop\results\rdfox\query2.txt","w")
file.write(query2.text)
file.close()


'''query4'''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 


SELECT (count(?c) as ?total_companies)

where{

SELECT DISTINCT ?c 

WHERE
{ 
      
  
            ?s ab:employedat ?c.
        
}}

'''
query4 = requests.get(
    rdfox_server + "/datastores/repo2/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''

file = open(r"C:\Users\GuptaR\Desktop\results\rdfox\query4.txt","w")
file.write(query4.text)
file.close()


'''query6'''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT (count(distinct concat(str(?first), str(?last))) as ?unique)
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}
'''
query6 = requests.get(
    rdfox_server + "/datastores/repo1/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''
file = open(r"C:\Users\GuptaR\Desktop\results\rdfox\query6.txt","w")
file.write(query6.text)
file.close()



'''query7'''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT ?first ?last 
(count(concat(str(?first), str(?last))) as ?unique)
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}
group by ?first ?last

'''
query7 = requests.get(
    rdfox_server + "/datastores/repo2/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''

file = open(r"C:\Users\GuptaR\Desktop\results\rdfox\query7.txt","w")
file.write(query7.text)
file.close()


'''query9'''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

select (count(?s) as ?unique)
where{
SELECT  ?s ?first ?last
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}
}
'''
query9 = requests.get(
    rdfox_server + "/datastores/repo1/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''

file = open(r"C:\Users\GuptaR\Desktop\results\rdfox\query9.txt","w")
file.write(query9.text)
file.close()


