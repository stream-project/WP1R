# -*- coding: utf-8 -*-

# import libraries

from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd


''' query1 '''

start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo1")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT (count(?s) as ?triples)
WHERE
{
 ?s a ab:Person;
   ?p ?o.
}
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query1 = sparql.query().convert()


end = time.time()

print('time taken to execute the query',end -   start)



''' storing results locally '''
query1=[]
for result in results_query1["results"]["bindings"]:
    query1.append(result["triples"]["value"])
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query1.txt', 'w') as f:
    for s in query1:
        f.write(str(s)+'\n')   



    
''' query2 '''

start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo1")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT ?first ?last
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query2 = sparql.query().convert()



end = time.time()

print('time taken to execute the query',end -   start)


''' storing results locally '''
query2=[]
for result in results_query2["results"]["bindings"]:
    query2.append((result["first"]["value"],result["last"]["value"]))
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query2.txt', 'w') as f:
    for s in query2:
        f.write(str(s)[1:-1]+'\n')    
       
        
        

'''query3'''


start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo1")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT ?last ?first ?c
WHERE
{
  ?s a ab:Person.  
  ?s ab:firstname ?first ;
     ab:lastname ?last . 
  
    SERVICE <http://localhost:7200/repositories/repo2> {
        ?s ab:employedat d:8254. 
        
    }
    SERVICE <http://localhost:7200/repositories/repo3> {
         d:8254 a ab:Company.
         d:8254 ab:hasname ?c. 
        }
}
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query3 = sparql.query().convert()



end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''
query3=[]
for result in results_query3["results"]["bindings"]:
    query3.append((result["first"]["value"],result["last"]["value"],result["c"]["value"]))
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query3.txt', 'w') as f:
    for s in query3:
        f.write(str(s)[1:-1] +'\n')

    
'''query4'''


start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo1")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 


SELECT (count(?c) as ?total_companies)

where{

SELECT DISTINCT ?c 

WHERE
{ 
        SERVICE <http://localhost:7200/repositories/repo2>{
  
            ?s ab:employedat ?c.}
        
}}
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query4 = sparql.query().convert()

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''
query4=[]
for result in results_query4["results"]["bindings"]:
    query4.append((result["total_companies"]["value"]))
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query4.txt', 'w') as f:
    for s in query4:
        f.write(str(s)+'\n')

    
'''query5'''


start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo2")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT DISTINCT ?c_id ?c_name ?c_emp

WHERE{

      
  
            ?s ab:employedat ?c_id.
    
        SERVICE  <http://localhost:7200/repositories/repo3>{
        ?c_id a ab:Company.
         ?c_id ab:hasname ?c_name;
               ab:hasempnumber ?c_emp.
 
            
        }
        
}
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query5 = sparql.query().convert()

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''
query5=[]
for result in results_query5["results"]["bindings"]:
    query5.append((result["c_id"]["value"],result["c_name"]["value"],result["c_emp"]["value"]))
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query5.txt', 'w') as f:
    for s in query5:
        f.write(str(s)[1:-1] +'\n')
    
     
'''query6'''


start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo1")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT (count(distinct concat(str(?first), str(?last))) as ?unique)
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query6 = sparql.query().convert()

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''
query6=[]
for result in results_query6["results"]["bindings"]:
    query6.append((result["unique"]["value"]))
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query6.txt', 'w') as f:
    for s in query6:
        f.write(str(s) +'\n')    
    
'''query7'''


start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo1")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
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
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query7 = sparql.query().convert()

end = time.time()

print('time taken to execute the query',end -   start)

'''storing results locally'''
query7=[]
for result in results_query7["results"]["bindings"]:
    query7.append((result["first"]["value"],result["last"]["value"],result["unique"]["value"]))
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query7.txt', 'w') as f:
    for s in query7:
        f.write(str(s)[1:-1] +'\n')    

    
'''query8'''


start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo1")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT    ?first ?last ?c_name

WHERE
{     
   
        ?s ab:firstname ?first;
            ab:lastname ?last.
    
    
        SERVICE <http://localhost:7200/repositories/repo2>{
  
            ?s ab:employedat ?c_id.}
    
        SERVICE  <http://localhost:7200/repositories/repo3>{
         ?c_id ab:hasname ?c_name.
               
 
            
        }
        
    }
LIMIT 500
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query8 = sparql.query().convert()

end = time.time()



print('time taken to execute the query',end -   start)  

'''storing results locally'''
query8=[]
for result in results_query8["results"]["bindings"]:
    query8.append((result["first"]["value"],result["last"]["value"],result["c_name"]["value"]))
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query8.txt', 'w') as f:
    for s in query8:
        f.write(str(s)[1:-1] +'\n')     
    
'''query9'''


start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/repo1")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
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
""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query9 = sparql.query().convert()

end = time.time()


print('time taken to execute the query',end -   start)  

'''storing results locally'''
query9=[]
for result in results_query9["results"]["bindings"]:
    query9.append((result["unique"]["value"]))
with open(r'C:\Users\GuptaR\Desktop\results\graphdb\query9.txt', 'w') as f:
    for s in query9:
        f.write(str(s) +'\n')     

        


