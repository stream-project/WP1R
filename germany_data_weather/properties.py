# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:50:13 2021

@author: GuptaR
"""





import pandas as pd

filename = r'C:\Users\GuptaR\Desktop\test_all\station_values_1.csv'

values = pd.read_csv(filename)



''' Calculating length of distinct parameters '''
dist = values['parameter'].unique()
dist = dist.tolist()
# print(dist)
len(dist)


station_id = values['station_id'].unique()
station_id = station_id.tolist()
print(len(station_id))

''' creating rdf graphs '''
import rdflib
import requests
import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SKOS, RDF, RDFS, OWL, DC, DCTERMS, VOID, DOAP #most common namespaces
# import urllib.parse #for parsing strings to URI's


'''Initializing Graph'''

g = Graph()


# assigning namespaces and binding 

sosa = Namespace('http://www.w3.org/ns/sosa/')
ssn = Namespace('http://www.w3.org/ns/ssn/')
time = Namespace('http://www.w3.org/2006/time#')
qudt = Namespace('http://qudt.org/1.1/schema/qudt#')
qudt_unit= Namespace('http://qudt.org/1.1/vocab/unit#')
cdt = Namespace('http://w3id.org/lindt/custom_datatypes#')
geo = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
base = Namespace('http://example.org/data/')




g.bind('sosa', sosa)
g.bind('ssn', ssn)
g.bind('time', time)
g.bind('qudt', qudt)
g.bind('qudt_unit', qudt_unit)
g.bind('cdt', cdt)
g.bind('geo', geo)
g.bind('base', base)



''' creating rdf's using ssn ontology'''


## defining properties

c = ["daily maximum of wind gust in m/s","daily mean of wind velocity m/s","daily precipitation height in mm",
      "precipitation form is between [0,9]","daily sunshine duration in hours","daily snow depth in cm","daily mean of cloud cover",
      "daily mean of vapor pressure in hpa","daily mean of pressure in hpa","daily mean of temperature in Degree Celcius",
      "daily mean of relative humidity in percentage","daily maximum of temperature at 2m height in Degree Celcius",
      "daily minimum of temperature at 2m height in Degree Celcius","daily minimum of air temperature at 5cm above ground in Degree Celcius"]



for i in range(0,len(dist)):
    sam = dist[i]
    g.add((URIRef(base+sam), RDF.type ,URIRef(sosa+'ObservableProperty')))
    g.add((URIRef(base+sam), RDF.type ,URIRef(ssn+'Property')))
    g.add((URIRef(base+sam), RDFS.label ,Literal(c[i],lang='en')))
    
g.serialize(r'C:\Users\GuptaR\Desktop\repo_all\properties.ttl', format='turtle')
    
    


