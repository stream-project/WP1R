# -*- coding: utf-8 -*-





import time
# import pandas as pd
import pickle
from nomad.client import ArchiveQuery
from nomad.metainfo import units
import urllib.parse
import validators
import os
import configparser

from nomad.client import ArchiveQuery
from nomad.metainfo import units

import requests
import nomad

import numpy
# import logging

# logging.basicConfig(filename = r'C:\Users\GuptaR\Desktop\try1\rohit.txt',
#                     filemode='a',
#                     format = '%(asctime)s %(levelname)s-%(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')

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
log_one = setup_logger('first_logger', 'log1.log')


log_two = setup_logger('second_logger', 'log2.log')



results = ArchiveQuery(
    # url='http://nomad-lab.eu/prod/rae/beta/api',
  
    required={
        'section_run': '*',
        'section_workflow': '*',
        'section_metadata': '*'
            },
    max=None)





length = (len(results))



""" reading the path from path.properties file,specify the path of path.properties file"""

config = configparser.ConfigParser()

''' specify the path of path.properties file here '''
config.readfp(open('./path.properties'))


''' reading paths from path.properties file '''
k_band = config.get('SECTION_CALCULATION', 'k_band' )
k_norm = config.get('SECTION_CALCULATION', 'k_norm' )
atom_dos = config.get('SECTION_CALCULATION', 'atom_dos' )
species_dos = config.get('SECTION_CALCULATION', 'species_dos' )
dos = config.get('SECTION_CALCULATION', 'dos' )
eigen= config.get('SECTION_CALCULATION', 'eigen' )
iteration = config.get('SECTION_CALCULATION', 'iteration' )
section_cal = config.get('SECTION_CALCULATION', 'section_cal' )
section_ener = config.get('SECTION_CALCULATION', 'section_ener' )




k_norm_seg = config.get('SECTION_NORMALIZED', 'k_norm_seg' )






import rdflib
import requests
import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SKOS, RDF, RDFS, OWL, DC, DCTERMS, VOID, DOAP #most common namespaces
# import urllib.parse #for parsing strings to URI's



'''Initializing Graph'''

''' Observations '''

# un = [] 
if os.path.isfile('un.txt'):
    pass
else:
    with open('un.txt', "wb") as fp:   
        un=[]
        pickle.dump(un, fp)
    
with open('un.txt', "rb") as fp:
    v = pickle.load(fp)

un = v
# print(un)
number = 100
length = len(un) + number
# print(length)
total = 0

