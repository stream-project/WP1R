# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:31:38 2021

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


import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')

# formatter = logging.basicConfig(filemode='a',
#                     format = '%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')


def setup_logger(name, log_file, level=logging.DEBUG):
    """To setup as many loggers as you want"""
    logger = logging.getLogger(name)
  
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

  
    logger.setLevel(level)
    logger.handlers.clear()
    logger.addHandler(handler)
       
    
   
    return logger



# first file logger
log_one = setup_logger('first_logger', r'C:\Users\GuptaR\Desktop\new_py_scripts\method\log1.log')

# from nomad import client, config

# results = client.query_archive(query={
#   'upload_id': ['-5WEQAwUSa6qNSrtS0YFrg'],
#   'calc_id': ['-vdV8O_pWTODtfpGutNJxl-hxooX']}, 
#         required={
#         'section_run': {
#             'section_method': '*',
#             'section_single_configuration_calculation': '*',
#             'section_system': '*',
#             'section_topology': '*'},
        
#         'section_workflow': '*',
#         'section_metadata': '*'
#             })



results = ArchiveQuery(
    # url='http://nomad-lab.eu/prod/rae/beta/api',
  
    required={
        'section_run': '*',
        'section_workflow': '*',
        'section_metadata': '*'
            },
    max=None)

print(results)

print('initializing_method_repo')


# print(results)

''' creating rdf graphs '''


import rdflib
import requests
import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SKOS, RDF, RDFS, OWL, DC, DCTERMS, VOID, DOAP #most common namespaces
# import urllib.parse #for parsing strings to URI's




''' Sampling '''


# un = [] 
if os.path.isfile(r'C:\Users\GuptaR\Desktop\new_py_scripts\method\un.txt'):
    pass
else:
    with open(r'C:\Users\GuptaR\Desktop\new_py_scripts\method\un.txt', "wb") as fp:   
        un=[]
        pickle.dump(un, fp)
    
with open(r'C:\Users\GuptaR\Desktop\new_py_scripts\method\un.txt', "rb") as fp:
    v = pickle.load(fp)

un = v
# print(un)
number = 10
length = len(un) + number
# print(length)
total = 0

