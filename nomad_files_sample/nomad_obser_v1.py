# -*- coding: utf-8 -*-



import urllib.parse
# import weakref
from nomad import client, config
import numpy as np
import validators




# from nomad import client, config
# config.client.url = 'http://nomad-lab.eu/prod/rae/api'
# results = client.query_archive(query={
#     'upload_id': ['BJsixXW0Qoy5A9WB5BBqtQ'],
#     'calc_id': ['CdVHQl-adqWnB3TYm11ETr4ML2cA']},
#       required = {       'section_run': {
#             'section_method': '*',
#             'section_single_configuration_calculation': '*',
#             'section_system': '*'},
#         'section_workflow': '*',
#         'section_metadata': '*'
#         })

results = client.query_archive(query={
    'upload_id': ['5TM3DMqGTtKtP5qfQ7havg'],
    'calc_id': ['pieH9n6qoVbsOnH7bTdjtPeVo6QM']},
        required={
        'section_run': {
            'section_method': '*',
            'section_single_configuration_calculation': '*',
            'section_system': '*'},
        'section_workflow': '*',
        'section_metadata': '*'
            })

print(results)


# from nomad import client, config
# config.client.url = 'http://nomad-lab.eu/prod/rae/api'
# results = client.query_archive(query={
#     'upload_id': ['B0ygTlpCR7yU5ORzv8i94g'],
#     'calc_id': ['rShBBcjZIp6t5w2d0GAPzId4BAGk']},
#      required={
#         'section_run': {
#             'section_method': '*',
#             'section_single_configuration_calculation': '*',
#             'section_system': '*'},
#         'section_workflow': '*',
#         'section_metadata': '*'
#             })

# print(results)

########################################

# import time
# import pandas as pd
# import pickle
# from nomad.client import ArchiveQuery
# from nomad.metainfo import units
# import numpy as np
# import urllib.parse



# results = ArchiveQuery(
#     # url='http://nomad-lab.eu/prod/rae/beta/api',
#     query={
#         'dft.code_name': 'VASP'
#     },
#     required={
#         'section_run': {
#             'section_method': '*',
#             'section_single_configuration_calculation': '*',
#             'section_system': '*'},
#         'section_workflow': '*',
#         'section_metadata': '*'
#             } )


# print(results)




# print(results)

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
nomad = Namespace('http://https://nomad-coe.eu/ontology#')
dc = Namespace('http://purl.org/dc/elements/1.1/')
ab = Namespace('http://learningsparql.com/ns/data#')
cdt = Namespace('http://w3id.org/lindt/custom_datatypes#') 


g.bind('sosa', sosa)
g.bind('ssn', ssn)
g.bind('time', time)
g.bind('qudt', qudt)
g.bind('qudt_unit', qudt_unit)
g.bind('cdt', cdt)
g.bind('geo', geo)
g.bind('base', base)
g.bind('nomad', nomad)
g.bind('ab', ab)
g.bind('dc', dc)
g.bind('cdt',cdt)




''' Observations '''

     

