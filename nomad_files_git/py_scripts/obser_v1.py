# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:32:05 2021

@author: GuptaR
"""


import time
import pandas as pd
import pickle
from nomad.client import ArchiveQuery
from nomad.metainfo import units
import numpy as np
import urllib.parse
import validators
import os

from nomad.client import ArchiveQuery
from nomad.metainfo import units


results = ArchiveQuery(
    # url='http://nomad-lab.eu/prod/rae/beta/api',
  
    required={
        'section_run': {
            'section_method': '*',
            'section_single_configuration_calculation': '*',
            'section_system': '*'},
        'section_workflow': '*',
        'section_metadata': '*'
            },
    max=None)

# print(results)


print('initializing_obser_repo')

# print(results)

''' creating rdf graphs '''


import rdflib
import requests
import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SKOS, RDF, RDFS, OWL, DC, DCTERMS, VOID, DOAP #most common namespaces
# import urllib.parse #for parsing strings to URI's



'''Initializing Graph'''







''' Observations '''

# un = [] 
if os.path.isfile(r'C:\Users\GuptaR\Desktop\nomad_files_v1_obser\un.txt'):
    pass
else:
    with open(r'C:\Users\GuptaR\Desktop\nomad_files_v1_obser\un.txt', "wb") as fp:   
        un=[]
        pickle.dump(un, fp)
    
with open(r'C:\Users\GuptaR\Desktop\nomad_files_v1_obser\un.txt', "rb") as fp:
    v = pickle.load(fp)

un = v
# print(un)
number = 2
length = len(un) + number
# print(length)
total = 0
for i, result in enumerate(results):
    # print(i)
        
  
    if i not in un:
        un.append(i)
        # print(i)
        
        
        
        if i <length:
            # print(i)
            g = Graph()


            # assigning namespaces and binding 
            
            sosa = Namespace('http://www.w3.org/ns/sosa/')
            ssn = Namespace('http://www.w3.org/ns/ssn/')
            time1 = Namespace('http://www.w3.org/2006/time#')
            qudt = Namespace('http://qudt.org/2.1/schema/qudt#')
            qudt_unit= Namespace('http://qudt.org/2.1/vocab/unit#')
            cdt = Namespace('http://w3id.org/lindt/custom_datatypes#')
            geo = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
            base = Namespace('http://example.org/data/')
            nomad = Namespace('http://https://nomad-coe.eu/ontology#')
            dc = Namespace('http://purl.org/dc/elements/1.1/')
            ab = Namespace('http://learningsparql.com/ns/data#')
            cdt = Namespace('http://w3id.org/lindt/custom_datatypes#') 
            matvoc = Namespace('http://stream-ontology.com/matvoc#') 
            
            
            g.bind('sosa', sosa)
            g.bind('ssn', ssn)
            g.bind('time1', time1)
            g.bind('qudt', qudt)
            g.bind('qudt_unit', qudt_unit)
            g.bind('cdt', cdt)
            g.bind('geo', geo)
            g.bind('base', base)
            g.bind('nomad', nomad)
            g.bind('ab', ab)
            g.bind('dc', dc)
            g.bind('cdt',cdt)
            g.bind('matvoc',matvoc)

            calc = result.section_run[0].section_single_configuration_calculation[:]
            if calc != None:
                
            # print(calc)
      
    
                for j in range(len(calc)):
                    # print(j)
                      
                
                    u = calc[j]
                    
                    
                    for att, value in (u.__dict__.items()):
                        # print(att)
                        r = 0
                       
                        # defining list for saving the attribute names 
                        meta = []
                        properties= []
                        labels=[] 
                        quantities = []
                        
                        if not att.startswith(('m_','single'
                                        )):
                            
                            # print(att)
                            
                            meta.append(att)
                            label = meta[r]  + '_' +  'calc'
                            labels.append(label)
                            prop = 'has' + '_' + att
                            # print(prop)
                            properties.append(prop)
                            quantities.append(att)
                            
                            # retrieving attribute values
                            observation = getattr(calc[j],meta[r])
                            
                           
        
        
                           
                            counter = []  
                            counter1 = []
                            counter2 = []
                            counter3 = []
                            
                          
         
                       
                           
                            
                            try:
                                
                                
                                shape = len(getattr(observation,'shape'))
                             
                                
                                
                              
                                magnitude = getattr(observation,'magnitude')   
                                
                               
                                
                                try:
                                    
                                    units = getattr(observation,'units')
                                    unit = str(units)
                                except:
                                    pass
                                
                                
                                
                                counter.append(properties)
                                
                                
                             
                                
                                y = BNode()
                                o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                # print(str(quantities[q]))
                                o = urllib.parse.quote(o)
                                # print(o)
                                # print(i)
                                a = 'mat' +str(i+1)
                                
                                g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                
                                g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                
                                
            
                                if shape >=1:
                                    
                                    g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                    
                                
                                    
                                    g.add((y, URIRef(nomad+'array'), Literal(magnitude)))
                                
                                else:
                                           
                                   
                                    g.add((y, URIRef(qudt+'numericValue'), Literal(magnitude)))
                                
                                if unit !=None:
                                    u = 0
    
                                    
                                    v = validators.url(qudt_unit + unit)
                                    # print(v)
                                    if v == True:
                                        g.add((y, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit)))
                                        u+=1
                                    else:
                                        if u<1:
                                            unit = unit.replace(" ","")
                                            
                                            g.add((y, URIRef(qudt + 'unit'), URIRef(ab+unit)))
                                    # g.add((y, URIRef(qudt+'unit'), URIRef(qudt_unit+str(units))))
                                    
                            
                            except:
                                
                                
                            
                          
                                
                                if properties not in counter:
                                    # print('rohit')
                                    
                                    counter1.append(properties)
                                    
                                    y = BNode()
                                    o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                    
                                    # print(str(quantities[q]))
                                    
                                    o = urllib.parse.quote(o)
                                    
                                    # print(o)
                                    # print(i)
                                    a = 'mat' +str(i+1)
                                    
                                    g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                    g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                    
                                    g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                    g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                    g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                    
                                   
                                    
                                    if type(observation) == list:
                                        if (len(observation)) > 1:
                                            # print(observation)
                                            k = 0
                                            for para in observation:
                                            
                                                for att1, val1 in para.__dict__.items():
                                                    if not att1.startswith(('m','_','section')):
                                                        # print(att1)
                                                        c = 0 
                                                        # meta = 0
                                                        properties1 = []
                                                        properties2 = []
                                                        # meta.append(att1)
                                                        prop1 = 'has'+ '_' + att1
                                                        prop2 = 'has'+ '_' + att + str(k)
                                                        properties2.append(prop2)
                                                        properties1.append(prop1)
                                                        value = getattr(para,att1)
                                                        # print(value)
                                                        try:
                                                            shape2 = len(getattr(value,'shape'))
                                                            magnitude2 = getattr(value,'magnitude')
                                                            units = getattr(value,'units')
                                                            unit2 = str(units)
                                                            y1 = BNode()
                                                            y2 = BNode()
                                                            g.add((y, URIRef(nomad+properties2[c]), y1))
                                                            g.add((y1,URIRef(nomad+properties1[c]),y2))
                                                            if shape2 >= 1:
                                                               
                                                                g.add((y2,URIRef(nomad+'array'),Literal(magnitude2)))
                                                                
                                                            elif shape2 == 0:
                                                               
                                                                g.add((y2,URIRef(nomad+'numericValue'),Literal(magnitude2)))
                                                            
                                                            if unit2 != None:
                                                                
                                                                u = 0
                                                                
                                                          
                                                                v = validators.url(qudt_unit + unit2)
                                                                # print(v)
                                                                if v == True:
                                                                    g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                    u+=1
                                                                else:
                                                                    if u<1:
                                                                        unit2 = unit2.replace(" ","")
                                                                        g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit2)))
                                                               
                                                    
                                                               
                                                
                                                            counter2.append(properties1)
                                                        except:
                                                            pass
                                                        try:
                                                            if properties1 not in counter2:
                                                                shape3 = len(getattr(value,'shape'))
                                                                counter3.append(properties1)
                                                                
                                                                    
                                                                    # magnitude3 = getattr(value, 'magnitude') 
                                                                    # ref2.append(properties1)
                                                                
                                                                try:
                                                                    units = getattr(value,'units')
                                                                    unit3 = str(units)
                                                                    counter3.append(properties1)
    
                                                                except:
                                                                    pass
                                                                y1 = BNode()
                                                                y2 = BNode()
                                                                g.add((y, URIRef(nomad+properties2[c]), y1))
                                                                g.add((y1,URIRef(nomad+properties1[c]),y2))
                                                                if shape3 >= 1:
                                                                   
                                                                    g.add((y2,URIRef(nomad+'array'),Literal(value)))
                                                                elif shape3 == 0:
                                                                   
                                                                    g.add((y2,URIRef(nomad+'numericValue'),Literal(value)))
                                                                if unit3 != None:
                                                                    
                                                                    u = 0
                                                                    
                                                             
                                                                    v = validators.url(qudt_unit + unit3)
                                                                    # print(v)
                                                                    if v == True:
                                                                        g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                        u+=1
                                                                    else:
                                                                        if u<1:
                                                                            unit3 = unit3.replace(" ","")
                                                                            g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit3)))
                                                               
                                                    
                                                                    
                                                        
                                                        except:
                                                            pass
                                                k+=1
                                        
                                        else:
                                            for para in observation:
                                                for att2,val2 in para.__dict__.items():
                                                    if not att2.startswith(('m','_')):
                                                        # print(att2)
                                                        # print(para)
                                                        c = 0 
                                                        # meta = 0
                                                        properties1 = []
                                                        properties2 = []
                                                        # meta.append(att1)
                                                        prop1 = 'has'+ '_' + att2
                                                        prop2 = 'has'+ '_' + att 
                                                        properties2.append(prop2)
                                                        properties1.append(prop1)
                                                        value = getattr(para,att2)
                                                        # print(value)
                                                        # value = getattr(para,'dos_values')
                                                        
                                                        try:
                                                            
                                                            for att3, val3 in value.__dict__.items():
                                                                if not att3.startswith(('m','_')):
                                                                    # print(att3)
                                                                    c = 0 
                                                                    # meta = 0
                                                                    properties3 = []
                                                                    properties2 = []
                                                                    properties1 = []
                                                                    # meta.append(att1)
                                                                    prop3 = 'has'+ '_' + att3
                                                                    prop2a = 'has'+ '_' + att 
                                                                    prop1 = 'has'+ '_' + att2
                                                                    properties2.append(prop2)
                                                                    properties3.append(prop3)
                                                                    properties1.append(prop1)
                                                                    value1 = getattr(value,att3)
                                                                    # print(value1)
                                                                    y1 = BNode()
                                                                    y2 = BNode()
                                                                   
                                                                    g.add((y, URIRef(nomad+properties2[c]), y1))
                                                                    g.add((y1, URIRef(nomad+properties1[c]), y2))
                                                                    
                                                                    g.add((y2,URIRef(nomad+properties3[c]),Literal(value1)))
                                                            counter2.append(properties1)
                                                                    
                                                        except:
                                                            pass
    
                                                        # print(value)
                                                        try:
                                                            if properties1 not in counter2:
                                                                
                                                                shape2 = len(getattr(value,'shape'))
                                                                magnitude2 = getattr(value,'magnitude')
                                                                units = getattr(value,'units')
                                                                unit2 = str(units)
        
                                                                y1 = BNode()
                                                                y2 = BNode()
                                                                g.add((y, URIRef(nomad+properties2[c]), y1))
                                                                g.add((y1,URIRef(nomad+properties1[c]),y2))
                                                                if shape2 >= 1:
                                                                    
                                                                    g.add((y2,URIRef(nomad+'array'),Literal(magnitude2)))
                                                                elif shape2 == 0:
                                                                   
                                                                    g.add((y2,URIRef(nomad+'numericValue'),Literal(magnitude2)))
                                                                
                                                                if unit2 != None:
                                                                    
                                                                    u = 0
                                                                    
                                                                   
                                                                    v = validators.url(qudt_unit + unit2)
                                                                    # print(v)
                                                                    if v == True:
                                                                        g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                        u+=1
                                                                    else:
                                                                        if u<1:
                                                                            unit2 = unit2.replace(" ","")
                                                                            g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit2)))
                                                                   
                                                        
                                                                   
                                                                counter2.append(properties1)
                                                            # print(ref1)
                                                            # print('rohit')
                                                            
                                                        except:
                                                            pass
                                                        try:
                                                            if properties1 not in counter2:
                                                                # print('rohit')
                                                                # print(properties1)
                                                                shape3 = len(getattr(value,'shape'))
                                                                counter3.append(properties1)
                                                                try:
                                                                    units = getattr(value,'units')
                                                                    unit3 = str(units)
                                                                    counter3.append(properties1)
                                                                except:
                                                                    pass
                                                                y1 = BNode()
                                                                y2 = BNode()
                                                                g.add((y, URIRef(nomad+properties2[c]), y1))
                                                                g.add((y1,URIRef(nomad+properties1[c]),y2))
                                                                if shape3 >= 1:
                                                                   
                                                                    g.add((y2,URIRef(nomad+'array'),Literal(value)))
                                                                elif shape3 == 0:
                                                                   
                                                                    g.add((y2,URIRef(nomad+'numericValue'),Literal(value)))
                                                                if unit3 != None:
                                                                    
                                                                    u = 0
                                                                    
                                                               
                                                                    v = validators.url(qudt_unit + unit3)
                                                                    # print(v)
                                                                    if v == True:
                                                                        g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                        u+=1
                                                                    else:
                                                                        if u<1:
                                                                            unit3 = unit3.replace(" ","")
                                                                            g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit3)))
                                                               
                                                    
                                                                                                                        
                                                        except:
                                                            if properties1 not in counter2 and properties1 not in counter3:
                                                                # print(properties1)
                                                                y1 = BNode()
                                                                g.add((y, URIRef(nomad+properties2[c]), y1))
                                                                g.add((y1,URIRef(nomad+properties1[c]),Literal(value)))
                                                               
                                                                
                                                                    
                                    
                                    
                                    elif type(observation) in [str,int,complex,float,bool]:
                                        # print(observation)
                                        g.add((y, URIRef(nomad+properties[r]), Literal(observation)))
                                    
                                    
        
                            finally:
                                
                                if properties not in counter and properties not in counter1:
                                    
                                    # print('properties')
                                        
                                  
                                    shape1 = len(getattr(observation,'shape'))
                                  
                                    
                                    
                                    try:
                                        
                                        unit1 = getattr(observation,'units')
                                        
                                    
                                    except:
                                        pass
                                    
                                    # refer.append(X)
                                    
                                    y = BNode()
                                    
                                    o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                    # print(str(quantities[q]))
                                    o = urllib.parse.quote(o)
                                    # print(o)
                                    # print(i)
                                    a = 'mat' +str(i+1)
                                    
                                    g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                    g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                    
                                    g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                    g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                    g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                    
                                    if shape1 >= 1:
                                        
                                        g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                      
                                        g.add((y, URIRef(nomad+'array'), Literal(observation)))
                                    
                                    else:
                                        
                                        g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                       
                                        g.add((y, URIRef(qudt+'numericValue'), Literal(observation)))
                                    
                                    
                                    if unit1 != None:
                                        
                                        u = 0
                                        
                                     
                                        v = validators.url(qudt_unit + unit1)
                                        # print(v)
                                        if v == True:
                                            g.add((y, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit1)))
                                            u+=1
                                        else:
                                            if u<1:
                                                unit1 = unit1.replace(" ","")
                                                g.add((y, URIRef(qudt + 'unit'), URIRef(ab+unit1)))
                        
                                                
                                      
                                          
                   
                                        
                                    # except:
            #                         #     pass
            with open(r'C:\Users\GuptaR\Desktop\nomad_files_v1_obser\un.txt', "wb") as fp:   
                pickle.dump(un, fp)
                                        
            g.serialize(r'C:\Users\GuptaR\Desktop\nomad_files_v1_obser\obser_v1_' + str(i) + '.ttl', format='turtle')
            # print('saved')
            # print('enter_repo' + str(i))
            
            start = time.time()
            
            headers = {
                    'Content-Type': 'application/x-turtle',
                }
                
            # data = g.serialize(format='turtle').decode('UTF-8')
            response = requests.post('http://localhost:7200/repositories/obser_all/statements', data=open(r'C:\Users\GuptaR\Desktop\nomad_files_v1_obser\obser_v1_' + str(i) + '.ttl','r').read(), headers=headers)
            # print(response)
            # print('done_repo' + str(i))
            end = time.time()
            tot = end - start
            total = total + tot 
            # print(total)
     
        else:
            break
print('observation_success')
 
       

