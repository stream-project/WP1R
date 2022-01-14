# -*- coding: utf-8 -*-


import urllib.parse
# import weakref
from nomad import client, config
import numpy as np


from nomad import client, config

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

###################################

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



            
''' Sampling '''


for i, result in enumerate(results):
    
    if i <1:
        calc = result.section_run[0].section_single_configuration_calculation[-1]
        calc = result.section_run[0].section_single_configuration_calculation[0]
        calc = result.section_workflow
        
        esm = result.section_run[0].section_method[:]
        if esm != None:
            if type(esm) == list:
                for x in esm:
                    X = x
            else:
                X = esm
                
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
                    # X1 = getattr(X,'section_method_atom_kind')
                    # # print(X1)
                    # # type(X1)
                    # # len(X1)
                    
                    # for i in X1:
                    #     for att,val in i.__dict__.items():
                    #         if not att.startswith(('m_','_')):
                    #             val = getattr(i,att)
                    #             print(val)
                        
                        
                    # len(X1)
                    # for x in X1:
                    #     print(x)
                    #     type(x)
                    #     break
                    # # # method = getattr(method,'shape')
          
                    
    
                  
    
                    # if type(method) == list:
                    #     for x in method:
                    #         X1 = x
                    # else:
                    #     X1 = method
                    
                    # # type(X1)
                    # # print(X1)
    
                    
                  
                            
                            
                            
                       

                    try:
    
                        y = BNode()
                        shape = len(getattr(X1,'shape'))
    
                        # print(shape)
                        magnitude = getattr(X1,'magnitude')
                        units = getattr(X1,'units')
                        unit = str(units)
    
    
                        # print(unit)
    
    
                        m = 'method' +str(i+1)
                        a = 'mat' +str(i+1)
                        
                        g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                        g.add((URIRef(ab+m), URIRef(nomad + properties[c]), y))               
                        
                        if shape >= 1 :
                            g.add((y, URIRef(nomad + 'array'), Literal(magnitude)))                
                        elif shape == 0:
                            g.add((y, URIRef(nomad + 'numericalvalue'), Literal(magnitude))) 
                        
                        # else:
                        #     if shape >=1 :
                        #         g.add((y, URIRef(nomad+'array'), Literal(X1)))
                        #     else:
                        #         g.add((y, URIRef(nomad+'numericalValue'), Literal(X1)))
                            
                            
                        if unit !=None:       
                            u = 0
                            try:
                                g.add((y, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit)))
                                u+=1
        
                            except:
                                if u<1:
                                    g.add((y, URIRef(qudt + 'unit'), Literal(unit)))
                        
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
                            
    
    
                            # units = getattr(X1,'units')
                            # unit = str(units)
                            
                            m = 'method' +str(i+1)
                            a = 'mat' +str(i+1)
                            g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                            y1 =BNode()
                            
                            if shape1 >=1 :
                                g.add((URIRef(ab+m), URIRef(ab+properties[c]), y1))
                                g.add((y1, URIRef(nomad+'array'), Literal(X1)))
                            
                            if shape1 == 0:
                                g.add((URIRef(ab+m), URIRef(ab+properties[c]), y1))
                                g.add((y1, URIRef(nomad+'numericalValue'), Literal(X1)))
                                
                            if unit1 != None:
                                u = 0
                                try:
                                    g.add((y1, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit1)))
                                    u+=1
            
                                except:
                                    if u<1:
                                        g.add((y1, URIRef(qudt + 'unit'), Literal(unit1)))
    
                    except:
                        
                        if properties[c] not in l1 and  properties[c] not in l2:
                            # print(properties[c])
                            m = 'method' +str(i+1)
                            a = 'mat' +str(i+1)
                            
                            if type(X1) in [str,int,float]:
                                g.add((URIRef(ab+m), URIRef(ab+properties[c]), Literal(X1)))
                            
                            else:
                                
                                
                                
                               
                                # for k in range(len(X1)):
                                #     # print(X1)
                                #     print(k)
                                    
                                    
                               
                                    
                                    if type(X1) == list:
                                        
                                        k=0
                                        for x in X1:
                                            
                                            for att2, value2 in x.__dict__.items():
                                                
                                                
                                                
                                                if not att2.startswith(('m_','_')):
                                                    
                                                    
                                   
                                    
    
                                                    
                                                # print(att2)
                                                
                                                    c1=0
                                                    meta1=[]
                                                    properties1=[]
                                                    properties2=[]
    
                                                    meta1.append(att2)
                                                    prop1='has'+'_'+meta1[c1] 
                                                    prop2 = 'has' + '_' + meta[c]  + str(k)
    
    
                                                    properties1.append(prop1)
                                                    properties2.append(prop2)
    
                                                    value = getattr(x,meta1[c1])
                                                    print(value)
                                                    
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
                                                                print(value)
                                                                y2 = BNode()
                                                                g.add((URIRef(ab+m), URIRef(ab+properties2[c]), y2))
                                                                g.add((y2, URIRef(ab+properties1[c1]), Literal(value_try)))
                                                                # v = getattr(value,att3)
                                                                # print(v)
                                                            
                                                                                                               
                                                        
                                                        
                                                    except:
                                                          y2 = BNode()
                                                          g.add((URIRef(ab+m), URIRef(ab+properties2[c]), y2))
                                                          g.add((y2, URIRef(ab+properties1[c1]), Literal(value)))
                                            k+=1

                                                            
                                            # break        
                   
                                
                                           

                                    
                        # else:
                        #     pass
                        
                
              
        
        
        
        w_type = result.section_workflow.workflow_type
        print(w_type)
        
        if w_type !=None:
            
            
            for e in range(len(w_type)):
                    
             
                    m = 'method' +str(i+1)
                    a = 'mat' +str(i+1)
                    # esm = str(esm)
                    g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                    g.add((URIRef(ab+m), URIRef(nomad + 'workflowtype'), URIRef(nomad + w_type )))

    
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
                            # print(meta_dft)
                            # import types
                            # meta_dft = getattr(meta_data,'optimade')
                            # print(meta_dft)
                            # if isinstance(meta_dft, types.ClassType):
                            #     print("Yep, it's new-style class")
                            # print(type((meta_dft)))
                            # if type((meta_dft)) == None:
                            #     print('another_one')
    
                            
                            # meta_dft = getattr(meta_data,'workflow')
                            # print(meta_dft)
                            
                            trying = []
                            
                            try:
                                for att1, val1 in meta_dft.__dict__.items():
                                    if not att1.startswith(('m','_')):
                                        # print(att1)
                                        c2 = 0
                                        meta3 = []
                                        properties3= []
                                        meta3.append(att1)
                                        prop3= 'has' + '_' + meta3[c2]
                                        properties3.append(prop3)
                                        x = getattr(meta_dft,att1)
                                        # print(x)
                                        # value3 = getattr(meta_dft,'species')
                                        try:
                                            
                                            if type(x) == list and len(x)>1:
                                                
                                                
                                                    
                                                
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
                                                            prop3= 'has' + '_' + meta3[c2] + str(k1)
                                                            # print(prop3)
                                                            properties5.append(prop3)
                                                            value4 = getattr(x1,att2)
                                                            print(value4)
                                            
    
                                            
                                        
                                                            m = 'method' +str(i+1)
                                                            y3 = BNode()
                                                            y4 = BNode()
                            
                                                            g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                                                            g.add((URIRef(ab+m), URIRef(nomad + properties[c]), y3))
                                                            g.add((y3, URIRef(nomad + properties5[c2]), y4))
                                                            g.add((y4, URIRef(nomad + properties4[c3]), Literal(value4)))
    
                                                            
                                                            
                                                            trying.append(properties4)
                                                    k1+=1
                                                
                                            elif type(x) != list:
                                                if properties3 not in trying:
                                                    
                                                    m = 'method' +str(i+1)
                                                    y5 = BNode()
                    
                                                    g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                                                    g.add((URIRef(ab+m), URIRef(nomad + properties[c]), y5))
                                                    g.add((y5, URIRef(nomad + properties3[c2]), Literal(x)))
                                                    trying.append(properties3)

                                                
                                                
                                        
                                            
                                      
                                        except:
                                            
                                            if properties3 not in trying:
                                             
                                     
                                                 m = 'method' +str(i+1)
                                                 y5 = BNode()
                 
                                                 g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                                                 g.add((URIRef(ab+m), URIRef(nomad + properties[c]), y5))
                                                 g.add((y5, URIRef(nomad + properties3[c2]), Literal(x)))
                                                 trying.append(properties3)

                                                    
                                        # else:
                                        #     m = 'method' +str(i+1)
                                        #     y3 = BNode()
             
                                        #     g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                                        #     g.add((URIRef(ab+m), URIRef(nomad + properties[c]), y3))
                                        #     g.add((y3, URIRef(nomad + properties3[c2]), Literal(x)))
                                            
                                            # trying.append(x1)
                               
    
                            except:
                                
                               
                                
                                
                                if properties not in trying:
                                    
                                    a = 'mat' + str(i+1)  
                                    m = 'method' +str(i+1)
    
                                    g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
    
                                    g.add((URIRef(ab+m), URIRef(nomad + properties[c]), Literal(meta_dft,lang='en')))
                                    g.add((URIRef(ab+m), URIRef(sosa + 'hasResult'), URIRef(nomad + a )))

                               
     
    else:
        break
    
# g.serialize(r'C:\Users\GuptaR\Desktop\nomad_re\method.ttl', format='turtle')

   

g.serialize(r'C:\Users\GuptaR\Desktop\nomad_files\method_v1.ttl', format='turtle')

