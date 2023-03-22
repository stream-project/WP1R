# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:17:05 2022

@author: GuptaR
"""



from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys



# __file__ = 'rdf.py'


''' query1 '''







from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper("http://graphdb:7200/repositories/DSMS_test")

sparql.setQuery("""
 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX emmo: <http://emmo.info/emmo#>
PREFIX mech:	<http://emmo.info/emmo/domain/mechanical-testing#>

construct {
    ?material_name_instance emmo:EMMO_23b579e1_8088_45b5_9975_064014026c42 ?material_name.
    
}

where 
{ 
	?material_name_instance rdf:type mech:EMMO_71200c24_44fe_4533_96be_55ecb299681c; 	# Material name instance is of Type ShortName
              emmo:EMMO_23b579e1_8088_45b5_9975_064014026c42 ?material_name.			# Material name instance hasSymbolDate Material name

} 

""")


results = sparql.queryAndConvert()
print(results.serialize('./actual_results/query1.ttl'))














