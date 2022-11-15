# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:34:52 2022

@author: GuptaR
"""

# -*- coding: utf-8 -*-

# import libraries

from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd


''' query1 '''

start = time.time()


sparql = SPARQLWrapper("http://graphdb:7200/repositories/Hybrid3")


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




CONSTRUCT {
    ?id sosa:hasSample ?system.
          ?system hybrid3:has_formula ?formula.
            
}

 where{
    
   ?id a sosa:FeatureOfInterest;
         sosa:hasSample ?system.
    
         ?system a sosa:Sample;
               hybrid3:has_formula ?formula.
            
    
    

}

""")

results = sparql.queryAndConvert()
print(results.serialize('./actual_results/query2.ttl'))


# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query1 = sparql.query().convert()


# end = time.time()

# print('time taken to execute the query',end -   start)



# ''' storing results locally '''
# query1=[]
# for result in results_query1["results"]["bindings"]:
    # query1.append((result["triples"]["value"]))
    # with open('query1.txt', 'w') as f:
        # for s in query1:
            # f.write(str(s)+'\n')
    

    
# ''' query2 '''

# start = time.time()


# sparql = SPARQLWrapper("http://localhost:7200/repositories/Hybrid")


# # sparql.setMethod(POST)

 
# sparql.setQuery("""
# PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
# PREFIX matonto: <http://matonto.org/ontology/matonto#> 
# PREFIX owl: <http://www.w3.org/2002/07/owl#> 
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# PREFIX ssn: <http://www.w3.org/ns/ssn/> 
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
# PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 


# SELECT ?id ?system ?compound_name ?group ?formula ?organic ?inorganic ?last_update ?description ?iupac

# where{
    
#   ?id a sosa:FeatureOfInterest;
#         sosa:hasSample ?system.
    
#         ?system a sosa:Sample;
#             hybrid3:has_compound_name ?compound_name;
#               hybrid3:has_group ?group;
#               hybrid3:has_formula ?formula;
#               hybrid3:has_organic ?organic;
#               hybrid3:has_inorganic ?inorganic;
#               hybrid3:has_last_update ?last_update;
#               hybrid3:has_iupac ?iupac.
#     optional {?system hybrid3:has_description ?description. }
    
    

# }
# """)

# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query2 = sparql.query().convert()


# end = time.time()

# print('time taken to execute the query',end -   start)



# ''' storing results locally '''
# query2=[]
# for result in results_query2["results"]["bindings"]:
#     try:
        
#         query2.append((result["id"]["value"],result["system"]["value"],result['compound_name']['value'],result['group']['value'],result['formula']['value'],result['organic']['value'],result['inorganic']['value'],result['iupac']['value'],result['last_update']['value'],result['description']['value']))
#         with open('query2.txt', 'w') as f:
#             for s in query2:
#                 f.write(str(s)[1:-1]+'\n')
#     except:
#         pass
    
#     finally:
        
         
#         query2.append((result["id"]["value"],result["system"]["value"],result['compound_name']['value'],result['group']['value'],result['formula']['value'],result['organic']['value'],result['inorganic']['value'],result['iupac']['value'],result['last_update']['value']))
#         with open('query2.txt', 'w') as f:
#             for s in query2:
#                 f.write(str(s)[1:-1]+'\n')
        
# ''' query3'''

# start = time.time()


# sparql = SPARQLWrapper("http://localhost:7200/repositories/Hybrid")


# # sparql.setMethod(POST)

 
# sparql.setQuery("""
# PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
# PREFIX matonto: <http://matonto.org/ontology/matonto#> 
# PREFIX owl: <http://www.w3.org/2002/07/owl#> 
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# PREFIX ssn: <http://www.w3.org/ns/ssn/> 
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
# PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 


# SELECT ?system ?experiment ?method ?computation ?theory_level ?k_point_grid

# where{
    
#   ?id a sosa:FeatureOfInterest;
#         sosa:hasSample ?system;
       
#         optional {?id hybrid3:has_experimental ?experiment.
    
#         ?experiment a sosa:Procedure;
#                 hybrid3:has_method ?method.
#     }
    
#     optional {?id hybrid3:has_computational ?computation.
#     ?computation a sosa:Procedure;
#                   hybrid3:has_level_of_theory ?theory_level;
#                   hybrid3:has_k_point_grid ?k_point_grid.
    
#     }
    

# }
# """)

# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query3 = sparql.query().convert()


# end = time.time()

# print('time taken to execute the query',end -   start)



# ''' storing results locally '''
# query3=[]
# for result in results_query3["results"]["bindings"]:
#     try:
        
#         query3.append((result["system"]["value"],result["experiment"]["value"],result["method"]["value"],result["computation"]["value"],result["theory_level"]["value"],result["k_point_grid"]["value"]))
#         with open('query3.txt', 'w') as f:
#             for s in query3:
#                 f.write(str(s)+'\n')
#     except:
#         query3.append((result["system"]["value"]))
#         with open('query3.txt', 'w') as f:
#             for s in query3:
#                 f.write(str(s)+'\n')
        
# ''' query4'''

# start = time.time()


# sparql = SPARQLWrapper("http://localhost:7200/repositories/Hybrid")