for i, result in enumerate(results):
    
    if i not in un:
        un.append(i)
        # print(i)
        
        
        
        if i <length:
            print(i)
            
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
    
        
            # calc = result.section_run[0].section_single_configuration_calculation[-1]
            # calc = result.section_run[0].section_single_configuration_calculation[0]
            # calc = result.section_workflow
            
            metadata_log = result.section_metadata
            if metadata_log != None:   
                
                form_log = getattr(metadata_log,'formula')
                calc_log = getattr(metadata_log,'calc_id')
                print(calc_log)
                
            metadata = result.section_metadata
            # print(metadata)
            
            if metadata != None:        
                for attn, valuen in (metadata.__dict__.items()): 
                    if attn.startswith(('formula','pid')):
                        formula_name = getattr(metadata,'formula')
                        # pid_name = getattr(metadata,'pid')
                        # pid = 9
            
            esm = result.section_run[0].section_method[:]
            if esm != None:
                if type(esm) == list:
                    for x in esm:
                        X = x
                else:
                    X = esm
                
                # defining list for storing attributes    
                l1 = []
                l2 = []
                for att, value in X.__dict__.items():
                    if not att.startswith(('m','_')):
                        # print(att)
                        c = 0
                        meta = []
                        properties = []
                        meta.append(att)
                        prop = 'has' + '_' + meta[c]
                        properties.append(prop)
                        X1 = getattr(X,meta[c])
                      
                        
                      
                                
                                
                                
                           
    
                        try:
        
                            y = BNode()
                            shape = len(getattr(X1,'shape'))
        
                            # print(shape)
                            magnitude = getattr(X1,'magnitude')
                            units = getattr(X1,'units')
                            unit = str(units)
        
        
                            # print(unit)
        
        
                            # m = 'method' +str(i+1)
                            # a = 'mat' +str(i+1)
                            m = 'method'+ '_' + formula_name + '_' + str(i+1)
                            # a = 'mat' +str(i+1)
                            a = 'mat'+ '_' + formula_name + '_' + str(i+1)
                            
                            g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
                            g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), y))               
                            
                            if shape >= 1 :
                                g.add((y, URIRef(nomad + 'array'), Literal(magnitude)))                
                            elif shape == 0:
                                g.add((y, URIRef(nomad + 'numericalvalue'), Literal(magnitude))) 
                            
                       
                                
                            if unit !=None:       
                                u = 0
                                v = validators.url(qudt_unit + unit)
                                # print(v)
                                if v == True:
                                    g.add((y, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit)))
                                    u+=1
                                else:
                                    if u<1:
                                        unitf = unit.replace(" ","")
                                        g.add((y, URIRef(qudt + 'unit'), Literal(unitf)))
                                        metadata_log = result.section_metadata
                                        if metadata_log != None:   
                                            
                                            form_log = getattr(metadata_log,'formula')
                                            calc_log = getattr(metadata_log,'calc_id')
                                            print(calc_log)
                                            log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties[c] + ', ' + 'unit:' + unit + ', ' + 'c_unit:' + unitf + ', ' + 'check:' + '1')
                                
                            
                            l1.append(properties[c])
        
        
                               
                                
                        except:
                            pass
                        
                        try:
        
                            if properties[c] not in l1:
        
                              
                           
                              
                                shape1 = len(getattr(X1,'shape'))
                                # print(shape1)
                                l2.append(properties[c])
        
        
                              
                                
                               
                                try:
                                   
                                    units = getattr(X1,'units')
                                    unit1 = str(units)
                                    print(unit1)
                                    l2.append(properties[c])
        
        
                                except:
                                    pass
                                
        
        
                             
                                
                                # m = 'method' +str(i+1)
                                # a = 'mat' +str(i+1)
                                
                                m = 'method'+ '_' + formula_name + '_' + str(i+1)
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + str(i+1)
                                
                                g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
                                y1 =BNode()
                                
                                if shape1 >=1 :
                                    g.add((URIRef(matvoc+m), URIRef(nomad+properties[c]), y1))
                                    g.add((y1, URIRef(nomad+'array'), Literal(X1)))
                                
                                if shape1 == 0:
                                    g.add((URIRef(matvoc+m), URIRef(nomad+properties[c]), y1))
                                    g.add((y1, URIRef(nomad+'numericalValue'), Literal(X1)))
                                    
                                if unit1 != None:
                                    u = 0
                                    
                                    v = validators.url(qudt_unit + unit1)
                                    # print(v)
                                    if v == True:
                                        g.add((y1, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit1)))
                                        u+=1
                                    else:
                                        if u<1:
                                            unit1f = unit1.replace(" ","")
                                            g.add((y1, URIRef(qudt + 'unit'), URIRef(ab+unit1f)))
                                            metadata_log = result.section_metadata
                                            if metadata_log != None:   
                                                
                                                form_log = getattr(metadata_log,'formula')
                                                calc_log = getattr(metadata_log,'calc_id')
                                                log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties[c] + ', ' + 'unit:' + unit1 + ', ' + 'c_unit:' + unit1f + ', ' + 'check:' + '2')
                                    
                                    
                                 
        
                        except:
                            
                            if properties[c] not in l1 and  properties[c] not in l2:
                                # print(properties[c])
                                # m = 'method' +str(i+1)
                                # a = 'mat' +str(i+1)
                                
                                m = 'method'+ '_' + formula_name + '_' + str(i+1)
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + str(i+1)
                                
                                if type(X1) in [str,int,float]:
                                    g.add((URIRef(matvoc+m), URIRef(nomad+properties[c]), Literal(X1)))
                                
                                else:
                                    if type(X1) == list:
                                        
                                        
                                        
                                        k=0
                                        for x in X1:
                                            
                                            for att2, value2 in x.__dict__.items():
                                                
                                                
                                                
                                                if not att2.startswith(('m_','_')):
                                                    
                                                    
                                                
                                                    c1=0
                                                    meta1=[]
                                                    properties1=[]
                                                    properties2=[]
    
                                                    meta1.append(att2)
                                                    prop1='has'+'_'+meta1[c1] 
                                                    prop2 = 'has' + '_' + meta[c] + '_'  + str(k)
    
    
                                                    properties1.append(prop1)
                                                    properties2.append(prop2)
    
                                                    value = getattr(x,meta1[c1])
                                                    # print(value)
                                                    
                                                    # value1 = set(value)
                                                    # # print(value)
                                                    # value = getattr(X2,'mapping_section_method_basis_set_cell_associated')
                                                    # print(value)
                                                    try:
                                                        
                                                        for att3,val3 in  value.__dict__.items():
                                                            # print(att3)
                                                            if not att3.startswith('m'):
                                                                # print(att3)
                                                                value_try = set(value)
                                                                # print(value)
                                                                y2 = BNode()
                                                                g.add((URIRef(matvoc+m), URIRef(nomad+properties2[c]), y2))
                                                                g.add((y2, URIRef(nomad+properties1[c1]), Literal(value_try)))
                                                                # v = getattr(value,att3)
                                                                # print(v)
                                                            
                                                                                                               
                                                        
                                                        
                                                    except:
                                                          y2 = BNode()
                                                          g.add((URIRef(matvoc+m), URIRef(nomad+properties2[c]), y2))
                                                          g.add((y2, URIRef(nomad+properties1[c1]), Literal(value)))
                                            k+=1

                                                                
                                                # break        
                       
                                
                    
                  
            
            
            
            w_type = result.section_workflow.workflow_type
            # print(w_type)
            
            if w_type !=None:
                
                
                for e in range(len(w_type)):
                        
                 
                        # m = 'method' +str(i+1)
                        # a = 'mat' +str(i+1)
                        # esm = str(esm)
                        
                        m = 'method'+ '_' + formula_name + '_' + str(i+1)
                        # a = 'mat' +str(i+1)
                        a = 'mat'+ '_' + formula_name + '_' + str(i+1)
                        
                        g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
                        g.add((URIRef(matvoc+m), URIRef(nomad + 'workflowtype'), URIRef(nomad + w_type )))
    
        
            else:
                pass
            
            
            metadata = result.section_metadata
            
            if metadata != None:
                
                for att, value in (metadata.__dict__.items()):  
                    if att.startswith(('dft')):
                        
                        c = 0
                        meta = []
                        properties = []
                        meta.append(att)
                        prop = 'has' + '_' + meta[c]
                        properties.append(prop)
                        # print(properties[m])
                        # print(meta[m])
                        meta_data = getattr(metadata,meta[c])
                        
                        # print(meta_data)
                        
                        for att, value in (meta_data.__dict__.items()):
                            if not att.startswith(('m_','workflow',)):
                                # print(att)
                                c = 0 
                                meta = []
                                properties = []
                                meta.append(att)
                                prop = 'has' + '_' + meta[c]
                                properties.append(prop)
                                # print(meta_data)
                                meta_dft = getattr(meta_data,meta[c])
                               
                                
                                t_list = []
                                
                                try:
                                    for att1, val1 in meta_dft.__dict__.items():
                                        if not att1.startswith(('m','_')):
                                            
                                            c2 = 0
                                            meta3 = []
                                            properties3= []
                                            meta3.append(att1)
                                            prop3= 'has' + '_' + meta3[c2]
                                            properties3.append(prop3)
                                            x = getattr(meta_dft,att1)
                                            # print(x)
                                            # value3 = getattr(meta_dft,'structure_features')
                                            # print(value3)
                                            # print('ru')
                                            try:
                                                
                                                if type(x) == list and len(x)>=1:
                                                    
                                                    
                                                        
                                                    
                                                    k1=0
                                                    
                                                    for x1 in x:
                                                        for att2, val2 in x1.__dict__.items():
                                                            if not att2.startswith(('m','_')):
                                                                # print(att2)
                                                                c3 = 0
                                                                meta4 = []
                                                                properties5=[]
                                                                properties4= []
                                                                meta4.append(att2)
                                                                prop4= 'has' + '_' + meta4[c3]
                                                                # print(prop4)
                                                                
                                                                properties4.append(prop4)
                                                                prop3= 'has' + '_' + meta3[c2] + '_' + str(k1)
                                                                # print(prop3)
                                                                properties5.append(prop3)
                                                                value4 = getattr(x1,att2)
                                                                # print(value4)
                                                
        
                                                
                                            
                                                                # m = 'method' +str(i+1)
                                                                m = 'method'+ '_' + formula_name + '_' + str(i+1)
                                                                y3 = BNode()
                                                                y4 = BNode()
                                
                                                                g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
                                                                g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), y3))
                                                                g.add((y3, URIRef(nomad + properties5[c2]), y4))
                                                                g.add((y4, URIRef(nomad + properties4[c3]), Literal(value4)))
        
                                                                
                                                                
                                                                t_list.append(properties4)
                                                        k1+=1
                                                    
                                                elif type(x) != list:
                                                    try:
                                                        
                                                        if properties3 not in t_list:
                                                            
                                                            shape2 = len(getattr(x,'shape'))
                                                            magnitude2 = getattr(x,'magnitude')
                                                            units = getattr(x,'units')
                                                            unit2 = str(units)
                                                            t_list.append(properties3)
    
    
        
                                                            
                                                            # m = 'method' +str(i+1)
                                                            m = 'method'+ '_' + formula_name + '_' + str(i+1)
                                                            y5 = BNode()
                                                            y6 = BNode()
                            
                                                            g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
                                                            if shape2 >= 1:
                                                                g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), y5))
                                                                g.add((y5, URIRef(nomad + properties3[c2]), y6))
                                                                g.add((y6, URIRef(nomad + 'array'), Literal(magnitude2)))
                                                            elif shape2 == 0:
                                                                g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), y5))
                                                                g.add((y5, URIRef(nomad + properties3[c2]), y6))
                                                                g.add((y6, URIRef(nomad + 'numericValue'), Literal(x)))
                                                            if unit2 !=None:  
                                                                u = 0
                                                                
                                                                v = validators.url(qudt_unit + unit2)
                                                                # print(v)
                                                                if v == True:
                                                                    g.add((y6, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                    u+=1
                                                                else:
                                                                    if u<1:
                                                                        unit2f = unit2.replace(" ","")
                                                                        g.add((y6, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                        metadata_log = result.section_metadata
                                                                        if metadata_log != None:   
                                                                            
                                                                            form_log = getattr(metadata_log,'formula')
                                                                            calc_log = getattr(metadata_log,'calc_id')
                                                                            log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties3[c2] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '3')
                                                                
                                                                
                                                                
                                                            
    
                                                    except:
                                                        pass
                                                    
                                                    try:
                                                        if properties3 not in t_list:
                                                            shape3 = len(getattr(x,'shape'))
                                                            t_list.append(properties3)
                                                            try:
                                                                units = getattr(x,'units')
                                                                unit3 = str(units)
                                                                t_list.append(properties3)
                                                            except:
                                                                pass
                                                            # m = 'method' +str(i+1)
                                                            m = 'method'+ '_' + formula_name + '_' + str(i+1)
                                                            y5 = BNode()
                                                            y6 = BNode()
                            
                                                            g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
                                                            if shape3 >= 1:
                                                                g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), y5))
                                                                g.add((y5, URIRef(nomad + properties3[c2]), y6))
                                                                g.add((y6, URIRef(nomad + 'array'), Literal(x)))
                                                            elif shape3 == 0:
                                                                g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), y5))
                                                                g.add((y5, URIRef(nomad + properties3[c2]), y6))
                                                                g.add((y6, URIRef(nomad + 'numericValue'), Literal(x)))
                                                            if unit3 !=None:  
                                                                u = 0
                                                                v = validators.url(qudt_unit + unit3)
                                                                # print(v)
                                                                if v == True:
                                                                    
                                                                    g.add((y6, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                    u+=1
                                                                else:
                                                                    
                                                                    if u<1:
                                                                        unit3f = unit3.replace(" ","")
                                                                        g.add((y6, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                        metadata_log = result.section_metadata
                                                                        if metadata_log != None:   
                                                                            
                                                                            form_log = getattr(metadata_log,'formula')
                                                                            calc_log = getattr(metadata_log,'calc_id')
                                                                            log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties3[c2] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '4')
                                                                
                                                                
                                                              
                                                        
                                                    except:
                                                        
                                                        
                                                        
                                                        if properties3 not in t_list:
                                                            # m = 'method' +str(i+1)
                                                            m = 'method'+ '_' + formula_name + '_' + str(i+1)
                                                            y5 = BNode()
                          
                                                            g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
                                                            g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), y5))
                                                            g.add((y5, URIRef(nomad + properties3[c2]), Literal(x)))
                                                            t_list.append(properties3)
                                                    
                                                    
                                            
                                                else:
                                                    
                                                      
                                                    if properties3 not in t_list and type(x) == list:
                                                     
                                             
                                                          # m = 'method' +str(i+1)
                                                          m = 'method'+ '_' + formula_name + '_' + str(i+1)
                                                          y5 = BNode()
                         
                                                          g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
                                                          g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), y5))
                                                          g.add((y5, URIRef(nomad + properties3[c2]), Literal(x)))
                                                          t_list.append(properties3)
                                          
                                            except:
                                                pass
                                                
                                                
                                               
    
                                                        
                                          
                                   
        
                                except:
                                    
                                    
                                   
                                    
                                    
                                    if properties not in t_list:
                                        
                                        # a = 'mat' + str(i+1)  
                                        # m = 'method' +str(i+1)
                                        
                                        m = 'method'+ '_' + formula_name + '_' + str(i+1)
                                        # a = 'mat' +str(i+1)
                                        a = 'mat'+ '_' + formula_name + '_' + str(i+1)
        
                                        g.add((URIRef(matvoc+m), RDF.type, URIRef(sosa + 'Sampling')))
        
                                        g.add((URIRef(matvoc+m), URIRef(nomad + properties[c]), Literal(meta_dft)))
                                        g.add((URIRef(matvoc+m), URIRef(sosa + 'hasResult'), URIRef(matvoc + a )))

            with open(r'C:\Users\GuptaR\Desktop\new_py_scripts\method\un.txt', "wb") as fp:   
                
                pickle.dump(un, fp)
                                        
            g.serialize(r'C:\Users\GuptaR\Desktop\new_py_scripts\method\method_v1_' + str(i) + '.ttl', format='turtle')
            # print('saved')
            # print('enter_repo' + str(i))
            
            start = time.time()
            
            headers = {
                    'Content-Type': 'application/x-turtle',
                }
                
            # data = g.serialize(format='turtle').decode('UTF-8')
            response = requests.post('http://localhost:7200/repositories/method_all/statements', data=open(r'C:\Users\GuptaR\Desktop\new_py_scripts\method\method_v1_' + str(i) + '.ttl','r').read(), headers=headers)
            # print(response)
            # print('done_repo' + str(i))
            end = time.time()
            tot = end - start
            total = total + tot 
            # print(total)                      
     
        else:
            break

logging.shutdown()

print('method_success')
    