# un = v
# # print(un)
# number = 2
# length = len(un) + number
# # print(length)
# total = 0
for i, result in enumerate(results):
    
    if i not in un:
        un.append(i)
        # print(i)
    
        # print(i)
        
        if i < length:
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
            
            metadata = result.section_metadata
            # print(metadata)
            
            if metadata != None:        
                for attn, valuen in (metadata.__dict__.items()): 
                    if attn.startswith(('formula','pid')):
                        formula_name = getattr(metadata,'formula')
                        pid_name = getattr(metadata,'calc_id')
    
            calc = result.section_run[0].section_single_configuration_calculation[:]
            if calc != None:
                
            # print(calc)
      
    
                for j in range(len(calc)):
                    # print(j)
                      
                
                    u = calc[j]
                    
                    
                    for att, value in (u.__dict__.items()):
                        # print(att)
                        if not att.startswith(('m','_','section_basis_set','single','section')):
                            
                            r = 0
                           
                            # defining list for saving the attribute names 
                            meta = []
                            properties= []
                            labels=[] 
                            quantities = []
                            
                            meta.append(att)
                            label = meta[r]  + '_' +  'calc'
                            labels.append(label)
                            prop = 'has' + '_' + att
                            # print(prop)
                            properties.append(prop)
                            quantities.append(att)
                            
                            # retrieving attribute values
                            observation = getattr(calc[j],meta[r])
                            # print(observation)
                            # observation = getattr(calc[j],'section_k_band')
                            y = BNode()
                            o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                            # print(str(quantities[q]))
                            o = urllib.parse.quote(o)
                            # print(o)
                            # print(i)
                            # a = 'mat' +str(i+1)
                            # print(properties)
                            
                            m = 'method'+ '_' + formula_name + '_' + pid_name
                            # a = 'mat' +str(i+1)
                            a = 'mat'+ '_' + formula_name + '_' + pid_name
                            
                            g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                            g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
            
                            g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                            g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                            g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                            g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
        
                            
                            
                            coun = [] 
                            counter0 = []
                            counter00 = []
                            counter000 = []
                            counter0000 = []
                            counter00000 = []
                            counter = []  
                            counter1 = []
                            counter2 = []
                            counter3 = []
                            cq = []
                            cq1 = []
                            cq2 = []
                            bz = []
                            bz1 = []
                            bz2 = []
                            cou = []
                            
                            try:
                                
                                
                                shape = len(getattr(observation,'shape'))
                                # print('yeah')
                                counter.append(properties)
                             
                                
                                
                              
                                magnitude = getattr(observation,'magnitude')
                                counter.append(properties)
                                
                               
                                
                                try:
                                    
                                    units = getattr(observation,'units')
                                    unit = str(units)
                                    counter.append(properties)
                                except:
                                    pass
                                
                                
                                
                                
                                # print(properties)
                                
                                
                             
                                
                            
                                
                                
                                
                                if shape >=1:
                                    
                                  
                                    
                                
                                    
                                    g.add((y, URIRef(nomad+'array'), Literal(magnitude)))
                                
                                elif shape == 0:
                                    # g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                           
                                   
                                    g.add((y, URIRef(qudt+'numericValue'), Literal(magnitude)))
                                
                                if unit !=None:
                                    u = 0
        
                                    
                                    v = validators.url(qudt_unit + unit)
                                    # print(v)
                                    if v == True:
                                        g.add((y, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit)))
                                        u+=1
                                        
                                        metadata_log = result.section_metadata
                                          # print(metadata)
                                         
                                      
                                        
                                    else:
                                        if u<1:
                                            unitf = unit.replace(" ","")
                                            
                                            g.add((y, URIRef(qudt + 'unit'), URIRef(ab+unitf)))
                                            metadata_log = result.section_metadata
                                            if metadata_log != None:   
                                                form_log = getattr(metadata_log,'formula')
                                                calc_log = getattr(metadata_log,'calc_id')
                                                log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties + ', ' + 'unit:' + unit + ', ' + 'c_unit:' + unitf + ', ' + 'check:' + '1')
                                             
                                            
                                    # g.add((y, URIRef(qudt+'unit'), URIRef(qudt_unit+str(units))))
                                
                        
                            except:
                                pass
                            
                            try:
                                if properties not in counter:
                                    # print(properties)
                                    # print('hvbvbttdd')
                                    # # print('properties')
                                    # print('sggs')
                                  
                                    shape1 = len(getattr(observation,'shape'))
                                    cou.append(properties)
                                   
                                  
                                    
                                    
                                    try:
                                        
                                        unit1 = getattr(observation,'units')
                                        cou.append(properties)
                                        
                                    
                                    except:
                                        pass
                                    
                                    # refer.append(X)
                                    # print(cou)
                                    
                                  
                                    if shape1 >= 1:
                                        
                                        # g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                      
                                        g.add((y, URIRef(nomad+'array'), Literal(observation)))
                                    
                                    elif shape == 0:
                                        
                                        # g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                       
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
                                                unit1f = unit1.replace(" ","")
                                                g.add((y, URIRef(qudt + 'unit'), URIRef(ab+unit1f)))
                                                metadata_log = result.section_metadata
                                                if metadata_log != None:   
                                                    form_log = getattr(metadata_log,'formula')
                                                    calc_log = getattr(metadata_log,'calc_id')
                                                   
                                                    log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties + ', ' + 'unit:' + unit1 + ', ' + 'c_unit:' + unit1f + ', ' + 'check:' + '2')
                           
                                   
                            except:
                                pass
                            
                            if type(observation) in [str,int,complex,float,bool]:
                                # print(properties)
                                # print('see this')
                                            
                                g.add((y, URIRef(nomad+properties[r]), Literal(observation)))
                      
          
                            # print(att)
            calc = result.section_run[0].section_single_configuration_calculation[:]
            if calc != None:
                
            # print(calc)
      
    
                for j in range(len(calc)):
                    # print(j)
                      
                
                    u = calc[j]
                    
                    
                    for att, value in (u.__dict__.items()):
                        # print(att)
                        if not att.startswith(('m','_','section_basis_set','single')):    
                            # print(att)
                            coun = [] 
                            counter0 = []
                            counter00 = []
                            counter000 = []
                            counter0000 = []
                            counter00000 = []
                            counter = []  
                            counter1 = []
                            counter2 = []
                            counter3 = []
                            cq = []
                            cq1 = []
                            cq2 = []
                            bz = []
                            bz1 = []
                            bz2 = []
                            cou = []
                            
                        
                            
                            check_quantities = []
                            if att == k_band :
                                r = 0
                                meta = []
                                properties= []
                                labels=[] 
                                quantities = []
                                
                                
                                # print(att)
                                
                                meta.append(att)
                                label = meta[r]  + '_' +  'calc'
                                labels.append(label)
                                prop= 'has' + '_' + att
                                # print(prop)
                                properties.append(prop)
                                quantities.append(att)
                                
                                # retrieving attribute values
                                observation = getattr(calc[j],meta[r])
                                # print(observation)
                                # observation = getattr(calc[j],'section_k_band')
                                # for k in observation:
                                #     print(k)
        
                                # observation = getattr(calc[j],'section_k_band_normalized')
                                # print(observation)
        
                                # print(type(observation))
                                
                                
                                y = BNode()
                                o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                # print(str(quantities[q]))
                                o = urllib.parse.quote(o)
                                # print(o)
                                # print(i)
                                # a = 'mat' +str(i+1)
                                m = 'method'+ '_' + formula_name + '_' + pid_name
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + pid_name
                                
                                g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                
                                g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                
                              
                                
                                for para in observation:
                                   
                                
                                    for attt, vatt in para.__dict__.items():
                                    # print(attt)
                                        if not attt.startswith(('m','_')):
                                            
                                            # print(attt)
                                            
                                            if attt == 'section_band_gap':
                                                
                                            
                                            
                                           
                                    
                                    
                                                c = 0 
                                                # meta = 0
                                                properties1 = []
                                                properties2 = []
                                                # meta.append(att1)
                                                prop1 = 'has'+ '_' + attt
                                                # print(prop1)
                                                prop2 = 'has'+ '_' + att
                                                
                                                # values = getattr(para,'section_k_band_segment')
                                                val = getattr(para,attt)
                                                # print((val))
                                                properties2.append(prop2)
                                                # print(properties2)
                                                properties1.append(prop1)
                                                check_quantities.append((attt))
                                                print(check_quantities)
                                                print('1')
                                                # print(properties1)
                                                # value = getattr(para,'reciprocal_cell')
                                                # print(value)
                                                # print(value)
                                                # print(type(value))
                                                
                                                
                                                if type(val) == list:
                                                    
                                                    
                                                    print(len(val))
                                                    
                                                    # print(val)
                                                    
                                                    
                                                    
                                                   
                                                    if (len(val)) >= 1:
                                                        # para1 = val
                                                        # for para1 in val:
                                                        #     print(para1)
                                                        # # print(type(para))
                                                       
                                                        k = 0
                                                        for para1 in val:
                                                            # print(para1)
                                                       
                                                            for att11, val1 in para1.__dict__.items():
                                                                if not att11.startswith(('m','_')):
                                                                    # print(att11)
                                                                    c = 0 
                                                                    # meta = 0
                                                                    properties1a = []
                                                                    properties2a = []
                                                                    properties3a = []
                                                                    # meta.append(att1)
                                                                    prop1a = 'has'+ '_' + att
                                                                    prop2a = 'has'+ '_' + attt + str(k)
                                                                    prop3a = 'has' + '_' + att11
                                                                    properties2a.append(prop2a)
                                                                    properties1a.append(prop1a)
                                                                    properties3a.append(prop3a)
                                                                    # if att11 == 'value':
                                                                        
                                                                        
                                                                    valu = getattr(para1,att11)
                                                                        # print(valu)
                                                                        # value11 = getattr(valu,'magnitude')
                                                                        # print(value11)
                                                                    # valu = getattr(para1,'type')
            
                                                                    # valuer = getattr(para,'value')
                                                                       # value11 = getattr(valuer,'magnitude')
                                                                    # print(valuer)
                                                                    try:
                                                                        # print('rohit')
                                                                        shape2 = len(getattr(valu,'shape'))
                                                                        magnitude2 = getattr(valu,'magnitude')
                                                                        units = getattr(valu,'units')
                                                                        unit2 = str(units)
                                                                        # print(properties3a)
                                                                        y1 = BNode()
                                                                        y2 = BNode()
                                                                        y3 = BNode()
                                                                        g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                        g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                        g.add((y2,URIRef(nomad+properties3a[c]),y3))
                                                                        if shape2 >= 1:
                                                                          
                                                                            g.add((y3,URIRef(nomad+'array'),Literal(magnitude2)))
                                                                           
                                                                        elif shape2 == 0:
                                                                          
                                                                            g.add((y3,URIRef(nomad+'numericValue'),Literal(magnitude2)))
                                                                       
                                                                        if unit2 != None:
                                                                           
                                                                            u = 0
                                                                           
                                                                     
                                                                            v = validators.url(qudt_unit + unit2)
                                                                            # print(v)
                                                                            if v == True:
                                                                                g.add((y3, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                                u+=1
                                                                            else:
                                                                                if u<1:
                                                                                    # print('1')
                                                                                    unit2f = unit2.replace(" ","")
                                                                                    if unit2f == '1/meter':
                                                                                        
                                                                                        unit2f = 'ONE-PER-METER'
                                                                                    g.add((y3, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                                    metadata_log = result.section_metadata
                                                                                    if metadata_log != None:   
                                                                                        form_log = getattr(metadata_log,'formula')
                                                                                        calc_log = getattr(metadata_log,'calc_id')
                                                                                       
                                                                                        log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties3a[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '3')
                                                                                                              
                                                               
                                                                          
                                                                        counter000.append(properties3a)
                                                                      
                                                                    except:
                                                                        pass
                                                                    try:
                                                                        if properties3a not in counter000:
                                                                            # print(properties3a)
                                                                            # print('ffhh')
                                                                            # print(properties1)
                                                                            # print('rohit1')
                                                                            shape3 = len(getattr(valu,'shape'))
                                                                            # print(shape3)
                                                                            counter0000.append(properties3a)
                                                                           
                                                                          
                                                                            try:
                                                                                units = getattr(valu,'units')
                                                                                unit3 = str(units)
                                                                                counter0000.append(properties3a)
               
                                                                            except:
                                                                                pass
                                                                            y1 = BNode()
                                                                            y2 = BNode()
                                                                            y3 = BNode()
                                                                            g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                            g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                            g.add((y2,URIRef(nomad+properties3a[c]),y3))
                                                                            if shape3 >= 1:
                                                                              
                                                                                g.add((y3,URIRef(nomad+'array'),Literal(valu)))
                                                                            elif shape3 == 0:
                                                                              
                                                                                g.add((y3,URIRef(nomad+'numericValue'),Literal(valu)))
                                                                            if unit3 != None:
                                                                               
                                                                                u = 0
                                                                               
                                                                        
                                                                                v = validators.url(qudt_unit + unit3)
                                                                                # print(v)
                                                                                if v == True:
                                                                                    g.add((y3, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                                    u+=1
                                                                                else:
                                                                                    if u<1:
                                                                                        # print('2')
                                                                                        unit3f = unit3.replace(" ","")
                                                                                        
                                                                                        g.add((y3, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                                        metadata_log = result.section_metadata
                                                                                        if metadata_log != None:   
                                                                                            form_log = getattr(metadata_log,'formula')
                                                                                            calc_log = getattr(metadata_log,'calc_id')
                                                                                           
                                                                                            log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties3a[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '4')
                                                                          
                                                               
                                                                               
                                                                   
                                                                    except:
                                                                        pass
                                                                    try:
                                                                        
                                                                        if properties3a not in counter000 and properties3a not in counter0000:
                                                                            # print(properties3a)
                                                                            y1 = BNode()
                                                                            y2 = BNode()
                                                                            y3 = BNode()
                                                                            g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                            g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                            g.add((y2,URIRef(nomad+properties3a[c]),Literal(valu)))
                                                                            counter00000.append(properties3a)
                                                                    except:
                                                                        pass
                                                            k+=1
                                                           
                                                            
                                            if attt == 'section_k_band_segment':    
                                                
                                                c = 0 
                                                # meta = 0
                                                properties1 = []
                                                properties2 = []
                                                # meta.append(att1)
                                                prop1 = 'has'+ '_' + attt
                                                # print(prop1)
                                                prop2 = 'has'+ '_' + att
                                                
                                                # values = getattr(para,'section_k_band_segment')
                                                val = getattr(para,attt)
                                                # print((val))
                                                properties2.append(prop2)
                                                # print(properties2)
                                                properties1.append(prop1)
                                                check_quantities.append((attt))
                                                print(check_quantities)
                                                print('2')
                                                # print(properties1)
                                                # value = getattr(para,'reciprocal_cell')
                                                # print(value)
                                                # print(value)
                                                # print(type(value))
                                                
                                                
                                                if type(val) == list:
                                                    
                                                    
                                                    print(len(val))
                                                    
                                                    # print(val)
                                                    
                                                    
                                                    
                                                   
                                                    if (len(val)) >= 1:
                                                        # para1 = val
                                                        # for para1 in val:
                                                        #     print(para1)
                                                        # # print(type(para))
                                                       
                                                        k = 0
                                                        for para1 in val:
                                                            # print(para1)
                                                       
                                                            for att11, val1 in para1.__dict__.items():
                                                                if not att11.startswith(('m','_')):
                                                                    # print(att11)
                                                                    c = 0 
                                                                    # meta = 0
                                                                    properties1a = []
                                                                    properties2a = []
                                                                    properties3a = []
                                                                    # meta.append(att1)
                                                                    prop1a = 'has'+ '_' + att
                                                                    prop2a = 'has'+ '_' + attt + str(k)
                                                                    prop3a = 'has' + '_' + att11
                                                                    properties2a.append(prop2a)
                                                                    properties1a.append(prop1a)
                                                                    properties3a.append(prop3a)
                                                                    # if att11 == 'value':
                                                                        
                                                                        
                                                                    valu = getattr(para1,att11)
                                                                        # print(valu)
                                                                        # value11 = getattr(valu,'magnitude')
                                                                        # print(value11)
                                                                    # valu = getattr(para1,'type')
            
                                                                    # valuer = getattr(para,'value')
                                                                       # value11 = getattr(valuer,'magnitude')
                                                                    # print(valuer)
                                                                    try:
                                                                        # print('rohit')
                                                                        shape2 = len(getattr(valu,'shape'))
                                                                        magnitude2 = getattr(valu,'magnitude')
                                                                        units = getattr(valu,'units')
                                                                        unit2 = str(units)
                                                                        # print(properties3a)
                                                                        y1 = BNode()
                                                                        y2 = BNode()
                                                                        y3 = BNode()
                                                                        g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                        g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                        g.add((y2,URIRef(nomad+properties3a[c]),y3))
                                                                        if shape2 >= 1:
                                                                          
                                                                            g.add((y3,URIRef(nomad+'array'),Literal(magnitude2)))
                                                                           
                                                                        elif shape2 == 0:
                                                                          
                                                                            g.add((y3,URIRef(nomad+'numericValue'),Literal(magnitude2)))
                                                                       
                                                                        if unit2 != None:
                                                                           
                                                                            u = 0
                                                                           
                                                                     
                                                                            v = validators.url(qudt_unit + unit2)
                                                                            # print(v)
                                                                            if v == True:
                                                                                g.add((y3, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                                u+=1
                                                                            else:
                                                                                if u<1:
                                                                                    # print('1')
                                                                                    unit2f = unit2.replace(" ","")
                                                                                    if unit2f == '1/meter':
                                                                                        
                                                                                        unit2f = 'ONE-PER-METER'
                                                                                    g.add((y3, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                                    metadata_log = result.section_metadata
                                                                                    if metadata_log != None:   
                                                                                        form_log = getattr(metadata_log,'formula')
                                                                                        calc_log = getattr(metadata_log,'calc_id')
                                                                                       
                                                                                        log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties3a[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '3')
                                                                                                              
                                                               
                                                                          
                                                                        counter000.append(properties3a)
                                                                      
                                                                    except:
                                                                        pass
                                                                    try:
                                                                        if properties3a not in counter000:
                                                                            # print(properties3a)
                                                                            # print('ffhh')
                                                                            # print(properties1)
                                                                            # print('rohit1')
                                                                            shape3 = len(getattr(valu,'shape'))
                                                                            # print(shape3)
                                                                            counter0000.append(properties3a)
                                                                           
                                                                          
                                                                            try:
                                                                                units = getattr(valu,'units')
                                                                                unit3 = str(units)
                                                                                counter0000.append(properties3a)
               
                                                                            except:
                                                                                pass
                                                                            y1 = BNode()
                                                                            y2 = BNode()
                                                                            y3 = BNode()
                                                                            g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                            g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                            g.add((y2,URIRef(nomad+properties3a[c]),y3))
                                                                            if shape3 >= 1:
                                                                              
                                                                                g.add((y3,URIRef(nomad+'array'),Literal(valu)))
                                                                            elif shape3 == 0:
                                                                              
                                                                                g.add((y3,URIRef(nomad+'numericValue'),Literal(valu)))
                                                                            if unit3 != None:
                                                                               
                                                                                u = 0
                                                                               
                                                                        
                                                                                v = validators.url(qudt_unit + unit3)
                                                                                # print(v)
                                                                                if v == True:
                                                                                    g.add((y3, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                                    u+=1
                                                                                else:
                                                                                    if u<1:
                                                                                        # print('2')
                                                                                        unit3f = unit3.replace(" ","")
                                                                                        
                                                                                        g.add((y3, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                                        metadata_log = result.section_metadata
                                                                                        if metadata_log != None:   
                                                                                            form_log = getattr(metadata_log,'formula')
                                                                                            calc_log = getattr(metadata_log,'calc_id')
                                                                                           
                                                                                            log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties3a[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '4')
                                                                          
                                                               
                                                                               
                                                                   
                                                                    except:
                                                                        pass
                                                                    try:
                                                                        
                                                                        if properties3a not in counter000 and properties3a not in counter0000:
                                                                            # print(properties3a)
                                                                            y1 = BNode()
                                                                            y2 = BNode()
                                                                            y3 = BNode()
                                                                            g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                            g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                            g.add((y2,URIRef(nomad+properties3a[c]),Literal(valu)))
                                                                            counter00000.append(properties3a)
                                                                    except:
                                                                        pass
                                                            k+=1
                                        
                                            
                                          
                                            if attt == 'brillouin_zone':
                                                print('yeah_')
                                                
                                                c = 0 
                                                # meta = 0
                                                properties1 = []
                                                properties2 = []
                                                # meta.append(att1)
                                                prop1 = 'has'+ '_' + attt
                                                # print(prop1)
                                                prop2 = 'has'+ '_' + att
                                                
                                                # values = getattr(para,'section_k_band_segment')
                                                val = getattr(para,attt)
                                                # print((val))
                                                properties2.append(prop2)
                                                # print(properties2)
                                                properties1.append(prop1)
                                                check_quantities.append((attt))
                                                print(check_quantities)
                                                print('3')
                                                    
                                                try:
                                                
                                                    for attr, valr in val.__dict__.items():
                                                        
                                                        if not attr.startswith(('m','_')):
                                                            print(attr)
                                                            
                                                            
                                               
                                                            c = 0 
                                                            # meta = 0
                                                            properties1aa = []
                                                            properties2aa = []
                                                            properties3aa = []
                                                            # meta.append(att1)
                                                            prop1aa = 'has'+ '_' + att
                                                            prop2aa = 'has'+ '_' + attt 
                                                            prop3aa = 'has' + '_' + attr
                                                            properties2aa.append(prop2aa)
                                                            properties1aa.append(prop1aa)
                                                            properties3aa.append(prop3aa)
                                                            # if att11 == 'value':
                                                                
                                                                
                                                            valu1 = getattr(val,attr)
                                                            # print(valu1)
                                                                # print(valu)
                                                                # value11 = getattr(valu,'magnitude')
                                                                # print(value11)
                                                            # valu = getattr(para1,'type')
                   
                                                            # valuer = getattr(para,'value')
                                                                # value11 = getattr(valuer,'magnitude')
                                                            # print(valuer)
                                                            try:
                                                                # print('rohit')
                                                                shape2 = len(getattr(valu1,'shape'))
                                                                magnitude2 = getattr(valu1,'magnitude')
                                                                units = getattr(valu1,'units')
                                                                unit2 = str(units)
                                                                
                                                                # print(properties3a)
                                                                y1 = BNode()
                                                                y2 = BNode()
                                                                y3 = BNode()
                                                                g.add((y, URIRef(nomad+properties1aa[c]), y1))
                                                                g.add((y1,URIRef(nomad+properties2aa[c]),y2))
                                                                g.add((y2,URIRef(nomad+properties3aa[c]),y3))
                                                                if shape2 >= 1:
                                                                  
                                                                    g.add((y3,URIRef(nomad+'array'),Literal(magnitude2)))
                                                                   
                                                                elif shape2 == 0:
                                                                  
                                                                    g.add((y3,URIRef(nomad+'numericValue'),Literal(magnitude2)))
                                                               
                                                                if unit2 != None:
                                                                   
                                                                    u = 0
                                                                   
                                                             
                                                                    v = validators.url(qudt_unit + unit2)
                                                                    # print(v)
                                                                    if v == True:
                                                                        g.add((y3, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                        u+=1
                                                                    else:
                                                                        if u<1:
                                                                            print('5')
                                                                            unit2f = unit2.replace(" ","")
                                                                            g.add((y3, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                            metadata_log = result.section_metadata
                                                                            if metadata_log != None:   
                                                                                form_log = getattr(metadata_log,'formula')
                                                                                calc_log = getattr(metadata_log,'calc_id')
                                                                               
                                                                                log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties3aa[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '7')
                                                                                                  
                                                       
                                                                  
                                                                bz.append(properties3aa)
                                                                # print(bz)
                                                              
                                                            except:
                                                                pass
                                                            try:
                                                                if properties3aa not in bz:
                                                                    # print(properties3a)
                                                                    # print('ffhh')
                                                                    # print(properties1)
                                                                    # print('rohit1')
                                                                    shape3 = len(getattr(valu1,'shape'))
                                                                    # print(shape3)
                                                                    bz1.append(properties3aa)
                                                                    # print(bz1)
                                                                   
                                                                  
                                                                    try:
                                                                        units = getattr(valu1,'units')
                                                                        unit3 = str(units)
                                                                        bz1.append(properties3aa)
                   
                                                                    except:
                                                                        pass
                                                                    y1 = BNode()
                                                                    y2 = BNode()
                                                                    y3 = BNode()
                                                                    g.add((y, URIRef(nomad+properties1aa[c]), y1))
                                                                    g.add((y1,URIRef(nomad+properties2aa[c]),y2))
                                                                    g.add((y2,URIRef(nomad+properties3aa[c]),y3))
                                                                    if shape3 >= 1:
                                                                      
                                                                        g.add((y3,URIRef(nomad+'array'),Literal(valu1)))
                                                                    elif shape3 == 0:
                                                                      
                                                                        g.add((y3,URIRef(nomad+'numericValue'),Literal(valu1)))
                                                                    if unit3 != None:
                                                                       
                                                                        u = 0
                                                                       
                                                                
                                                                        v = validators.url(qudt_unit + unit3)
                                                                        # print(v)
                                                                        if v == True:
                                                                            g.add((y3, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                            u+=1
                                                                        else:
                                                                            if u<1:
                                                                                print('6')
                                                                                unit3f = unit3.replace(" ","")
                                                                                g.add((y3, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                                metadata_log = result.section_metadata
                                                                                if metadata_log != None:   
                                                                                    form_log = getattr(metadata_log,'formula')
                                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                                   
                                                                                    log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties3aa[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '8')
                                                                                                      
                                                       
                                                                       
                                                           
                                                            except:
                                                                pass
                                                            try:
                                                                
                                                                if properties3aa not in bz1 and properties3aa not in bz:
                                                                    # print(properties3aa)
                                                                    y1 = BNode()
                                                                    y2 = BNode()
                                                                    y3 = BNode()
                                                                    g.add((y, URIRef(nomad+properties1aa[c]), y1))
                                                                    g.add((y1,URIRef(nomad+properties2aa[c]),y2))
                                                                    g.add((y2,URIRef(nomad+properties3aa[c]),Literal(valu1)))
                                                            except:
                                                                pass
                                                            
                                               
                                                except:
                                                    pass
                                                
                                            if attt not in check_quantities:
                                                # print(properties1)
                                                print('ggfggfgfgfg')
                                                # print(check_quantities)
                                                print(attt)
                                                
                                                c = 0 
                                                # meta = 0
                                                properties1 = []
                                                properties2 = []
                                                # meta.append(att1)
                                                prop1 = 'has'+ '_' + attt
                                                # print(prop1)
                                                prop2 = 'has'+ '_' + att
                                                
                                                # values = getattr(para,'section_k_band_segment')
                                                val = getattr(para,attt)
                                                # print((val))
                                                properties2.append(prop2)
                                                # print(properties2)
                                                properties1.append(prop1)
                                                
                                                
                                                try:
                                                    
                                                    '''for quantity part '''
                                                    
                                                    # print(properties1)
                                                    
                                            
                                                          
                                                    print('rohit')
                                                    shape2 = len(getattr(val,'shape'))
                                                    magnitude2 = getattr(val,'magnitude')
                                                    units = getattr(val,'units')
                                                    unit2 = str(units)
                                                    # print(properties3a)
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
                                                                # print('3')
                                                                unit2f = unit2.replace(" ","")
                                                                #print(unit2)
                                
                                                                if unit2f == '1/meter':
                                                                    
                                                                    unit2f = 'ONE-PER-METER'
                                                                g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                metadata_log = result.section_metadata
                                                                if metadata_log != None:   
                                                                    form_log = getattr(metadata_log,'formula')
                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                   
                                                                    log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '5')
                                                      
                                           
                                                      
                                                    cq.append(properties1)
                                                  
                                                except:
                                                    pass
                                                
                                                try:
                                                    if properties1 not in cq:
                                                        # print(properties3a)
                                                        # print('ffhh')
                                                        # print(properties1)
                                                        # print('rohit1')
                                                        shape3 = len(getattr(val,'shape'))
                                                        # print(shape3)
                                                        cq1.append(properties1)
                                                       
                                                      
                                                        try:
                                                            units = getattr(val,'units')
                                                            unit3 = str(units)
                                                            cq1.append(properties1)
           
                                                        except:
                                                            pass
                                                        y1 = BNode()
                                                        y2 = BNode()
                                                        # y3 = BNode()
                                                        g.add((y, URIRef(nomad+properties2[c]), y1))
                                                        g.add((y1,URIRef(nomad+properties1[c]),y2))
                                                        # g.add((y2,URIRef(nomad+properties3a[c]),y3))
                                                        if shape3 >= 1:
                                                          
                                                            g.add((y2,URIRef(nomad+'array'),Literal(val)))
                                                        elif shape3 == 0:
                                                          
                                                            g.add((y2,URIRef(nomad+'numericValue'),Literal(val)))
                                                        if unit3 != None:
                                                           
                                                            u = 0
                                                           
                                                    
                                                            v = validators.url(qudt_unit + unit3)
                                                            # print(v)
                                                            if v == True:
                                                                g.add((y2, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                u+=1
                                                            else:
                                                                if u<1:
                                                                    print('4')
                                                                    unit3f = unit3.replace(" ","")
                                                                    g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                    metadata_log = result.section_metadata
                                                                    if metadata_log != None:   
                                                                        form_log = getattr(metadata_log,'formula')
                                                                        calc_log = getattr(metadata_log,'calc_id')
                                                                       
                                                                        log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '6')
                                                                              
                                           
                                                           
                                               
                                                except:
                                                    pass
                                                
                                                try:
                                                    
                                                    if properties1 not in cq and properties1 not in cq1:
                                                        if type(properties) in [str,int,float,bool]:
                                                            
                                                            print(properties1)
                                                            y1 = BNode()
                                                            y2 = BNode()
                                                            # y3 = BNode()
                                                            g.add((y, URIRef(nomad+properties2[c]), y1))
                                                            g.add((y1,URIRef(nomad+properties1[c]),Literal(val)))
                                                            cq2.append(properties1)
                                                        # g.add((y2,URIRef(nomad+properties3a[c]),Literal(valu)))
                                                except:
                                                    pass    
                          
                            
                            if att == k_norm:
                              
                                r = 0
                                meta = []
                                properties= []
                                labels=[] 
                                quantities = []
                                    
                                
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
                                # print(observation)
                                # observation = getattr(calc[j],'section_k_band')
                                # for k in observation:
                                #     print(k)
        
                                # observation = getattr(calc[j],'section_k_band_normalized')
                                # print(observation)
        
                                # print(type(observation))
                                
                                
                                y = BNode()
                                o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                # print(str(quantities[q]))
                                o = urllib.parse.quote(o)
                                # print(o)
                                # print(i)
                                # a = 'mat' +str(i+1)
                                m = 'method'+ '_' + formula_name + '_' + pid_name
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + pid_name
                                
                                g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                
                                g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                
                              
                                
                                for para in observation:
                                   
                                
                                    for attt, vatt in para.__dict__.items():
                                    # print(attt)
                                        if not attt.startswith(('m','_')):
                                            # print(attt)
                                            # print(att)
                                            if attt == k_norm_seg:
                                    
                                    
                                                c = 0 
                                                # meta = 0
                                                properties1 = []
                                                properties2 = []
                                                # meta.append(att1)
                                                prop1 = 'has'+ '_' + attt
                                                # print(prop1)
                                                prop2 = 'has'+ '_' + att
                                                
                                                # values = getattr(para,'section_k_band_segment')
                                                val = getattr(para,attt)
                                                # print((val))
                                                properties2.append(prop2)
                                                # print(properties2)
                                                properties1.append(prop1)
                                                # print(properties1)
                                                # value = getattr(para,'reciprocal_cell')
                                                # print(value)
                                                # print(value)
                                                # print(type(value))
                                                
                                                
                                                if type(val) == list:
                                                    
                                                    # print(len(val))
                                                    
                                                    
                                                   
                                                    if (len(val)) > 1:
                                                        # para1 = val
                                                        # for para1 in val:
                                                        #     print(para1)
                                                        # # print(type(para))
                                                       
                                                        k = 0
                                                        for para1 in val:
                                                            # print(para1)
                                                       
                                                            for att11, val1 in para1.__dict__.items():
                                                                if not att11.startswith(('m','_')):
                                                                    # print(att11)
                                                                    c = 0 
                                                                    # meta = 0
                                                                    properties1a = []
                                                                    properties2a = []
                                                                    properties3a = []
                                                                    # meta.append(att1)
                                                                    prop1a = 'has'+ '_' + att
                                                                    prop2a = 'has'+ '_' + attt + str(k)
                                                                    prop3a = 'has' + '_' + att11
                                                                    properties2a.append(prop2a)
                                                                    properties1a.append(prop1a)
                                                                    properties3a.append(prop3a)
                                                                    # if att11 == 'value':
                                                                        
                                                                        
                                                                    valu = getattr(para1,att11)
                                                                        # print(valu)
                                                                        # value11 = getattr(valu,'magnitude')
                                                                        # print(value11)
                                                                    # valu = getattr(para1,'type')
            
                                                                    # valuer = getattr(para,'value')
                                                                       # value11 = getattr(valuer,'magnitude')
                                                                    # print(valuer)
                                                                    try:
                                                                        # print('rohit')
                                                                        shape2 = len(getattr(valu,'shape'))
                                                                        magnitude2 = getattr(valu,'magnitude')
                                                                        units = getattr(valu,'units')
                                                                        unit2 = str(units)
                                                                        # print(properties3a)
                                                                        y1 = BNode()
                                                                        y2 = BNode()
                                                                        y3 = BNode()
                                                                        g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                        g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                        g.add((y2,URIRef(nomad+properties3a[c]),y3))
                                                                        if shape2 >= 1:
                                                                          
                                                                            g.add((y3,URIRef(nomad+'array'),Literal(magnitude2)))
                                                                           
                                                                        elif shape2 == 0:
                                                                          
                                                                            g.add((y3,URIRef(nomad+'numericValue'),Literal(magnitude2)))
                                                                       
                                                                        if unit2 != None:
                                                                           
                                                                            u = 0
                                                                           
                                                                     
                                                                            v = validators.url(qudt_unit + unit2)
                                                                            # print(v)
                                                                            if v == True:
                                                                                g.add((y3, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                                u+=1
                                                                            else:
                                                                                if u<1:
                                                                                    unit2f = unit2.replace(" ","")
                                                                                    g.add((y3, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                                    metadata_log = result.section_metadata
                                                                                    if metadata_log != None:   
                                                                                        form_log = getattr(metadata_log,'formula')
                                                                                        calc_log = getattr(metadata_log,'calc_id')
                                                                                       
                                                                                        log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties3a[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '9')
                                                                          
                                                               
                                                                          
                                                                        counter000.append(properties3a)
                                                                      
                                                                    except:
                                                                        pass
                                                                    try:
                                                                        if properties3a not in counter000:
                                                                            # print(properties3a)
                                                                            # print('ffhh')
                                                                            # print(properties1)
                                                                            # print('rohit1')
                                                                            shape3 = len(getattr(valu,'shape'))
                                                                            # print(shape3)
                                                                            counter0000.append(properties3a)
                                                                           
                                                                          
                                                                            try:
                                                                                units = getattr(valu,'units')
                                                                                unit3 = str(units)
                                                                                counter0000.append(properties3a)
               
                                                                            except:
                                                                                pass
                                                                            y1 = BNode()
                                                                            y2 = BNode()
                                                                            y3 = BNode()
                                                                            g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                            g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                            g.add((y2,URIRef(nomad+properties3a[c]),y3))
                                                                            if shape3 >= 1:
                                                                              
                                                                                g.add((y3,URIRef(nomad+'array'),Literal(valu)))
                                                                            elif shape3 == 0:
                                                                              
                                                                                g.add((y3,URIRef(nomad+'numericValue'),Literal(valu)))
                                                                            if unit3 != None:
                                                                               
                                                                                u = 0
                                                                               
                                                                        
                                                                                v = validators.url(qudt_unit + unit3)
                                                                                # print(v)
                                                                                if v == True:
                                                                                    g.add((y3, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                                    u+=1
                                                                                else:
                                                                                    if u<1:
                                                                                        unit3f = unit3.replace(" ","")
                                                                                        g.add((y3, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                                        metadata_log = result.section_metadata
                                                                                        if metadata_log != None:   
                                                                                            form_log = getattr(metadata_log,'formula')
                                                                                            calc_log = getattr(metadata_log,'calc_id')
                                                                                           
                                                                                            log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties3a[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '10')
                                                                          
                                                               
                                                                               
                                                                   
                                                                    except:
                                                                        pass
                                                                    try:
                                                                        
                                                                        if properties3a not in counter000 and properties3a not in counter0000:
                                                                            # print(properties3a)
                                                                            y1 = BNode()
                                                                            y2 = BNode()
                                                                            y3 = BNode()
                                                                            g.add((y, URIRef(nomad+properties1a[c]), y1))
                                                                            g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                                            g.add((y2,URIRef(nomad+properties3a[c]),Literal(valu)))
                                                                            counter00000.append(properties3a)
                                                                    except:
                                                                        pass
                                                            k+=1
                                    
                                    
                               
                                
                            
                                        
                                    
                            
                            # if k_track == 0 and att != 'section_k_band' and att!= 'section_k_band_normalized': ## other part
                            if att == iteration:
                                
                                r = 0
                           
                                # defining list for saving the attribute names 
                                meta = []
                                properties= []
                                labels=[] 
                                quantities = []
                                
                                meta.append(att)
                                label = meta[r]  + '_' +  'calc'
                                labels.append(label)
                                prop = 'has' + '_' + att
                                # print(prop)
                                properties.append(prop)
                                quantities.append(att)
                                
                                # retrieving attribute values
                                observation = getattr(calc[j],meta[r])
                                
                                # print(counter)
                               
                                if properties not in counter:
                                    
                                    # print('rohit')
                                    
                                    counter1.append(properties)
                                    
                                    y = BNode()
                                    o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                    
                                    # print(str(quantities[q]))
                                    
                                    o = urllib.parse.quote(o)
                                    
                                    # print(o)
                                    # print(i)
                                    # a = 'mat' +str(i+1)
                                    m = 'method'+ '_' + formula_name + '_' + pid_name
                                    # a = 'mat' +str(i+1)
                                    a = 'mat'+ '_' + formula_name + '_' + pid_name
                                    
                                    g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                    g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                    
                                    g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                    g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                    g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                    g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                    
                                   
                                    # print(observation)
                                    if type(observation) == list:
                                        if (len(observation)) > 1:
                                            # print(observation)
                                            k = 0
                                            for para in observation:
                                                # print(para)
                                            
                                                for att1, val1 in para.__dict__.items():
                                                    if not att1.startswith(('m','_','section')):
                                                        # print(att1)
                                                        # print('scf_iteration')
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
                                                                        unit2f = unit2.replace(" ","")
                                                                        g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                        metadata_log = result.section_metadata
                                                                        if metadata_log != None:   
                                                                            form_log = getattr(metadata_log,'formula')
                                                                            calc_log = getattr(metadata_log,'calc_id')
                                                                           
                                                                            log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '11')
                                                               
                                                    
                                                               
                                                
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
                                                                            unit3f = unit3.replace(" ","")
                                                                            g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                            metadata_log = result.section_metadata
                                                                            if metadata_log != None:   
                                                                                form_log = getattr(metadata_log,'formula')
                                                                                calc_log = getattr(metadata_log,'calc_id')
                                                                               
                                                                                log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '12')
                                                                                               
                                                    
                                                                    
                                                        
                                                        except:
                                                            pass
                                                k+=1
                            
                            if att == dos:
                                r = 0
                           
                                # defining list for saving the attribute names 
                                meta = []
                                properties= []
                                labels=[] 
                                quantities = []
                                
                                meta.append(att)
                                label = meta[r]  + '_' +  'calc'
                                labels.append(label)
                                prop = 'has' + '_' + att
                                # print(prop)
                                properties.append(prop)
                                quantities.append(att)
                                
                                # retrieving attribute values
                                observation = getattr(calc[j],meta[r])
                                
                                y = BNode()
                                o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                
                                # print(str(quantities[q]))
                                
                                o = urllib.parse.quote(o)
                                
                                # print(o)
                                # print(i)
                                # a = 'mat' +str(i+1)
                                m = 'method'+ '_' + formula_name + '_' + pid_name
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + pid_name
                                
                                g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                
                                g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                            
                                for para in observation:
                                    # print('th')
                                    for att2,val2 in para.__dict__.items():
                                        if not att2.startswith(('m','_')):
                                            # print(att2)
                                            # print('section_dos')
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
                                            # value = getattr(para,'dos_energies')
                                            # shape = len(getattr(value,'shape'))
                                            # print(shape)
                                            # print('ro')
                                            # mag = getattr(value,'magnitude')
                                            # print(mag)
                                            # print('rh')
                                            # un = getattr(value,'units')
                                            # print(un)
                                            # print('rh1')
                                            # value = getattr(para,'dos_values')
                                            # print(properties1)
                                            
                                            try:
                                                
                                                for att3, val3 in value.__dict__.items():
                                                    if not att3.startswith(('m','_')):
                                                        # print(att3)
                                                        # print(properties1)
                                                        counter2.append(properties1)
                                                        # print(counter2)
                                                        # print('hhhhh')
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
                                               
                                                        
                                            except:
                                                pass
    
                                            # print(value)
                                            try:
                                                if properties1 not in counter2:
                                                    # print(properties1)
                                                    
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
                                                                unit2f = unit2.replace(" ","")
                                                                g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                metadata_log = result.section_metadata
                                                                if metadata_log != None:   
                                                                    form_log = getattr(metadata_log,'formula')
                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                   
                                                                    log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '13')
                                                       
                                            
                                                       
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
                                                                unit3f = unit3.replace(" ","")
                                                                g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                metadata_log = result.section_metadata
                                                                if metadata_log != None:   
                                                                    form_log = getattr(metadata_log,'formula')
                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                   
                                                                    log_one.warning('issue with unit arrangement ' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '14')
                                                   
                                        
                                                                                                            
                                            except:
                                                if properties1 not in counter2 and properties1 not in counter3:
                                                    # print(properties1)
                                                    y1 = BNode()
                                                    g.add((y, URIRef(nomad+properties2[c]), y1))
                                                    g.add((y1,URIRef(nomad+properties1[c]),Literal(value)))
                                                               
                                                                    
                             
                            if att == eigen:
                                # print('heghfghfhf')
                                r = 0
                           
                                # defining list for saving the attribute names 
                                meta = []
                                properties= []
                                labels=[] 
                                quantities = []
                                
                                meta.append(att)
                                label = meta[r]  + '_' +  'calc'
                                labels.append(label)
                                prop = 'has' + '_' + att
                                # print(prop)
                                properties.append(prop)
                                quantities.append(att)
                                
                                # retrieving attribute values
                                observation = getattr(calc[j],meta[r])
                                # print('hhhh')
                                # print(type(observation))
                                
                                # print('hhhhh')
                                y = BNode()
                                o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                
                                # print(str(quantities[q]))
                                
                                o = urllib.parse.quote(o)
                                
                                # print(o)
                                # print(i)
                                # a = 'mat' +str(i+1)
                                
                                m = 'method'+ '_' + formula_name + '_' + pid_name
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + pid_name
                                
                                g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                
                                g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                            
                                for para in observation:
                                    # print('th')
                                    for att2,val2 in para.__dict__.items():
                                        if not att2.startswith(('m','_')):
                                            # print(att2)
                                            # print('section_dos')
                                            
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
                                                        print(value1)
                                                        counter2.append(properties1)
                                                        y1 = BNode()
                                                        y2 = BNode()
                                                       
                                                        g.add((y, URIRef(nomad+properties2[c]), y1))
                                                        g.add((y1, URIRef(nomad+properties1[c]), y2))
                                                        
                                                        g.add((y2,URIRef(nomad+properties3[c]),Literal(value1)))
                                                
                                                        
                                            except:
                                                pass
    
                                            # print(value)
                                            try:
                                                if properties1 not in counter2:
                                                    print(properties1)
                                                    
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
                                                                unit2f = unit2.replace(" ","")
                                                                g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                metadata_log = result.section_metadata
                                                                if metadata_log != None:   
                                                                    form_log = getattr(metadata_log,'formula')
                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                   
                                                                    log_one.warning('issue with unit arrangement ' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '15')
                                                       
                                            
                                                       
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
                                                                unit3f = unit3.replace(" ","")
                                                                g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                metadata_log = result.section_metadata
                                                                if metadata_log != None:   
                                                                    form_log = getattr(metadata_log,'formula')
                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                   
                                                                    log_one.warning('issue with unit arrangement:- ' + ', ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '16')
                                                   
                                        
                                                                                                            
                                            except:
                                                if properties1 not in counter2 and properties1 not in counter3:
                                                    # print(properties1)
                                                    y1 = BNode()
                                                    g.add((y, URIRef(nomad+properties2[c]), y1))
                                                    g.add((y1,URIRef(nomad+properties1[c]),Literal(value)))
                                                               
                            atom = 0                                                                                
                            if att == atom_dos:
                                
                                
                                # r = 0
                           
                                # # defining list for saving the attribute names 
                                # meta = []
                                # properties= []
                                # labels=[] 
                                # quantities = []
                                
                                # meta.append(att)
                                # label = meta[r]  + '_' +  'calc'
                                # labels.append(label)
                                # prop = 'has' + '_' + att
                                # # print(prop)
                                # properties.append(prop)
                                # quantities.append(att)
                                
                                # # retrieving attribute values
                                observation = getattr(calc[j],att)
                                print('hdhgegfgeg')
                                print(len(observation))
                                for l in observation:
                                    for att1, val1 in l.__dict__.items():
                                        # print(att)
                                        # print('hddvvdh')
                                        if not att1.startswith(('m','_')):
                                            atom+=1
                                            print('Annotate me please!')
                                            
                                            
                                if atom == 0:
                                    
                                    
                                    metadata_log = result.section_metadata
                                    if metadata_log != None:   
                                        form_log = getattr(metadata_log,'formula')
                                        calc_log = getattr(metadata_log,'calc_id')
                                    
                                        log_two.warning('empty_attribute:- ' + 'formula:' + form_log  + ', ' + 'calc_id:' + calc_log + ', ' + 'section:' + att )
                                
                            
                            species=0
                            if att == species_dos:
                                # r = 0
                           
                                # # defining list for saving the attribute names 
                                # meta = []
                                # properties= []
                                # labels=[] 
                                # quantities = []
                                
                                # meta.append(att)
                                # label = meta[r]  + '_' +  'calc'
                                # labels.append(label)
                                # prop = 'has' + '_' + att
                                # # print(prop)
                                # properties.append(prop)
                                # quantities.append(att)
                                
                                # # retrieving attribute values
                                observation = getattr(calc[j],att)
                                print('hdhgegfgeg')
                                print(len(observation))
                                for l in observation:
                                    for att1, val1 in l.__dict__.items():
                                        # print(att)
                                        # print('hddvvdh')
                                        if not att1.startswith(('m','_')):
                                            species+=1
                                            print('Annotate me please!')
                                            
                                if species == 0:
                                    print('spec')
                                    metadata_log = result.section_metadata
                                    if metadata_log != None:   
                                        form_log = getattr(metadata_log,'formula')
                                        calc_log = getattr(metadata_log,'calc_id')
                                        log_two.warning('empty_attribute:- ' + 'formula:' + form_log  + ', ' + 'calc_id:' + calc_log + ', ' + 'section:' + att )
                            
                            if att == section_cal:
                                r = 0
                           
                                # defining list for saving the attribute names 
                                meta = []
                                properties= []
                                labels=[] 
                                quantities = []
                                
                                meta.append(att)
                                label = meta[r]  + '_' +  'calc'
                                labels.append(label)
                                prop = 'has' + '_' + att
                                # print(prop)
                                properties.append(prop)
                                quantities.append(att)
                                
                                # retrieving attribute values
                                observation = getattr(calc[j],meta[r])
                                # print(type(observation))
                                
                                y = BNode()
                                o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                
                                # print(str(quantities[q]))
                                
                                o = urllib.parse.quote(o)
                                
                                # print(o)
                                # print(i)
                                # a = 'mat' +str(i+1)
                                # print('rohit')
                                
                                m = 'method'+ '_' + formula_name + '_' + pid_name
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + pid_name
                                g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                
                                g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                                
                                for ob in observation:
                                    
                                
                                    for att1, val1 in ob.__dict__.items():
                                        if not att1.startswith(('m','_','calculation_to_calculation_ref')):
                                            c=0
                                            # pass
                                            # print(att)
                                            properties2 = []
                                            properties1 = []
                                            # meta.append(att1)
                                            # prop3 = 'has'+ '_' + att3
                                            prop2 = 'has'+ '_' + att1
                                            prop1 = 'has'+ '_' + att
                                            properties2.append(prop2)
                                           
                                            properties1.append(prop1)
                                            value1 = getattr(ob,att1)
                                            # print(value1)
                                            y1 = BNode()
                                            y2 = BNode()
                                           
                                            g.add((y, URIRef(nomad+properties1[c]), y1))
                                            g.add((y1, URIRef(nomad+properties2[c]), Literal(value1)))
                                            
                                            # g.add((y2,URIRef(nomad+properties3[c]),Literal(value1)))
                                            
                                            
                            if att == section_ener:
                                
                                r = 0
                           
                                # defining list for saving the attribute names 
                                meta = []
                                properties= []
                                labels=[] 
                                quantities = []
                                
                                meta.append(att)
                                label = meta[r]  + '_' +  'calc'
                                labels.append(label)
                                prop = 'has' + '_' + att
                                # print(prop)
                                properties.append(prop)
                                quantities.append(att)
                                
                                # retrieving attribute values
                                observation = getattr(calc[j],meta[r])
                                print(observation)
                                # print('hhhh')
                                # print(type(observation))
                                
                                # print('hhhhh')
                                y = BNode()
                                o =  'mat' + str(i+1) + 'ob' + str(j) + labels[r] 
                                
                                # print(str(quantities[q]))
                                
                                o = urllib.parse.quote(o)
                                
                                # print(o)
                                # print(i)
                                # a = 'mat' +str(i+1)
                                
                                m = 'method'+ '_' + formula_name + '_' + pid_name
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + pid_name
                                
                                g.add((URIRef(matvoc+o), RDF.type, URIRef(sosa+'Observation')))
                                g.add((URIRef(matvoc+o), URIRef(sosa + 'hasfeatureOfInterest'), URIRef(matvoc+a)))
                
                                g.add((URIRef(matvoc+o), URIRef(sosa+'hasResult'), y))
                                g.add((y, RDFS.label, Literal(labels[r],lang='en')))
                                g.add((y, URIRef(dc+'title'), Literal(quantities[r],lang='en')))
                                g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                            
                                for para in observation:
                                    # print('th')
                                    for att2,val2 in para.__dict__.items():
                                        if not att2.startswith(('m','_')):
                                            # print(att2)
                                            # print('section_dos')
                                            
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
                                                        print(value1)
                                                        counter2.append(properties1)
                                                        y1 = BNode()
                                                        y2 = BNode()
                                                       
                                                        g.add((y, URIRef(nomad+properties2[c]), y1))
                                                        g.add((y1, URIRef(nomad+properties1[c]), y2))
                                                        
                                                        g.add((y2,URIRef(nomad+properties3[c]),Literal(value1)))
                                                
                                                        
                                            except:
                                                pass
    
                                            # print(value)
                                            try:
                                                if properties1 not in counter2:
                                                    print(properties1)
                                                    
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
                                                                unit2f = unit2.replace(" ","")
                                                                g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit2f)))
                                                                metadata_log = result.section_metadata
                                                                if metadata_log != None:   
                                                                    form_log = getattr(metadata_log,'formula')
                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                   
                                                                    log_one.warning('issue with unit arrangement ' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '17')
                                                       
                                            
                                                       
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
                                                                unit3f = unit3.replace(" ","")
                                                                g.add((y2, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                metadata_log = result.section_metadata
                                                                if metadata_log != None:   
                                                                    form_log = getattr(metadata_log,'formula')
                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                   
                                                                    log_one.warning('issue with unit arrangement:- ' + ', ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties1[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '18')
                                                   
                                        
                                                                                                            
                                            except:
                                                if properties1 not in counter2 and properties1 not in counter3:
                                                    # print(properties1)
                                                    y1 = BNode()
                                                    g.add((y, URIRef(nomad+properties2[c]), y1))
                                                    g.add((y1,URIRef(nomad+properties1[c]),Literal(value)))
                                                    
                        
                            logging.shutdown()   
        
            with open('un.txt', "wb") as fp:   
                pickle.dump(un, fp)
    
                                        
            g.serialize('obser_v1_' + str(i) + '.ttl', format='turtle')
            # print('saved')
            # print('enter_repo' + str(i))
            
            start = time.time()
            
            headers = {
                    'Content-Type': 'application/x-turtle',
                }
                
            # data = g.serialize(format='turtle').decode('UTF-8')
            response = requests.post('http://localhost:7200/repositories/Nomad/statements', data=open('obser_v1_' + str(i) + '.ttl','r').read().encode('utf-8'), headers=headers)
            # print(response)
            # print('done_repo' + str(i))
            end = time.time()
            tot = end - start
            total = total + tot 
            # print(total)
     
        else:
            break
    
# logging.shutdown()   

print('observation_success')
                                 
                                   
       

                    
                                    
                            
                           
# g.serialize(r'C:\Users\GuptaR\Desktop\confi\obser_v1.ttl', format='turtle')                                          
                   


                                        



