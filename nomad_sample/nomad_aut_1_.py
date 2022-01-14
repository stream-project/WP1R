# -*- coding: utf-8 -*-



import urllib.parse
import weakref

from nomad import client, config
import numpy as np

# config.client.url = 'http://nomad-lab.eu/prod/rae/api'


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
                                            
                                            # print(att)
                                            if att.startswith(('material_type','material_id','material_name')):
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
            
                                                if meta_mat.isalpha():
                                                    # print(meta_mat)
                                                    g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_mat,lang='en')))
                                                else:
                                                    g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_mat)))
                                    
                                                g.add((URIRef(ab+a), URIRef(sosa + 'isSampleOf'), URIRef(ab + 'materials')))
                                                g.add((URIRef(ab+a), URIRef(sosa + 'isResultOf'), URIRef(ab + m)))
                            
                            if att == 'properties':  
    
                                meta_enc = getattr(meta_data,att)
                                print(meta_enc)
                                if meta_enc != None:
                                    for att1, value in meta_enc.__dict__.items():
                                        # print(att1)
                                        
                                        if not att1.startswith(('m_','energies')):
                                            
                                            print(att1)
                                            
                                            c=0
                                            meta2 = []
                                            properties = []
                                            meta2.append(att1)
                                            
                                            # electronic=[]
                                            # if meta[c].startswith(('electronic')):
                                            #     meta_mat = getattr(meta_enc,meta[c])
        
                                                
                                            #     electronic = meta_mat
                                            #     print(electronic)
                                            # else:
                                                
                                            meta_mat1 = getattr(meta_enc,meta2[c])
                                            # print(meta_mat1)
                                            prop = 'has' + '_' + meta2[c]
                                            
                                            properties.append(prop) 
                                            # print(meta2[c])
                                            # print(meta_mat1)
                                            
                                             
                                            
                                            a = 'mat' + str(i+1)   
                                            hasprop = 'has' + '_' + att1 
                                            
                                            if meta2[c].startswith(('electronic')):
                                                
                                                g.add((URIRef(ab+a), URIRef(nomad + hasprop), URIRef(nomad + meta2[c])))
                                                
                                            else:
                                                g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_mat1)))
    
                                                
                                                                            
                                                                                            
                                     
                                            
                                         
                                 
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
                        
                        g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_data,lang='en')))

        
        calc = result.section_run[0].section_single_configuration_calculation[:]
        for j in range(len(calc)):
            
            u = calc[j]
            
            for att1, value in (u.__dict__.items()):
                
                if att1.startswith(('section_dos','section_k')):
                    
                    print(att1)
                     
                    
                    r = 0
                    # print(att)
                    obser = []
                    labels=[]
                    quantities = []
                    obser.append(att1)
                    ## condition here 
                    section_prop = getattr(calc[j],obser[r])
                    print(section_prop)
                    
                    if (type(section_prop)) == list:
                        
                        for x in section_prop: 
                            X = x
                    else:
                        X = section_prop
                    
                    for att, value in X.__dict__.items():
                        
                        if not att.startswith(('m','section')):
                            
                            c=0
                            
                            meta3 = []
                            
                            properties = []
                            
                            meta3.append(att)
                            
                            meta_prop = getattr(X,meta3[c])
                            # print(meta_prop)
                            
                            prop = 'has' + '_' + meta3[c]
                            
                            properties.append(prop)
    
                    
                            
                            if hasattr(meta_prop,'magnitude') and hasattr(meta_prop,'units'):
                                magnitude = getattr(meta_prop,'magnitude')
                                units = getattr(meta_prop,'units')
                                p = BNode()
                                p1 = BNode()
                                
                                a = 'mat' + str(i+1) 
                                hasprop = 'has' + '_' + str(att1)
                                # print(hasprop) 
                              
                                g.add((URIRef(ab+a), URIRef(nomad + hasprop ), p))
                                g.add((p, URIRef(nomad + properties[c]),p1))
                                
                                if magnitude.dtype == int:
                                    g.add((p1, URIRef(nomad + 'array'),Literal(magnitude,datatype=XSD.int)))
                                
                                else:
                                    g.add((p1, URIRef(nomad + 'array'),Literal(magnitude,datatype=XSD.float)))
                 
                                g.add((p1, URIRef(qudt + 'unit'),URIRef(qudt_unit + str(units))))
                            
                            elif type(meta_prop) == str:
                                
                                  a = 'mat' + str(i+1) 
                                  g.add((URIRef(ab+a), URIRef(nomad + properties[c]), Literal(meta_prop)))
                                
                            else:
                                 
                                  p = BNode()
                                  p1 = BNode()
                                  a = 'mat' + str(i+1) 
                                  hasprop = 'has' + '_' + att1 
                                  g.add((URIRef(ab+a), URIRef(nomad + hasprop ), p))
                                  g.add((p, URIRef(nomad + properties[c]),p1))
                                  if meta_prop.dtype == int:
                                      
                                      g.add((p1, URIRef(nomad + 'array'),Literal(meta_prop,datatype=XSD.int)))
                                  else:
                                      g.add((p1, URIRef(nomad + 'array'),Literal(meta_prop,datatype=XSD.float))) 
    else:
        break  
    
    

            
