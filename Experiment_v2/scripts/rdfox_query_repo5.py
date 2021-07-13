# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:12:17 2021

@author: GuptaR
"""

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


## importing turtle data into repo5

start = time.time()


turtle_data = r'C:\Users\GuptaR\Desktop\sparql\all_repo.ttl'


headers = {
  'Content-type': 'text/turtle',
}


response = requests.post(
    rdfox_server + "/datastores/all_repo/content", headers = headers, data=open(turtle_data,'r',encoding='utf-8').read())
assert_reponse_ok(response, "Failed to add facts to data store.")

end = time.time()

print('time taken to upload :', end -   start)



'''querying database'''

''' query1 '''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

select ((?co+?com) as ?total_triples)
{
    {
        select (count(?s) AS ?co)
        { ?s a ab:Person ;
             ?o ?p.}
    } 
    {
        select (count(?d) AS ?com) 
        { ?d a ab:Company;
             ?w ?q.} 
     


    }

}'''
query1 = requests.get(
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")
# print(response.text)



end = time.time()

print('time taken to execute the query',end -   start)

# print(results)  

# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query1.txt","w")
file.write(response.text)
file.close()



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
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")


end = time.time()

print('time taken to execute the query',end -   start)

# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query2.txt","w")
file.write(response.text)
file.close()


'''query3'''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT ?last ?first ?c
WHERE
{
  ?s a ab:Person.  
  ?s ab:firstname ?first ;
     ab:lastname ?last . 
  

        ?s ab:employedat d:8254. 
        
    
    
         d:8254 a ab:Company.
         d:8254 ab:hasname ?c. 
        
}

'''
query3 = requests.get(
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")



end = time.time()

print('time taken to execute the query',end -   start)

# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query3.txt","w")
file.write(query3.text)
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
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")



end = time.time()

print('time taken to execute the query',end -   start)

# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query4.txt","w")
file.write(query4.text)
file.close()


'''query5'''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT DISTINCT ?c_id ?c_name ?c_emp

WHERE{

      
  
            ?s ab:employedat ?c_id.
    
       
        ?c_id a ab:Company.
         ?c_id ab:hasname ?c_name;
               ab:hasempnumber ?c_emp.
 
            
        
        
}

'''
query5 = requests.get(
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")


end = time.time()

print('time taken to execute the query',end -   start)

# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query5.txt","w")
file.write(query5.text)
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
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")


end = time.time()

print('time taken to execute the query',end -   start)

# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query6.txt","w")
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
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")



end = time.time()

print('time taken to execute the query',end -   start)

# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query7.txt","w")
file.write(query7.text)
file.close()

'''query8'''

start = time.time()


sparql_text = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT    ?first ?last ?c_name

WHERE
{     
   
        ?s ab:firstname ?first;
            ab:lastname ?last.
    
    
     
  
            ?s ab:employedat ?c_id.
    
     
         ?c_id ab:hasname ?c_name.
               
 
            
        
        
    }

'''
query8 = requests.get(
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")



end = time.time()

print('time taken to execute the query',end -   start)


# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query8.txt","w")
file.write(query8.text)
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
    rdfox_server + "/datastores/all_repo/sparql", params={"query": sparql_text})
assert_reponse_ok(response, "Failed to run select query.")
print("== Initial query result ==")



end = time.time()

print('time taken to execute the query',end -   start)

# saving file locally

file = open(r"C:\Users\GuptaR\Desktop\result1\rdfox\query9.txt","w")
file.write(query9.text)
file.close()















