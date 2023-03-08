# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:30:52 2023

@author: GuptaR
"""


# -*- coding: utf-8 -*-




from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib import URIRef

import re




# original_form

t =[]
with open('result_hybrid_common.txt') as f:
    for line in f:
        line = line.strip('\n')
        t.append(line)

# print(t)


## querying the id's



from SPARQLWrapper import SPARQLWrapper, POST
import requests
import requests
import random

def insert(subject, predicate, object, graphdb_endpoint):
    # Construct the SPARQL query with placeholders for the subject, predicate, and object
    query = """
    PREFIX matvoc:<http://stream-ontology.com/matvoc-core/> 
    PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/>
    INSERT DATA {
      hybrid3:%s matvoc:%s matvoc:%s .
    }
    """


    # Replace the placeholders in the SPARQL query with the random values and the provided predicate
    query_with_random_values = query % (subject, predicate, object)

    # Send the SPARQL query to the GraphDB server using the HTTP POST method
    response = requests.post(graphdb_endpoint, data={"update": query_with_random_values})
    
    print(response)
    print(response.content)

# insert("system_4", "has_canonical_form", "NH4SnI3", "http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/try/statements")



sparql = SPARQLWrapper("http://graphdb:7200//repositories/Hybrid3")
   


def formula(form):

    query_template = '''
    
        
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
        PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
        PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX bacdive: <http://kg.bacdive.dsmz.de/>
        PREFIX qudt: <http://qudt.org/2.1/schema/qudt#> 
        PREFIX matvoc:	<http://stream-ontology.com/matvoc-core/>
        PREFIX nomad: <http://https://nomad-coe.eu/ontology#> 
        PREFIX sosa: <http://www.w3.org/ns/sosa/> 
        PREFIX hybrid3:<https://materials.hybrid3.duke.edu/materials/> 
        
        select ?subject
        
        where
        
        {{
            
            ?subject a sosa:Sample;
                  hybrid3:has_formula <{object}>.
                               
            
        
                                                                       
        }}
        
    '''
    query = query_template.format(object=form)
    
    # create a SPARQLWrapper object and set the query and endpoint URL
    # sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    
    # set the query format and execute the query
    sparql.setReturnFormat(JSON)
    results_query1 = sparql.query().convert()
    # print('rohit')
    # print(t)
    form1 = form.split('matvoc-core/')[-1]
    print(form1)
    for result in results_query1["results"]["bindings"]:
        material_id = result["subject"]["value"]
        # print(material_id)
        m = material_id
        print(m)
        m = (material_id.split('materials/')[-1])
        print(m)
    
        # m1 = 'system' + '_' + m
        # # print(type(m1))
            
       
        insert(m, "has_canonical_form", form1,"http://graphdb:7200/repositories/Hybrid3/statements")
            
                



for x in (t):
    # print(x,y)
    # print(x)
    matvoc = 'http://stream-ontology.com/matvoc-core'
    form = matvoc+'/'+x
    # print(form)
    formula(form)







# ''' query2a '''


# from SPARQLWrapper import SPARQLWrapper, POST, DIGEST



# sparql = SPARQLWrapper("http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/Hybrid3")



# sparql.setHTTPAuth(DIGEST)
# # sparql.setCredentials("login", "password")
# sparql.setMethod(POST)
# sparql.setQuery("""

# # PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
# # PREFIX matonto: <http://matonto.org/ontology/matonto#> 
# # PREFIX owl: <http://www.w3.org/2002/07/owl#> 
# # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# # PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# # PREFIX ssn: <http://www.w3.org/ns/ssn/> 
# # PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# # PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
# # PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
# # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
# # PREFIX matvoc:	<http://stream-ontology.com/matvoc-core/>




# import requests

# headers = {
#     'Content-Type': 'application/sparql-update',
# }

# data = "PREFIX hybrid3:<https://materials.hybrid3.duke.edu/materials/> PREFIX matvoc:<http://stream-ontology.com/matvoc-core/> INSERT DATA { <https://materials.hybrid3.duke.edu/materials/system/113> hybrid3:has_canonical_formula matvoc:NH4SnI3.\
# <https://materials.hybrid3.duke.edu/materials/system/188> hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
#     <https://materials.hybrid3.duke.edu/materials/system/41> hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
#                 <https://materials.hybrid3.duke.edu/materials/system/105> hybrid3:has_canonical_formula matvoc:C3H10NGeI3.\
#             <https://materials.hybrid3.duke.edu/materials/system/106> hybrid3:has_canonical_formula matvoc:C3H10NGeI3.\
#                 <https://materials.hybrid3.duke.edu/materials/system/333> hybrid3:has_canonical_formula matvoc:C3N2H5SnI3\
#                     <https://materials.hybrid3.duke.edu/materials/system/79> hybrid3:has_canonical_formula matvoc:CH5N2GeI3.\
#                         <https://materials.hybrid3.duke.edu/materials/system/39> hybrid3:has_canonical_formula matvoc:CH5N2PbI3.\
#                             <https://materials.hybrid3.duke.edu/materials/system/94> hybrid3:has_canonical_formula matvoc:C2H7N2GeI3.\
#                                 <https://materials.hybrid3.duke.edu/materials/system/191> hybrid3:has_canonical_formula matvoc:CH6NSnBr3.\
#                                     <https://materials.hybrid3.duke.edu/materials/system/348> hybrid3:has_canonical_formula matvoc:C3H8Br3NPb.\
#             <https://materials.hybrid3.duke.edu/materials/system/402> hybrid3:has_canonical_formula matvoc:C3H8Br3NPb.\
#       <https://materials.hybrid3.duke.edu/materials/system/95> hybrid3:has_canonical_formula matvoc:CH6N3GeI3.\
#           <https://materials.hybrid3.duke.edu/materials/system/362> hybrid3:has_canonical_formula matvoc:CH6NPbBr3.\
#     <https://materials.hybrid3.duke.edu/materials/system/190> hybrid3:has_canonical_formula matvoc:CH6NSnCl3.\
#         <https://materials.hybrid3.duke.edu/materials/system/184> hybrid3:has_canonical_formula matvoc:C2H8NPbI3.\
#     <https://materials.hybrid3.duke.edu/materials/system/1> hybrid3:has_canonical_formula matvoc:CH6NPbCl3.\
#       <https://materials.hybrid3.duke.edu/materials/system/44> hybrid3:has_canonical_formula matvoc:CH5N2SnI3.}"

# response = requests.post('http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/Hybrid3/statements', 
#                          headers=headers, data=data)


# print(response)





            
            


