# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:51:53 2021

@author: GuptaR
"""


import pandas as pd
import pickle

filename = r'C:\Users\GuptaR\Desktop\repo_all\station_values_v2.csv'

values = pd.read_csv(filename)



''' Calculating length of distinct parameters '''
dist = values['parameter'].unique()
dist = dist.tolist()
# print(dist)
len(dist)

station_id = values['station_id'].unique()
station_id = station_id.tolist()
print((station_id))
len(station_id)

''' creating rdf graphs '''
import rdflib
import requests
import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SKOS, RDF, RDFS, OWL, DC, DCTERMS, VOID, DOAP #most common namespaces
# import urllib.parse #for parsing strings to URI's


'''Initializing Graph'''


## observations 

with open(r'C:\Users\GuptaR\Desktop\try\un.txt', "rb") as fp:
    v = pickle.load(fp)
    
gr=len(v)
print(gr)
for i in range(0,len(station_id)):
    
    count = 0

    
    print('done'+ str(i))
    print(count)


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
    
    
    
    c = ["daily maximum of wind gust in m/s","daily mean of wind velocity m/s","daily precipitation height in mm",
          "precipitation form is between [0,9]","daily sunshine duration in hours","daily snow depth in cm","daily mean of cloud cover measured as 1/8(Oktas)",
          "daily mean of vapor pressure in hpa","daily mean of pressure in hpa","daily mean of temperature in Degree Celcius",
          "daily mean of relative humidity in percentage","daily maximum of temperature at 2m height in Degree Celcius",
          "daily minimum of temperature at 2m height in Degree Celcius","daily minimum of air temperature at 5cm above ground in Degree Celcius"]
    
    units = ['M-PER-SEC', 'M-PER-SEC', 'MilliM','','HR', 'CentiM', '', 'HectoPA', 'HectoPA', 'DEG_C', 'PERCENT',
              'DEG_C', 'DEG_C', 'DEG_C']
        
    
    
    ''' creating rdf's using ssn ontology'''
    
    
    
    sam = 'sample'+str(station_id[i])
    
   
    
    for j in range(0,len(dist)):
        par = dist[j]
        sensor = dist[j]+'_' + 'sensor'
    

        # entry = 0
        # FileReader = pd.read_csv(r'C:\Users\GuptaR\Desktop\repos\weather_data.csv', chunksize=10000)  # the number of rows per chunk

        # for df in FileReader:
           
        for index,row in values.iterrows():
            
            y = BNode()
            y1= BNode()
            count+=1
            ob = str(count) + str(station_id[i])  +  par 
            if row['parameter'] == par:
                g.add((URIRef(base+ob), RDF.type, URIRef(sosa+'Observation')))
                g.add((URIRef(base+ob), RDFS.label, Literal(c[j],lang='en')))
                # g.add((URIRef(base+ob), URIRef(sosa+'observedProperty'), URIRef(base+par)))
                g.add((URIRef(base+ob), URIRef(sosa+'madeBySensor'), URIRef(base+sensor)))
                g.add((URIRef(base+ob), URIRef(sosa+'hasFeatureOfInterest'), URIRef(base+sam)))
                g.add((URIRef(base+ob), URIRef(sosa+'hasResult'), y))
                g.add((y, RDF.type , URIRef(qudt+'quantityValue')))
                g.add((y, URIRef(qudt+'numericValue') , Literal(row['value'],datatype=XSD.double)))
                g.add((y, URIRef(qudt+'unit') , URIRef(qudt_unit+units[j])))
                # g.add((URIRef(base+ob), URIRef(sosa+'hasSimpleResult'), Literal(row['value'],datatype= units[j])))
                g.add((URIRef(base+ob), URIRef(sosa+'resultTime'), y1))
                g.add((y1, RDF.type , URIRef(time+'Instant')))
                g.add((y1, URIRef(time+'inXSDDateTimeStamp') , Literal(row['date'],datatype=XSD.dateTimeStamp)))
                
   
    gr+=1
    print('saved')            
    g.serialize(r'C:\Users\GuptaR\Desktop\repo_all\repo'+str(gr)+'.ttl', format='turtle')



    print('enter_repo' + str(gr))
    
    headers = {
            'Content-Type': 'application/x-turtle',
        }
        
    # data = g.serialize(format='turtle').decode('UTF-8')
    response = requests.post('http://localhost:7200/repositories/observations/statements', data=open(r'C:\Users\GuptaR\Desktop\repo_all\repo'+str(gr)+'.ttl','r').read(), headers=headers)
    print(response)
    print('done_repo' + str(gr))
    print(count)