''' Sampling '''


for i, result in enumerate(results):
    
    if i <1:
        # calc = result.section_run[0].section_single_configuration_calculation[-1]
        # calc = result.section_run[0].section_single_configuration_calculation[0]
        # calc = result.section_workflow
        esm = result.section_run[0].section_method[:]
        for e in range(len(esm)):
            if esm[e].electronic_structure_method != None:
                esm = esm[e].electronic_structure_method
                # print(esm)
                m = 'method' +str(i+1)
                a = 'mat' +str(i+1)
                # esm = str(esm)
                g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                g.add((URIRef(ab+m), URIRef(nomad + 'electronicstructuremethod'), Literal(esm)))

            else:
                pass
                
        w_type = result.section_workflow.workflow_type
            
        for e in range(len(w_type)):
            if w_type !=None:
                
         
                m = 'method' +str(i+1)
                a = 'mat' +str(i+1)
                # esm = str(esm)
                g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))
                g.add((URIRef(ab+m), URIRef(nomad + 'workflowtype'), URIRef(nomad + w_type )))

    
        else:
            pass
        
        
        metadata = result.section_metadata
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
                print(meta_data)
                for att, value in (meta_data.__dict__.items()):
                    if not att.startswith(('m_','optimade')):
                        # print(att)
                        c = 0 
                        meta = []
                        properties = []
                        meta.append(att)
                        prop = 'has' + '_' + meta[c]
                        properties.append(prop)
                        # print(meta_data)
                        meta_dft = getattr(meta_data,meta[c])
                        
                        # meta_dft = getattr(meta_data,'workflow')
                        # print(meta_dft)
                        
                        trying = []
                        
                        try:
                            for att,value in meta_dft.__dict__.items():
                                # print(att)
                                trying.append(att)
                                # print(trying)
                                
                        except Exception as e:
                            print(e)
                        
                        finally:
                            
                            if att not in trying:
                                
                                a = 'mat' + str(i+1)  
                                m = 'method' +str(i+1)

                                g.add((URIRef(ab+m), RDF.type, URIRef(sosa + 'Sampling')))

                                g.add((URIRef(ab+m), URIRef(nomad + properties[c]), Literal(meta_dft,lang='en')))
                                g.add((URIRef(ab+m), URIRef(sosa + 'hasResult'), URIRef(nomad + a )))

                               
     
    else:
        break
   
        

''' Observations '''


for i, result in enumerate(results):
    
    if i <1:
        print(i)
        calc = result.section_run[0].section_single_configuration_calculation[:]
        # print(calc)
        for j in range(len(calc)):
              
        
            u = calc[j]
            # vars(u)
            for att, value in (u.__dict__.items()):
                r = 0
                # print(att)
                obser = []
                # gupta= []
                labels=[]
                quantities = []
                if not att.startswith(('m_', 'section_',
                                'single_')):
                    
                    # print(att)
                    
                    obser.append(att)
                    label = obser[r]  + '_' +  'calc'
                    labels.append(label)
                    quantities.append(att)
                    # print(labels)
                    # print(rohit)
                    
                    # gupta.append(value)
                           
                    observation = getattr(calc[j],obser[r])
                        
                    
                    magnitude = getattr(observation,'magnitude')   
                    units = getattr(observation,'units')
                    shape = len(getattr(observation,'shape'))
                    
                    print(shape)

                    if shape > 1:
                        row, column = (getattr(observation,'shape'))
                        mat = np.zeros((row,column))
                    
                    
                    if shape == 1:
                        row = (getattr(observation,'shape'))
                    
                 
                    
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
                    
                    
                    if shape > 1:
                        print('true')
                        g.add((y, RDF.type, URIRef(nomad+'matrix')))
    
                        for k in range(len(magnitude)):
                            for l in range(len(magnitude[k])):
                                mat[k][l] = (magnitude[k][l])
                                r = str('row') + str(k)
                                c = str('column') + str(l)
                                y1 = BNode()
                                g.add((y, URIRef(nomad+'haselements'), y1))
    
                                g.add((y1,URIRef(ab+'value'),Literal(mat[k][l],datatype=XSD.float)))
                                # g.add((URIRef(ab+'value'),Literal(mat[i][j])))
            
                                g.add((y1,URIRef(ab+'row'),URIRef(ab+r)))
                                g.add((y1,URIRef(ab+'column'),URIRef(ab+c)))
                    
                    
                    elif shape == 1:
                        
                        g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                        g.add((y, URIRef(qudt+'numericValue'), Literal(magnitude[r],datatype=XSD.float)))
                    
                    else:
                               
                        g.add((y, RDF.type, URIRef(qudt+'QuantityValue')))
                        g.add((y, URIRef(qudt+'numericValue'), Literal(magnitude,datatype=XSD.float)))
                    
                    
                    g.add((y, URIRef(qudt+'unit'), URIRef(qudt_unit+str(units))))
    
    
        else:
            
            break



g.serialize(r'C:\Users\GuptaR\Desktop\nomad\nomad_aut_1.ttl', format='turtle')