# sparql.setMethod(POST)

 
# sparql.setQuery("""
# PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
# PREFIX matonto: <http://matonto.org/ontology/matonto#> 
# PREFIX owl: <http://www.w3.org/2002/07/owl#> 
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# PREFIX ssn: <http://www.w3.org/ns/ssn/> 
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
# PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
# PREFIX foaf: <http://xmlns.com/foaf/0.1/> 



# SELECT ?id ?system ?reference ?author ?first ?last ?institution

# where{
    
  # ?id a sosa:FeatureOfInterest;
        # hybrid3:has_reference ?reference;
        # sosa:hasSample ?system.
    
        # ?reference a hybrid3:Reference;
                # hybrid3:has_author ?author.
    
    # ?author a foaf:Person;
            # hybrid3:has_first_name ?first;
            # hybrid3:has_last_name ?last;
            # hybrid3:has_institution ?institution.
    

# }
 
# """)

# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query4 = sparql.query().convert()


# end = time.time()

# print('time taken to execute the query',end -   start)



# ''' storing results locally '''
# query4=[]
# for result in results_query4["results"]["bindings"]:
    # query4.append((result['id']['value'],result['system']['value'],result['reference']['value'],result['author']['value'],result['first']['value'],result['last']['value'],result['institution']['value']))
    # with open('query4.txt', 'w') as f:
        # for s in query4:
            # f.write(str(s)[1:-1]+'\n')
    
# ''' query5'''

# start = time.time()


# sparql = SPARQLWrapper("http://localhost:7200/repositories/Hybrid")


# # sparql.setMethod(POST)

 
# sparql.setQuery("""
# PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
# PREFIX matonto: <http://matonto.org/ontology/matonto#> 
# PREFIX owl: <http://www.w3.org/2002/07/owl#> 
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# PREFIX ssn: <http://www.w3.org/ns/ssn/> 
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
# PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
# PREFIX foaf: <http://xmlns.com/foaf/0.1/> 


# SELECT ?id ?system ?p_name ?s_name

# where{
    
#   ?id a sosa:FeatureOfInterest;
#         sosa:hasSample ?system;
       
#         optional {?id hybrid3:has_observed_primary_property ?primary_prop.
    
#         ?primary_prop a ssn:Property;
#                 hybrid3:has_name ?p_name.
#     }
    
#     optional {?id hybrid3:has_observed_secondary_property ?secondary_prop.
#     ?secondary_prop a ssn:Property;
#                   hybrid3:has_name ?s_name.
    
#     }
    
# }

 
# """)

# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query5 = sparql.query().convert()


# end = time.time()

# print('time taken to execute the query',end -   start)



# ''' storing results locally '''
# query5=[]
# for result in results_query5["results"]["bindings"]:
#     try:
        
#         query5.append((results['id']['value'],results['system ']['value'],results['p_name']['value'],results['s_name']['value']))
#         with open('query5.txt', 'w') as f:
#             for s in query5:
#                 f.write(str(s)[1:-1]+'\n')
#     except:
         
#         query5.append((results['id']['value'],results['system ']['value']))
#         with open('query5.txt', 'w') as f:
#             for s in query5:
#                 f.write(str(s)[1:-1]+'\n')
        
            
            
    
# ''' query6'''

# start = time.time()


# sparql = SPARQLWrapper("http://localhost:7200/repositories/Hybrid")


# # sparql.setMethod(POST)

 
# sparql.setQuery("""
 # PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
 # PREFIX matonto: <http://matonto.org/ontology/matonto#> 
 # PREFIX owl: <http://www.w3.org/2002/07/owl#> 
 # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
 # PREFIX sosa: <http://www.w3.org/ns/sosa/> 
 # PREFIX ssn: <http://www.w3.org/ns/ssn/> 
 # PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
 # PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
 # PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
 # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
 # PREFIX matvoc: <http://stream-ontology.com/matvoc#>


 # SELECT ?sample ?observation ?result ?value_id ?value ?qualifier

 # where{
    
   # <http://example.com/ns/365>  a sosa:FeatureOfInterest;
        # sosa:hasSample ?sample;
        # sosa:hasObservation ?observation.
    
    # ?observation a sosa:Observation;
                 # sosa:hasfeatureOfInterest <http://example.com/ns/365>;
                 # sosa:hasResult ?result.
    
    # ?result a sosa:Result;
            # matvoc:hasValue ?value_id.
    
    # ?value_id a matvoc:Multi_series_value;
              # hybrid3:has_observed_value ?value;
              # hybrid3:has_qualifier ?qualifier.
    
                 
       
    
# }

 
# """)

# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query6 = sparql.query().convert()


# end = time.time()

# print('time taken to execute the query',end -   start)



# ''' storing results locally '''
# query6=[]
# for result in results_query6["results"]["bindings"]:
    
    # query6.append((result['sample']['value'],result['observation']['value'],result['result']['value'],result['value_id']['value'],result['value']['value'],result['qualifier']['value']))
    # with open('query6.txt', 'w') as f:
        # for s in query6:
            # f.write(str(s)[1:-1]+'\n')
        




    
        


