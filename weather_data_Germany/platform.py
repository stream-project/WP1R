# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:48:17 2021

@author: GuptaR
"""

import pandas as pd

filename = r'C:\Users\GuptaR\Desktop\repo_all\station_values_1.csv'

values = pd.read_csv(filename)


file_station = r'C:\Users\GuptaR\Desktop\repo_all\station_details_v.csv'
stations = pd.read_csv(file_station)


''' Calculating length of distinct parameters '''
dist = values['parameter'].unique()
dist = dist.tolist()
# print(dist)
len(dist)

station_id = values['station_id'].unique()
station_id = station_id.tolist()
print(station_id)
print(len(station_id))



height = stations['height']
height = height.tolist()
height[0]
len(height)

latitude = stations['latitude']
latitude = latitude.tolist()
len(latitude)


longitude = stations['longitude']
longitude = longitude.tolist()
len(longitude)

names = stations['name']
names = names.tolist()
len(names)

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
qudt = Namespace('http://qudt.org/2.1/schema/qudt#')
qudt_unit= Namespace('http://qudt.org/2.1/vocab/unit#')
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




# defining Platform 

for i in range(0,len(station_id)):
    y = BNode()
    g.add((URIRef(base+str(station_id[i])), RDF.type , URIRef(sosa+'Platform')))
    g.add((URIRef(base+str(station_id[i])), RDFS.label , Literal("station in " + names[i],lang='en')))
    g.add((URIRef(base+str(station_id[i])), URIRef(geo+'alt'), y))
    g.add((y, RDF.type , URIRef(qudt+'quantityValue')))
    g.add((y, URIRef(qudt+'numericValue') , Literal(str(height[i]),datatype=XSD.double)))
    g.add((y, URIRef(qudt+'unit') , URIRef(qudt_unit+'M')))    
#    g.add((URIRef(base+str(station_id[i])), URIRef(geo+'alt') , Literal(str(height[i])+ ' meters',datatype=cdt.ucum)))
    g.add((URIRef(base+str(station_id[i])), URIRef(geo+'lat') , Literal(latitude[i])))
    g.add((URIRef(base+str(station_id[i])), URIRef(geo+'lon') , Literal(longitude[i])))
    for j in range(0,len(dist)):
        sensor = dist[j]+'_' + 'sensor'

        g.add((URIRef(base+str(station_id[i])), URIRef(sosa+'hosts'), URIRef(base+sensor)))

# g.serialize(r'C:\Users\GuptaR\Desktop\repos\repo2.ttl', format='turtle')

# defining sensor

for j in range(0,len(station_id)):

    for i in range(0,len(dist)):
        
        sensor = dist[i]+'_' + 'sensor'
    
        g.add((URIRef(base+sensor), RDF.type , URIRef(sosa+'Sensor')))
        g.add((URIRef(base+sensor), RDFS.label , Literal("sensor for measuring " + dist[i],lang='en')))
        # g.add((URIRef(base+sensor), URIRef(sosa+'isHostedBy'), (URIRef(base+str(station_id[j])))))
        g.add((URIRef(base+sensor), URIRef(sosa+'observes'), (URIRef(base+dist[i]))))
    
    
g.serialize(r'C:\Users\GuptaR\Desktop\repo_all\platform2.ttl', format='turtle')




