# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:02:02 2021

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
import re

from nomad.client import ArchiveQuery
from nomad.metainfo import units


from nomad import client, config

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


results = ArchiveQuery(
    # url='http://nomad-lab.eu/prod/rae/beta/api',
  
    required={
        'section_run': '*',
        'section_workflow': '*',
        'section_metadata': '*'
            },
    max=None)

print(results)

print('initializing_metadata_repo')

''' creating rdf graphs '''


import rdflib
import requests
import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SKOS, RDF, RDFS, OWL, DC, DCTERMS, VOID, DOAP #most common namespaces
# import urllib.parse #for parsing strings to URI's



'''Initializing Graph'''



    
''' creating rdf's using ssn ontology'''
    



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


''' defining feature of Interest '''           




''' defining sample and metadata related to materials '''


for i, result in enumerate(results):
    if i not in un:
        un.append(i)
        # print(i)
    
        if i <length:
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
            matvoc = Namespace('http://stream-ontology.com/matvoc-core/')
            
            
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
            
            g.add((URIRef(matvoc+'mat'+'_'+ formula_name), RDF.type, URIRef(sosa+'FeatureOfInterest')))
            g.add((URIRef(matvoc+'mat'+'_'+ formula_name), RDFS.label, Literal('calculating energy levels of materials',lang ='en')))
            # a = 'mat'+str(i+1)
            a = 'mat'+ '_' + formula_name + '_' + pid_name
            g.add((URIRef(matvoc+'mat'+'_'+ formula_name), URIRef(sosa+'hasSample'), URIRef(matvoc + a)))

            formula1 = []
            try1 = 0
            metadata = result.section_metadata
            # print(metadata)
            
            if metadata != None:        
                for att, value in (metadata.__dict__.items()): 
                    
                    
                    if not att.startswith(('m_','a_','mainfile','dft','encyclopedia','files','uploader','coauthors')):
                        
                        
                        c=0
                        meta = []
                        properties = []
                        meta.append(att)
                        prop = 'has' + '_' + meta[c]
                        properties.append(prop)
                        # print(properties[c])
                        # print(meta[c])
                        meta_data = getattr(metadata,meta[c])
                        # print(meta_data)
                        # a = 'mat'+str(i+1)
                        # m = 'method' +str(i+1)
                        m = 'method'+ '_' + formula_name + '_' + pid_name
                        # a = 'mat' +str(i+1)
                        a = 'mat'+ '_' + formula_name + '_' + pid_name
                        if meta_data !=None:
                        
                            t = BNode()
                            t1 = BNode()
            
                            g.add((URIRef(matvoc+a), RDF.type, URIRef(sosa + 'Sample')))
                            g.add((URIRef(matvoc+a),URIRef(nomad+'has_dcat_metadata'),URIRef(str('https://nomad-lab.eu/prod/rae/dcat/datasets/')+str(pid_name))))
                            g.add((URIRef(matvoc+a), RDFS.label, Literal('material',lang='en')))
            
                            if meta[c] == 'comment' :
                                g.add((URIRef(matvoc+a), RDFS.comment, Literal(meta_data,lang='en')))
                            
                            
                            elif meta[c] == 'upload_time':
                                
                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), t))
                                g.add((t, RDF.type, URIRef(time1 + 'Instant')))
                                g.add((t, URIRef(time1 + 'inXSDDateTime'), Literal(meta_data,datatype=XSD.dateTime)))
                
                            
                            elif meta[c] == 'last_processing':
                                
                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), t1))
                                g.add((t1, RDF.type, URIRef(time1 + 'Instant')))
                                g.add((t1, URIRef(time1 + 'inXSDDateTime'), Literal(meta_data,datatype=XSD.dateTime)))  
                                
                            elif att == "formula":
                                s  = re.split("[^a-zA-Z]*", meta_data)
                                s = [x for x in s if x]
                                s = sorted(c for c in s if c.isupper())
                                # print(s)
                                
                                # print(form1)
                                if meta_data.startswith((s[0])) and len(formula1) == 0:
                                    # ur_id = meta_data
                                    # print(ur_id)
                                    formula1.append(meta_data)
                                # form = sorted(meta_data)
                                # form1 = "".join(form)
                                # if meta_data not in formula:
                                    # formula.append(form1)
                                    # print(meta_data)
                                    # print('1')
                                    # f = meta_data[-3:] 
                                    g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), URIRef(matvoc+meta_data)))
                                    g.add((URIRef(matvoc+meta_data), RDF.type, URIRef(matvoc+'Formula')))
                                    g.add((URIRef(matvoc+meta_data), RDFS.label, Literal(meta_data)))
                                    # ur_id = meta_data
                                else:
                                    # print('2')
                                    # ur_id = meta_mat
                                    # f = meta_data[-3:]
                                    g.add((URIRef(matvoc+formula1[0]), RDF.type, URIRef(matvoc+'Formula')))
                                    g.add((URIRef(matvoc+formula1[0]), RDFS.label, Literal(meta_data)))

                 
                            else: # properties[c] != 'has_comment' and 'has_upload_time':
                                
                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), Literal(meta_data)))
                                
                            # print(ur_id)
                            
                for att, value in (metadata.__dict__.items()):    
                    # print(formula)

                    
                    # if try1==1:
                    if att.startswith(('encyclopedia')):
                        # print(att)                
                        # print(properties[m])
                        # print(meta[m])
                        meta_data1 = getattr(metadata,att)
                        
                       
                       
                        counter=[]
                        counter1=[]
                        counter2=[]
                        counter3=[]
                        if meta_data1 !=None:
                            
                            
                            try:
                                
                                for att, value in meta_data1.__dict__.items():
                                    if att.startswith(('material','properties')):
                                        if att == 'material':
                                            meta_enc = getattr(meta_data1,att)
                                            if meta_enc !=None:
                                            
                                                for att, value in meta_enc.__dict__.items():
                                                    
                                                    
                                                    if not att.startswith(('m_')):
                                                        # print(att)
                                                        c=0
                                                        meta1 = []
                                                        properties = []
                                                        meta1.append(att)
                                                        meta_mat = getattr(meta_enc,meta1[c])
                                                        prop = 'has' + '_' + meta1[c]
                                                        properties.append(prop)  
                                                        # print(meta_mat)
                                                        # print(properties[c])
                                                        # a = 'mat' + str(i+1)  
                                                        # m = 'method' +str(i+1)
                                                        m = 'method'+ '_' + formula_name + '_' + pid_name
                                                        # a = 'mat' +str(i+1)
                                                        a = 'mat'+ '_' + formula_name + '_' + pid_name
                                                        
                                                        m_list =[]
                                                       
                                                        try:
                    
                                                            if att == "formula":
                                                                print(att)
                                                                s  = re.split("[^a-zA-Z]*", meta_mat)
                                                                print(s)
                                                                s = [x for x in s if x]
                                                                s = sorted(c for c in s if c.isupper())
                                                                print(meta_mat)
                                                                # print(s[0])
                                                                
                                                                # print(form1)
                                                                if meta_mat.startswith((s[0])) and len(formula1) == 0:
                                                                    ur_id = meta_mat
                                                                    print('hhhhh')
                                                                    formula1.append(meta_mat)
                                                                    # f = meta_mat[-3:]
                                                                    # print(f)
                                                                    print('3')
                                                                    g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), URIRef(matvoc+meta_mat)))
                                                                    g.add((URIRef(matvoc+meta_mat), RDF.type, URIRef(matvoc+'Formula')))
                                                                    g.add((URIRef(matvoc+meta_mat), RDFS.label, Literal(meta_mat)))
                                                                else:
                                                                    print('4')
                                                                    
                                                                    # print(ur_id)
                                                                    # f = meta_mat[-3:]
                                                                    g.add((URIRef(matvoc+formula1[0]), RDF.type, URIRef(matvoc+'Formula')))
                                                                    g.add((URIRef(matvoc+formula1[0]), RDFS.label, Literal(meta_mat)))
                                                                    # formulas.append(meta_mat)
                                                                    # print(formulas)
                                                                
                                                                    # print(meta_mat)
                                                                    
                                                            elif meta_mat.isalpha():
                                                                print('trtr')
                                                                print(meta_mat)
                                                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), Literal(meta_mat)))
                                                            
                                                            else:
                                                                    
                                                                print('dddd')
                                                                print(meta_mat)
                                                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), Literal(meta_mat)))
                                                                # print('ro')
                                                                # print(meta_mat)
                                                                m_list.append(meta_mat)                                               
                                                        except:
                                                            if meta_mat not in m_list:
                                                                if meta1[c].startswith(('bulk')):
                                                                    
                                                                    for att0, val0 in meta_mat.__dict__.items():
                                                                        if not att0.startswith(('m','_')):
                                                                            # print(att0)
                                                                            c0 = 0
                                                                            meta0 = []
                                                                            properties0=[]
                                                                            meta0.append(att0)
                                                                            meta_mat_v = getattr(meta_mat,meta0[c0])
                                                                            prop0 = 'has'+'_' + meta0[c0]
                                                                            properties0.append(prop0)
                                                                            # meta_mat_v = getattr(meta_mat,'lattice_parameter')
            
                                                                           
                                                                            
                                                                            ma =BNode()
                                                                            g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), ma))
                                                                            g.add((ma, URIRef(nomad+properties0[c0]), Literal(meta_mat_v)))
                                                              
                                                                if meta1[c].startswith(('idealized_structure')):
                                                                    
                                                                    for att00, val00 in meta_mat.__dict__.items():
                                                                        
                                                                        if not att00.startswith(('m','_')):
                                                                            c00 = 0
                                                                            meta00 = []
                                                                            properties00=[]
                                                                            meta00.append(att00)
                                                                            Is = getattr(meta_mat,meta00[c00])
                                                                            prop00 = 'has'+'_' + meta00[c00]
                                                                            properties00.append(prop00)
                                                                            print('hdhd')
                                                                            print(properties00)
                                                                            # if type(la) == list:
                                                                            #     for x in la:
                                                                            #         la1 = x
                                                                            # else:
                                                                            #     la1 = la
                                                                            # print(la1)
                                                                            try:
                                                                                shape = len(getattr(Is,'shape'))
                                                                                magnitude = getattr(Is,'magnitude')
                                                                                units = getattr(Is,'units')
                                                                                unit = str(units)
                                                                                counter.append(properties00)
                                                                                # print(unit)
                                                                                ma =BNode()
                                                                                ma1 = BNode()
                                                                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), ma))
                                                                                if shape >=1:
                                                                                    g.add((ma, URIRef(nomad+properties00[c00]), ma1))
                                                                                    g.add((ma1, URIRef(nomad+'array'), Literal(magnitude)))
                                                                                elif shape == 0:
                                                                                    g.add((ma, URIRef(nomad+properties00[c00]), ma1))
                                                                                    g.add((ma1, URIRef(nomad+'numericValue'), Literal(magnitude)))
                                                                                if unit !=None: 
        
                                                                                    
                                                                                    u = 0
                                                                               
                                                                                    v = validators.url(qudt_unit + unit)
                                                                                    if v == True:
                                                                                        g.add((ma1, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit)))
                                                                                        u+=1
                                                                                    else:
                                                                                          if u<1:
                                                                                              unitf = unit.replace(" ","")
                                                                                              # print(unit)
                                                                                              print('1')
                                                                                              if unitf == 'meter**3':
                                                                                                  unitf = 'M3'
                                                                                                # ab1 = urllib.parse.quote(ab)
                                                                                          
                                                                                              g.add((ma1, URIRef(qudt + 'unit'), URIRef(ab+unitf)))
                                                                                              metadata_log = result.section_metadata
                                                                                              if metadata_log != None:   
                                                                                                  
                                                                                                  
                                                                                                  form_log = getattr(metadata_log,'formula')
                                                                                                  print(form_log)
                                                                                                  calc_log = getattr(metadata_log,'calc_id')
                                                                                                  print(calc_log)
                                                                                                  log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties00[c00] + ', ' + 'unit:' + unit + ', ' + 'c_unit:' + unitf + ', ' + 'check:' + '1')
                                                                                              
                                                                                              # g.add((ma1, URIRef(qudt + 'unit'), Literal(unit)))
                                                                                        # print('go_on')
                                                                                   
                                                                
                            
                                         
                                                    
                                                                                       
        
                                                                                    
                                                                             
                                                                                
                                                                            except:
                                                                                pass    
                                                                            
                                                                            try:
                                                                                if properties00 not in counter:
                                                                                    print('try')
                                                                                    print(properties00)
                                                                                    shape1 = len(getattr(Is,'shape'))
                                                                                    counter1.append(properties00)
                                                                                    
                                                                                    try:
                                                                                        units = getattr(Is,'units')
                                                                                        unit1 = str(units)
                                                                                        counter1.append(properties00)
                                                                                    except:
                                                                                        pass
                                                                                    ma =BNode()
                                                                                    ma1 = BNode()
                                                                                    g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), ma))
                                                                                    if shape >=1:
                                                                                        g.add((ma, URIRef(nomad+properties00[c00]), ma1))
                                                                                        g.add((ma1, URIRef(nomad+'array'), Literal(Is)))
                                                                                    elif shape == 0:
                                                                                        g.add((ma, URIRef(nomad+properties00[c00]), ma1))
                                                                                        g.add((ma1, URIRef(nomad+'numericValue'), Literal(Is)))
                                                                                    if unit1 !=None:  
                                                                                        
                                                                                        u = 0
                                                                                        v = validators.url(qudt_unit + unit1)
                                                                                        if v == True:
                                                                                            
                                                                                             
                                                                                            g.add((ma1, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit1)))
                                                                                            u+=1
                                                                     
                                                                                        else:
                                                                                            
                                                                                            
                                                                                            
                                                                                            if u<1:
                                                                                                unit1f = unit1.replace(" ","")
                                                                                                g.add((ma1, URIRef(qudt + 'unit'), URIRef(ab+unit1f)))
                                                                                                metadata_log = result.section_metadata
                                                                                                if metadata_log != None:   
                                                                                                    
                                                                                                    form_log = getattr(metadata_log,'formula')
                                                                                                    calc_log = getattr(metadata_log,'calc_id')
                                                                                                    log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties00[c00] + ', ' + 'unit:' + unit1 + ', ' + 'c_unit:' + unit1f + ', ' + 'check:' + '2')
                                                                                         
                                                                                    
                                                                                    
                                                                            except:
                                                                                
                                                                                
                                                                                if properties00 not in counter and properties00 not in counter1:
                                                                                    # print(properties00)
                                                                                    
                                                                                    
                                                                                            
                                                                                    if type(Is) == list:
                                                                                        k =0
                                                                                        for x in Is:
                                                                                            # print(x)
                                                                                            try:
                                                                                                
                                                                                                
                                                                                                for att000,va000 in x.__dict__.items():
                                                                                                    if not att000.startswith(('m','_','variables')):
                                                                                                        # print(att000)
                                                                                                        c000 = 0
                                                                                                        c00 = 0
                                                                                                        meta000 = []
                                                                                                        properties000 = []
                                                                                                        properties00 = []
                                                                                                        meta000.append(att000)
                                                                                                       
                                                                                                        
                                                                                                        
                                                                                                        va = getattr(x,att000)
                                                                                                        # print(va)
                                                                                                        prop00 = 'has'+ '_'+att00 + str(k)
                                                                                                        # print(prop00)
                                                                                                        prop000 = 'has'+'_'+ att000 
                                                                                                        properties00.append(prop00)
                                                                                                        # print(properties00)
                                                                                                        properties000.append(prop000) 
                                                                                                        ma1 =BNode()
                                                                                                        ma2 = BNode()
        
                                                                                                        g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), ma1))
                                                                                                        g.add((ma1, URIRef(nomad + properties00[c00]), ma2))
        
                                                                                                        g.add((ma2, URIRef(nomad+properties000[c000]), Literal(va)))
                                                                                                        counter2.append(properties00)
                                                                                                        print('try1')
                                                                                                        print(properties00)
        
        
                                                                                            except:
                                                                                                pass
                                                                                            
                                                                                            k+=1
                                                                                    
                                                                                    if type(Is) in [int,str,float,list]:
                                                                                        if properties00 not in counter2 and properties00 not in counter1 and properties00 not in counter :
                                                                                            print('try2')
                                                                                            print(properties00)
                                                                                            ma =BNode()
            
                                                                                            g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), ma))
                                                                                            g.add((ma, URIRef(nomad+properties00[c00]), Literal(Is)))
                                                                                            counter3.append(properties00)
                                                                                    else:
                                                                                        if properties00 not in counter2 and properties00 not in counter3 and properties00 not in counter1 and properties00 not in counter :
                                                                                            print('try3')
                                                                                            print(properties00)
                                                                                            
                                                                                            for a3,v3 in Is.__dict__.items():
                                                                                                if not a3.startswith(('m','_')):
                                                                                                    # print(a3)
                                                                                                    c0000 = 0
                                                                                                    c00 = 0
                                                                                                    meta0000 = []
                                                                                                    properties0000 = []
                                                                                                    properties00 = []
                                                                                                    meta0000.append(a3)
                                                                                                   
                                                                                                    
                                                                                                    
                                                                                                    va1 = getattr(Is,a3)
                                                                                                    # print(va)
                                                                                                    prop00 = 'has'+ '_'+att00
                                                                                                    # print(prop00)
                                                                                                    prop0000 = 'has'+'_'+ a3 
                                                                                                    properties00.append(prop00)
                                                                                                    # print(properties00)
                                                                                                    properties0000.append(prop0000) 
                                                                                                    ma1 =BNode()
                                                                                                    ma2 = BNode()
        
                                                                                                    g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), ma1))
                                                                                                    g.add((ma1, URIRef(nomad + properties00[c00]), ma2))
        
                                                                                                    g.add((ma2, URIRef(nomad+properties0000[c0000]), Literal(va1)))
                                                                                            
                                                                                        
        
        
                                                                                    
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                    
                                                        g.add((URIRef(matvoc+a), URIRef(sosa + 'isSampleOf'), URIRef(matvoc+'mat'+'_'+ formula_name)))
                                                        g.add((URIRef(matvoc+a), URIRef(sosa + 'isResultOf'), URIRef(matvoc + m)))
                                    
                                        if att == 'properties':  
                
                                            meta_enc = getattr(meta_data,att)
                                            # print(meta_enc)
                                            if meta_enc != None:
                                                for att1, value in meta_enc.__dict__.items():
                                                    # print(att1)
                                                    
                                                    if not att1.startswith(('m_','electronic','energies')):
                                                        
                                                        # print(att1)
                                                        
                                                        c=0
                                                        meta2 = []
                                                        properties = []
                                                        meta2.append(att1)
                                                        
                                                            
                                                        meta_mat1 = getattr(meta_enc,meta2[c])
                                                        # meta_mat1 = getattr(meta_enc,'atomic_density')
                                                        # meta_mat1 = getattr(meta_mat1,'magnitude')
            
            
                                                        # print(meta_mat1)
                                                        
                                                        prop = 'has' + '_' + meta2[c]
                                                        
                                                        properties.append(prop) 
                                                        # print(meta2[c])
                                                        # print(meta_mat1)
                                                        
                                                        m = 'method'+ '_' + formula_name + '_' + pid_name
                                                        # a = 'mat' +str(i+1)
                                                        a = 'mat'+ '_' + formula_name + '_' + pid_name
                                                        
                                                        # a = 'mat' + str(i+1)   
                                                        hasprop = 'has' + '_' + att1 
                                                        elec = []
                                                        
                                                        try:
                                                            shape2 = len(getattr(meta_mat1,'shape'))
                                                            
                                                            magnitude2 = getattr(meta_mat1,'magnitude')
                                                            units = getattr(meta_mat1,'units')
                                                            unit2 = str(units)
                                                            elec.append(properties)
            
                                                            p = BNode()
                                                            if shape2 >= 1:
                                                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), p))
                                                                g.add((p, URIRef(nomad + 'array'), Literal(magnitude2)))
            
                                                            elif shape2 == 0:
                                                                
                                                               
                                                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), p))
                                                                g.add((p, URIRef(nomad + 'numericValue'), Literal(magnitude2)))
                                                            if unit2 !=None:  
                                                                    u = 0
                                                                    
                                                                        
                                                                    
                                                                    v = validators.url(qudt_unit + unit2)
                                                                    if v == True:
                                                                                            
                                                                        g.add((p, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit2)))
                                                                        u+=1
                                                                    else:
                                                                          if u<1:
                                                                              
                                                                              
                                                                              unit2f = unit2.replace(" ","")
                                                                              if unit2f == '1/meter**3':
                                                                                  unit2f = "ONE-PER-M3"
                                                                                  # g.add((p, URIRef(qudt + 'unit'), URIRef(ab + unit2)))
                                                                              if unit2f == 'kilogram/meter**3':
                                                                                  # print(unit2)
                                                                                  unit2f = 'KG-PER-M3'
                                                                                  # g.add((p, URIRef(qudt + 'unit'), URIRef(ab + unit2)))
                                                                              
                                                                              
                                                                              # print(unit2)
                                                                              g.add((p, URIRef(qudt + 'unit'), URIRef(ab + unit2f)))
                                                                              metadata_log = result.section_metadata
                                                                              if metadata_log != None:   
                                                                                  
                                                                                  form_log = getattr(metadata_log,'formula')
                                                                                  calc_log = getattr(metadata_log,'calc_id')
                                                                                  log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '3')
                                                                              # g.add((p, URIRef(qudt + 'unit'), Literal(unit2)))
                                                                        
                                                                    
                                                                        # if u<1:
                                                                        #     g.add((p, URIRef(qudt + 'unit'), Literal(unit2)))
                                      
                                                            # elec.append(meta_mat1)
                                                                  
                                                        
                                                        except:
                                                            pass
                                                        try:
                                                            if properties not in elec:
                                                                shape3 = len(getattr(meta_mat1,'shape'))
                                                                elec.append(properties)
                                                                try:
                                                                    units = getattr(meta_mat1,'units')
                                                                    unit3 = str(units)
                                                                    elec.append(properties)
                                                                except:
                                                                    pass
                                                                
                                                            p = BNode()
                                                            if shape3 >= 1:
                                                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), p))
                                                                g.add((p, URIRef(nomad + 'array'), Literal(meta_mat1)))
                                                            
                                                            
                                                            elif shape3 == 0:
                                                                
                                                               
                                                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), p))
                                                                g.add((p, URIRef(nomad + 'numericValue'), Literal(meta_mat1)))
                                                            if unit3 !=None:  
                                                                    u = 0
                                                                    
                                                                        
                                                                    
                                                                    v = validators.url(qudt_unit + unit3)
                                                                    if v == True:
                                                                                            
                                                                        g.add((p, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit3)))
                                                                        u+=1
                                                                    else:
                                                                        if u<1:
                                                                            unit3f = unit3.replace(" ","")
                                                                            g.add((p, URIRef(qudt + 'unit'), URIRef(ab+unit3f)))
                                                                            metadata_log = result.section_metadata
                                                                            if metadata_log != None:   
                                                                                
                                                                                form_log = getattr(metadata_log,'formula')
                                                                                calc_log = getattr(metadata_log,'calc_id')
                                                                                log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '4')
                                                            
                                                                            
                                                                        
                                                              
                                                            
                                                                      
                                                        except:
                                                            if properties not in elec:
                                                                # print(properties)
                                                                g.add((URIRef(matvoc+a), URIRef(nomad + properties[c]), Literal(meta_mat1)))

                                                                  
                                                            
                            except:
                                pass                        
                                                
                                             
                                     
                   
    
            system = result.section_run[0].section_system[:]
            # print(type(system))
            if system != None:
                
                
            
                for j in range(len(system)):
                    # print(j)
                    u = system[j]
                    # print(u)
                    
                    l1 = []
                    l2 = []
                    
                    for att, value in u.__dict__.items():
                        if not att.startswith(('m','_','section')):
                            # print(att)
                            c = 0
                            meta = []
                            properties = []
                            meta.append(att)
                            prop = 'has' + '_' + meta[c] 
                            properties.append(prop)
                            method = getattr(system[j],meta[c])
                            # method = getattr(system[j],'section_symmetry')
                            # method = getattr(system[j],'atom_labels')
        
                            # method = getattr(method,'shape')
        
                            type((method))
        
                          
                            X1 = []
                            if type(method) == list:
                                for x in method:
                                    if (type(x)) in [str, int, complex, float, bool, list]:
                                        
                                        X1.append(x)
                                    else:
                                        X1 = x
                            else:
                                X1 = method
                            
            
                            
                            
                            
            
                            try:
            
                                y = BNode()
                                
                                shape = len(getattr(X1,'shape'))
            
                                # print(shape)
                                
                                try:
                                    magnitude = getattr(X1,'magnitude')
                                
                                except:
                                    pass
                                
                                try:
                                    
                                    units = getattr(X1,'units')
                                    unit = str(units)
                                
                                except:
                                    pass
                                
                                # print(unit)
                                
                                # m = 'method' +str(i+1)
                                # a = 'mat' +str(i+1)
                                m = 'method'+ '_' + formula_name + '_' + pid_name
                                # a = 'mat' +str(i+1)
                                a = 'mat'+ '_' + formula_name + '_' + pid_name
                                # section = 'calculation_number' + '_' + str(j)
                                section = 'section_system' + '_' + str(j)

                                
                                g.add((URIRef(matvoc+a), RDF.type, URIRef(sosa + 'Sample')))
                                s = BNode()
                                g.add((URIRef(matvoc+a), URIRef(matvoc + section), s))
                                g.add((s, URIRef(nomad + properties[c]), y))
        
                                
                                           
                                
                                if shape >= 1:
                                    
                                    g.add((y, URIRef(nomad + 'array'), Literal(magnitude)))                
                                
                                elif shape == 0:
                                    
                                    g.add((y, URIRef(nomad + 'numericalValue'), Literal(magnitude))) 
                            
                                
                                    
                                    
                                if unit !=None:     
                                    
                                    u = 0
                                    v = validators.url(qudt_unit + unit)
                                    if v == True:
                                        g.add((y, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit)))
                                        u +=1
                
                                    else:
                                        
                                        if u<1:
                                            unitf = unit.replace(" ","")
                                            g.add((y, URIRef(qudt + 'unit'), URIRef(ab+unitf)))
                                            metadata_log = result.section_metadata
                                            if metadata_log != None:   
                                                
                                                form_log = getattr(metadata_log,'formula')
                                                calc_log = getattr(metadata_log,'calc_id')
                                                log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties[c] + ', ' + 'unit:' + unit + ', ' + 'c_unit:' + unitf + ', ' + 'check:' + '5')
                                
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
                                        # print(unit1)
                                        l2.append(properties[c])
                                    
                                    
                                    except:
                                        pass
                                    
                                    
                                    # m = 'method' +str(i+1)
                                    # a = 'mat' +str(i+1)
                                    m = 'method'+ '_' + formula_name + '_' + pid_name
                                    # a = 'mat' +str(i+1)
                                    a = 'mat'+ '_' + formula_name + '_' + pid_name
                                    g.add((URIRef(matvoc+a), RDF.type, URIRef(sosa + 'Sample')))
                                    s = BNode()
                                    g.add((URIRef(matvoc+a), URIRef(matvoc + section), s))
                                    # g.add((URIRef(matvoc+a), URIRef(matvoc + 'Calculaton_number'), Literal(str(j))))
                                    
                                    y1 = BNode()
                                    
                                    if shape1 >= 1 :
                                        g.add((s, URIRef(nomad+properties[c]), y1))
                                        g.add((y1, URIRef(nomad+'array'), Literal(X1)))
                                    
                                    elif shape == 0:
                                        g.add((s, URIRef(nomad+properties[c]), y1))
                                        g.add((y1, URIRef(nomad+'numericalValue'), Literal(X1)))
                                        
                                    if unit1 != None:
                                        u = 0
                                        
                                        v = validators.url(qudt_unit + unit1)
                                        if v == True:
                                            g.add((y1, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit1)))
                                            u +=1
                    
                                        else:
                                            
                                            if u<1:
                                                unit1f = unit1.replace(" ","")
                                                g.add((y1, URIRef(qudt + 'unit'), URIRef(ab+unit1f)))
                                                metadata_log = result.section_metadata
                                                if metadata_log != None:   
                                                    
                                                    form_log = getattr(metadata_log,'formula')
                                                    calc_log = getattr(metadata_log,'calc_id')
                                                    log_one.warning('issue with unit arrangement' + ' ' + 'formula:' + form_log + ' ' + 'calc_id:' + calc_log + ' ' + 'prop:' + properties[c] + ', ' + 'unit:' + unit1 + ', ' + 'c_unit:' + unit1f + ', ' + 'check:' + '6')
                            
                                    # l2.append(properties[c])                    
                            
                            except:
                                
                                
                                if properties[c] not in l1 and  properties[c] not in l2:
                                    # print(properties[c])
                                    # m = 'method' +str(i+1)
                                    # a = 'mat' +str(i+1)
                                    m = 'method'+ '_' + formula_name + '_' + pid_name
                                    # a = 'mat' +str(i+1)
                                    a = 'mat'+ '_' + formula_name + '_' + pid_name
                                    # section = 'calculation_number' + '_' + str(j)
                                    section = 'section_system' + '_' + str(j)
                                    s = BNode()
                                    g.add((URIRef(matvoc+a), URIRef(matvoc + section), s))
                                    
                                    # print('here')
                                    
                                    # print(X1)
                                    
                                    if type(X1) in [str,int,complex,float,bool,list]:
                                        g.add((s, URIRef(nomad+properties[c]), Literal(X1)))
                                    
                                    else:
                                        pass
                                        
                                        
                                        # y2 = BNode()
                                        
                                        # g.add((s, URIRef(nomad+properties[c]), y2))
                                        # g.add((y2, URIRef(matvoc+'refernce'), Literal('https://nomad-lab.eu/prod/rae/gui/search')))
                                else:
                                    pass
                                
            counter000 = []
            counter0000 = []
            counter00000 = []
            topology = result.section_run[0].section_topology[:]
            # print(topology)
            if topology != None:
                for j in range(len(topology)):
                    # print(j)
                    u = topology[j]
                    
                    for att, val in u.__dict__.items():
                        # print(att)
                        if not att.startswith(('m','_')):
                            
                            c = 0 
                            # meta = 0
                            properties1 = []
                            # meta.append(att1)
                            prop1 = 'has'+ '_' + att
                            # print(prop1)
                            
                            # values = getattr(para,'section_k_band_segment')
                            val = getattr(u,att)
                            print((type(val)))
                         
                            properties1.append(prop1)
                            
                            # m = 'method' +str(i+1)
                            # a = 'mat' +str(i+1)
                            
                            m = 'method'+ '_' + formula_name + '_' + pid_name
                            # a = 'mat' +str(i+1)
                            a = 'mat'+ '_' + formula_name + '_' + pid_name
                            
                            # section = 'calculation_number' + '_' + str(j)
                            section = 'section_topology' + '_' + str(j)
                            
                            g.add((URIRef(matvoc+a), RDF.type, URIRef(sosa + 'Sample')))
                            # s = BNode()
                            # g.add((URIRef(matvoc+a), URIRef(matvoc + section), s))
                            # g.add((URIRef(matvoc+a), URIRef(nomad + properties1[c]), y))
                            
                            
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
                                                prop1a = 'has'+ '_' + att + str(k)
                                                # prop2a = 'has'+ '_' + attt + str(k)
                                                prop3a = 'has' + '_' + att11
                                                # properties2a.append(prop2a)
                                                properties1a.append(prop1a)
                                                properties3a.append(prop3a)
                                                # if att11 == 'value':
                                                    
                                                    
                                                valu = getattr(para1,att11)
                                                print(valu)
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
                                                    g.add((URIRef(matvoc+a), URIRef(nomad+properties1a[c]), y1))
                                                    # g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                    g.add((y1,URIRef(nomad+properties3a[c]),y3))
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
                                                                   
                                                                    log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties3a[c] + ', ' + 'unit:' + unit2 + ', ' + 'c_unit:' + unit2f + ', ' + 'check:' + '7')
                                                                                          
                                           
                                                      
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
                                                        g.add(URIRef(matvoc+a), URIRef(nomad+properties1a[c]), y1)
                                                        # g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                        g.add((y1,URIRef(nomad+properties3a[c]),y3))
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
                                                                       
                                                                        log_one.warning('issue with unit arrangement:- ' + ' ' + 'formula:' + form_log + ', ' + 'calc_id:' + calc_log + ', ' + 'prop:' + properties3a[c] + ', ' + 'unit:' + unit3 + ', ' + 'c_unit:' + unit3f + ', ' + 'check:' + '8')
                                                      
                                           
                                                           
                                               
                                                except:
                                                    pass
                                                try:
                                                    
                                                    if properties3a not in counter000 and properties3a not in counter0000:
                                                        # print(properties3a)
                                                        y1 = BNode()
                                                        y2 = BNode()
                                                        y3 = BNode()
                                                        g.add((URIRef(matvoc+a), URIRef(nomad+properties1a[c]), y1))
                                                        # g.add((y1,URIRef(nomad+properties2a[c]),y2))
                                                        g.add((y1,URIRef(nomad+properties3a[c]),Literal(valu)))
                                                        counter00000.append(properties3a)
                                                except:
                                                    pass
                                        k+=1
                             
            with open('un.txt', "wb") as fp:   
                pickle.dump(un, fp)
                                        
            g.serialize('metadata_v1_' + str(i) + '.ttl', format='turtle')
            # print('saved')
            # print('enter_repo' + str(i))
            
            # start = time.time()
            
            # headers = {
            #         'Content-Type': 'application/x-turtle',
            #     }
                
            # # data = g.serialize(format='turtle').decode('UTF-8')
            # response = requests.post('http://localhost:7200/repositories/Nomad/statements', data=open('metadata_v1_' + str(i) + '.ttl','r').read(), headers=headers)
            # # print(response)
            # # print('done_repo' + str(i))
            # end = time.time()
            # tot = end - start
            # total = total + tot 
            # print(total)
            


        
        else:
            break  
        
        
logging.shutdown()   
           
        
print('metadata_success')



    






