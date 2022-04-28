# -*- coding: utf-8 -*-



# import libraries

from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd


''' query1 '''

start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/Hybrid")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
PREFIX matonto: <http://matonto.org/ontology/matonto#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT (count(*) as ?triples)

where{
  ?id a sosa:Sample;
      ?s1 ?o1.
    
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
    query1.append((result["triples"]["value"]))
    with open('query1.txt', 'w') as f:
        for s in query1:
            f.write(str(s)+'\n')
    
    
    
    


    
        