for i, result in enumerate(results):
    
    if i <10:
        print(i)
        calc = result.section_run[0].section_single_configuration_calculation[:]
        if calc != None:
            
        # print(calc)
  

            for j in range(len(calc)):
                # print(j)
                  
            
                u = calc[j]
                
                # vars(u)
             
                for att, value in (u.__dict__.items()):
                    # print(att)
                    r = 0
                    # print(att)
                    rohit = []
                    properties= []
                    labels=[] 
                    quantities = []
                    if not att.startswith(('m_','single'
                                    )):
                        
                        # print(att)
                        
                        rohit.append(att)
                        label = rohit[r]  + '_' +  'calc'
                        labels.append(label)
                        prop = 'has' + '_' + att
                        # print(prop)
                        properties.append(prop)
                        quantities.append(att)
                        # print(labels)
                        # print(rohit)
                        
                        # gupta.append(value)
                               
                        observation = getattr(calc[j],rohit[r])
                        
                        # print(observation)
                        # observation = getattr(calc[j],'energy_free')
                        # magnitude = getattr(observation,'magnitude')
                        # unit = getattr(observation,'units')
                        # shape = len(getattr(observation,'shape'))
                        # print(shape)
    
    
                        
                        sin = []  
                        ref = []
                        ref1 = []
                        ref2 = []
                        
                        # if type(observation) == list:
                        #     for x in observation:
                        #         para = x
                        # else:
                        #     para = observation
                            
                            # print(para)
                        
     
                   
                       
                        
                        try:
                            
                            
                            shape = len(getattr(observation,'shape'))
                         
                            
                            
                          
                            magnitude = getattr(observation,'magnitude')   
                            
                           
                            
                            try:
                                
                                units = getattr(observation,'units')
                                unit = str(units)
                            except:
                                pass
                            
                            
                            
                            sin.append(properties)
                            
                            
                         
                            
                            y = BNode()
                            o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                            # print(str(quantities[q]))
                            o = urllib.parse.quote(o)
                            # print(o)
                            # print(i)
                            a = 'mat' +str(i+1)
                            
                            g.add((URIRef(ab+o), RDF.type, URIRef(sosa+'Observation')))
                            g.add((URIRef(ab+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(ab+a)))
            
                            g.add((URIRef(ab+o), URIRef(sosa+'hasResult'), y))
                            g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                            g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                            
                            
        
                            if shape >=1:
                                
                                g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                g.add((y, URIRef(nomad+'array'), Literal(magnitude,datatype=XSD.float)))
                            
                            else:
                                       
                                g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                g.add((y, URIRef(qudt+'numericValue'), Literal(magnitude,datatype=XSD.float)))
                            
                            if unit !=None:
                                u = 0

                                try:
                                    v = validators.url(qudt_unit + unit)
                                    # print(v)
                                    if v == True:
                                        g.add((y, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit)))
                                        u+=1
                                    else:
                                        if u<1:
                                            g.add((y, URIRef(qudt + 'unit'), Literal(unit)))
                                # g.add((y, URIRef(qudt+'unit'), URIRef(qudt_unit+str(units))))
                                except:
                                    pass
                        
                        except:
                            
                            
                        
                      
                            
                            if properties not in sin:
                                # print('rohit')
                                
                                ref.append(properties)
                                
                                y = BNode()
                                o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                
                                # print(str(quantities[q]))
                                
                                o = urllib.parse.quote(o)
                                
                                # print(o)
                                # print(i)
                                a = 'mat' +str(i+1)
                                
                                g.add((URIRef(ab+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(ab+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(ab+a)))
                
                                g.add((URIRef(ab+o), URIRef(sosa+'hasResult'), y))
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
                                                            
                                                            try:
                                                                v = validators.url(qudt_unit + unit2)
                                                                # print(v)
                                                                if v == True:
                                                                    g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                    u+=1
                                                                else:
                                                                    if u<1:
                                                                        g.add((y2, URIRef(qudt + 'unit'), Literal(unit2)))
                                                           
                                                
                                                            except:
                                                                pass
                                            
                                                        ref1.append(para)
                                                    except:
                                                        pass
                                                    try:
                                                        if para not in ref1:
                                                            shape3 = len(getattr(para,'shape'))
                                                            ref2.append(para)
                                                            try:
                                                                units = getattr(para,'units')
                                                                unit3 = str(units)
                                                            except:
                                                                pass
                                                            y1 = BNode()
                                                            y2 = BNode()
                                                            g.add((y, URIRef(nomad+properties2[c]), y1))
                                                            g.add((y1,URIRef(nomad+properties1[c]),y2))
                                                            if shape2 >= 1:
                                                                g.add((y2,URIRef(nomad+'array'),Literal(magnitude2)))
                                                            elif shape2 == 0:
                                                                g.add((y2,URIRef(nomad+'numericValue'),Literal(magnitude2)))
                                                            if unit3 != None:
                                                                
                                                                u = 0
                                                                
                                                                try:
                                                                    v = validators.url(qudt_unit + unit3)
                                                                    # print(v)
                                                                    if v == True:
                                                                        g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                        u+=1
                                                                    else:
                                                                        if u<1:
                                                                            g.add((y2, URIRef(qudt + 'unit'), Literal(unit3)))
                                                               
                                                
                                                                except:
                                                                    pass
                                                    
                                                    except:
                                                        pass
                                            k+=1
                                    
                                    else:
                                        for para in observation:
                                            for att2,val2 in para.__dict__.items():
                                                if not att2.startswith(('m','_','section')):
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
                                                            
                                                            try:
                                                                v = validators.url(qudt_unit + unit2)
                                                                # print(v)
                                                                if v == True:
                                                                    g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                    u+=1
                                                                else:
                                                                    if u<1:
                                                                        g.add((y2, URIRef(qudt + 'unit'), Literal(unit2)))
                                                           
                                                
                                                            except:
                                                                pass
                                            
                                                        ref1.append(para)
                                                    except:
                                                        pass
                                                    try:
                                                        if para not in ref1:
                                                            shape3 = len(getattr(para,'shape'))
                                                            ref2.append(para)
                                                            try:
                                                                units = getattr(para,'units')
                                                                unit3 = str(units)
                                                            except:
                                                                pass
                                                            y1 = BNode()
                                                            y2 = BNode()
                                                            g.add((y, URIRef(nomad+properties2[c]), y1))
                                                            g.add((y1,URIRef(nomad+properties1[c]),y2))
                                                            if shape2 >= 1:
                                                                g.add((y2,URIRef(nomad+'array'),Literal(magnitude2)))
                                                            elif shape2 == 0:
                                                                g.add((y2,URIRef(nomad+'numericValue'),Literal(magnitude2)))
                                                            if unit3 != None:
                                                                
                                                                u = 0
                                                                
                                                                try:
                                                                    v = validators.url(qudt_unit + unit3)
                                                                    # print(v)
                                                                    if v == True:
                                                                        g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                        u+=1
                                                                    else:
                                                                        if u<1:
                                                                            g.add((y2, URIRef(qudt + 'unit'), Literal(unit3)))
                                                               
                                                
                                                                except:
                                                                    pass                                                    
                                                    except:
                                                        pass
                                
                                
                                elif type(observation) in [str,int,complex,float,bool]:
                                    
                                    g.add((y, URIRef(ab+properties[r]), Literal(observation)))
                                
                                
    
                        finally:
                            
                            if properties not in sin and properties not in ref:
                                
                                # print('rohit')
                                    
                              
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
                                
                                g.add((URIRef(ab+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(ab+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(ab+a)))
                
                                g.add((URIRef(ab+o), URIRef(sosa+'hasResult'), y))
                                g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                
                                if shape1 >= 1:
                                    
                                    g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                    g.add((y, URIRef(nomad+'array'), Literal(observation,datatype=XSD.float)))
                                
                                else:
                                    
                                    g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                    g.add((y, URIRef(qudt+'numericValue'), Literal(observation,datatype=XSD.float)))
                                
                                
                                if unit1 != None:
                                    
                                    u = 0
                                    
                                    try:
                                        v = validators.url(qudt_unit + unit1)
                                        # print(v)
                                        if v == True:
                                            g.add((y, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit1)))
                                            u+=1
                                        else:
                                            if u<1:
                                                g.add((y, URIRef(qudt + 'unit'), Literal(unit1)))
                        
                                            
                                    except:
                                        pass
                                      
               
                        
                    # except:
                    #     pass
    
 
    else:
        break
        

# g.serialize(r'C:\Users\GuptaR\Desktop\nomad_re\nomad_ob.ttl', format='turtle')

g.serialize(r'C:\Users\GuptaR\Desktop\nomad_files\nomad_obser_v1.ttl', format='turtle')

