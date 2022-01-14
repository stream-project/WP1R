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

###############################

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

    
''' creating rdf's using ssn ontology'''
    


''' defining feature of Interest '''           

g.add((URIRef(ab+'materials'), RDF.type, URIRef(sosa+'FeatureOfInterest')))
g.add((URIRef(ab+'materials'), RDFS.label, Literal('calculating energy levels of materials',lang ='en')))

for i in range(1,2):

      a = 'mat'+str(i)
      g.add((URIRef(ab+'materials'), URIRef(sosa+'hasSample'), URIRef(ab + a)))



''' defining sample and metadata related to materials '''


for i, result in enumerate(results):
    
    if i <1:
        
        metadata = result.section_metadata
        if metadata != None:        
            for att, value in (metadata.__dict__.items()):  
    
                
                                    
                    
                if att.startswith(('encyclopedia')):
                    # print(att)                
                    # print(properties[m])
                    # print(meta[m])
                    meta_data = getattr(metadata,att)
                    print(meta_data)
                    if meta_data !=None:
                        for att, value in meta_data.__dict__.items():
                            if att.startswith(('material','properties')):
                                if att == 'material':
                                    meta_enc = getattr(meta_data,att)
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
                                                a = 'mat' + str(i+1)  
                                                m = 'method' +str(i+1)
                                                
                                                material =[]
                                                try:
            
                                                    if meta_mat.isalpha():
                                                        # print(meta_mat)
                                                        g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_mat,lang='en')))
                                                    else:
                                                        g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_mat)))
                                                    material.append(meta_mat)                                               
                                                except:
                                                    if meta_mat not in material:
                                                        ma =BNode()
                                                        g.add((URIRef(ab+a), URIRef(nomad + properties[c]), ma))
                                                        g.add((ma, URIRef(ab+'reference'), Literal('https://nomad-lab.eu/prod/rae/gui/search')))

                                                        
                                                g.add((URIRef(ab+a), URIRef(sosa + 'isSampleOf'), URIRef(ab + 'materials')))
                                                g.add((URIRef(ab+a), URIRef(sosa + 'isResultOf'), URIRef(ab + m)))
                            
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
                                            
                                             
                                            
                                            a = 'mat' + str(i+1)   
                                            hasprop = 'has' + '_' + att1 
                                            elec = []
                                            
                                            try:
                                                magnitude = getattr(meta_mat1,'magnitude')
                                                g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_mat1)))
                                              
                                                elec.append(meta_mat1)
                                                      
                                            
                                            except:
                                                pass
                                                
                                                          
                                                                
                                                              
                                                        
                                                    
                                            
                                         
                                 
                elif not att.startswith(('m_','a_','mainfile','dft','encyclopedia','files','uploader')):
                    
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
                    a = 'mat'+str(i+1)
                    m = 'method' +str(i+1)
                    if meta_data !=None:
                    
                        t = BNode()
                        t1 = BNode()
        
                        g.add((URIRef(ab+a), RDF.type, URIRef(sosa + 'Sample')))
                        g.add((URIRef(ab+a), RDFS.label, Literal('material',lang='en')))
        
                        if meta[c] == 'comment' :
                            g.add((URIRef(ab+a), RDFS.comment, Literal(meta_data,lang='en')))
                        
                        
                        elif meta[c] == 'upload_time':
                            
                            g.add((URIRef(ab+a), URIRef(nomad + properties[c]), t))
                            g.add((t, RDF.type, URIRef(time + 'Instant')))
                            g.add((t, URIRef(time + 'inXSDDateTime'), Literal(meta_data,datatype=XSD.dateTime)))
            
                        
                        elif meta[c] == 'last_processing':
                            
                            g.add((URIRef(ab+a), URIRef(nomad + properties[c]), t1))
                            g.add((t1, RDF.type, URIRef(time + 'Instant')))
                            g.add((t1, URIRef(time + 'inXSDDateTime'), Literal(meta_data,datatype=XSD.dateTime)))  
            
             
                        else: # properties[c] != 'has_comment' and 'has_upload_time':
                            
                            g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_data)))

        system = result.section_run[0].section_system[:]
        # print(system)
        if system != None:
            
            
        
            for j in range(len(system)):
                u = system[j]
                
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
                            
                            m = 'method' +str(i+1)
                            a = 'mat' +str(i+1)
                            
                            
                            g.add((URIRef(ab+a), RDF.type, URIRef(sosa + 'Sample')))
                            g.add((URIRef(ab+a), URIRef(nomad + properties[c]), y))
    
                            
                                       
                            
                            if shape >= 1:
                                
                                g.add((y, URIRef(nomad + 'array'), Literal(magnitude)))                
                            
                            elif shape == 0:
                                
                                g.add((y, URIRef(nomad + 'numericalvalue'), Literal(magnitude))) 
                        
                            
                                
                                
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
                                    # print(unit1)
                                    l2.append(properties[c])
                                
                                
                                except:
                                    pass
                                
                                
                                m = 'method' +str(i+1)
                                a = 'mat' +str(i+1)
                                g.add((URIRef(ab+a), RDF.type, URIRef(sosa + 'Sample')))
                                
                                y1 = BNode()
                                
                                if shape1 >= 1 :
                                    g.add((URIRef(ab+a), URIRef(ab+properties[c]), y1))
                                    g.add((y1, URIRef(nomad+'array'), Literal(X1)))
                                
                                elif shape == 0:
                                    g.add((URIRef(ab+a), URIRef(ab+properties[c]), y1))
                                    g.add((y1, URIRef(nomad+'numericalValue'), Literal(X1)))
                                    
                                if unit1 != None:
                                    u = 0
                                    try:
                                        g.add((y1, URIRef(qudt + 'unit'), URIRef(qudt_unit + unit1)))
                                        u +=1
                
                                    except:
                                        
                                        if u<1:
                                            g.add((y1, URIRef(qudt + 'unit'), Literal(unit1)))
                        
                                # l2.append(properties[c])                    
                        
                        except:
                            
                            
                            if properties[c] not in l1 and  properties[c] not in l2:
                                # print(properties[c])
                                m = 'method' +str(i+1)
                                a = 'mat' +str(i+1)
                                
                                # print('here')
                                
                                # print(X1)
                                
                                if type(X1) in [str,int,complex,float,bool,list]:
                                    g.add((URIRef(ab+a), URIRef(ab+properties[c]), Literal(X1)))
                                
                                else:
                                    
                                    y2 = BNode()
                                    
                                    g.add((URIRef(ab+a), URIRef(ab+properties[c]), y2))
                                    g.add((y2, URIRef(ab+'refernce'), Literal('https://nomad-lab.eu/prod/rae/gui/search')))
                            else:
                                pass
    
    else:
        break  

# g.serialize(r'C:\Users\GuptaR\Desktop\nomad_re\nomad_metadata.ttl', format='turtle')

g.serialize(r'C:\Users\GuptaR\Desktop\nomad_files\nomad_metadata_v1.ttl', format='turtle')

    