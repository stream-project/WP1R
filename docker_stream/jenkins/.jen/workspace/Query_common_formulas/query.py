# -*- coding: utf-8 -*-


from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib import URIRef
import csv



sparql = SPARQLWrapper("http://graphdb:7200//repositories/Nomad_hybrid")


sparql.setQuery("""

PREFIX matvoc:	<http://stream-ontology.com/matvoc-core/>
PREFIX sosa: <http://www.w3.org/ns/sosa/>
PREFIX nomad: <http://https://nomad-coe.eu/ontology#>
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/>

PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

select  ?sample ?calc_id ?id_hybrid

where 

{
         ?id_nomad a sosa:FeatureOfInterest;
                  
         sosa:hasSample ?sample.
    
    ?sample  a sosa:Sample;
         nomad:has_calc_id ?calc_id;
         matvoc:has_canonical_form ?form.
         
    
        SERVICE <http://localhost:7200//repositories/Hybrid3>{    
        ?id_hybrid sosa:hasSample ?system_h.
    # ?system_h matvoc:has_canonical_form ?form.
    
    }
 
    filter(?form=matvoc:CH6NSnBr3)
}



""")
results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query = sparql.query().convert()
print((results_query))


# extract the headers dynamically
headers = results_query["results"]["bindings"][0].keys()


# print(headers)


# open a new CSV file and write the headers
with open('fed_query.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)

    # write the results row by row
    for result in results_query["results"]["bindings"]:
        row = [result.get(header, {}).get("value", "") for header in headers]
        writer.writerow(row)
    
results_list = []
for result in results_query["results"]["bindings"]:
    row_dict = {}
    for header in headers:
        row_dict[header] = result.get(header, {}).get("value", "")
    results_list.append(row_dict)

df = pd.DataFrame(results_list)

pd.set_option('display.max_columns', None)



print(df)

