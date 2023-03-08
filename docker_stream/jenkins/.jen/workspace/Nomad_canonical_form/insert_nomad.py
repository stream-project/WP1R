# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:25:59 2023

@author: GuptaR
"""

from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys
from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib import URIRef
import re




# original_form
t =[]
with open('result_hybrid_common.txt') as f:
    for line in f:
        line = line.strip('\n')
        t.append(line)

# print(t)


# alpha form

t1 = []
for i1 in t:
    # print(i2)
    # i1 = i1.split(',')[0]
    # print(i3)
    i1 = re.sub("[^A-Za-z0-9]", '', i1)
    # print(i1)


    i1= re.sub( r"([A-Z])", r" \1", i1).split()

    # print(i1)

    i1 = sorted(i1)

    i1 = ''.join(i1)


    # print(i1)
    # break
    
    t1.append(i1)

# print(t1)
# print(type(t1[0]))


## querying the id's



from SPARQLWrapper import SPARQLWrapper, POST
import requests





import requests
import random

def insert(subject, predicate, object, graphdb_endpoint):
    # Construct the SPARQL query with placeholders for the subject, predicate, and object
    query = """
    PREFIX matvoc:<http://stream-ontology.com/matvoc-core/> 
    # PREFIX nomad: <http://https://nomad-coe.eu/ontology#>
    INSERT DATA {
      matvoc:%s matvoc:%s matvoc:%s .
    }
    """


    # Replace the placeholders in the SPARQL query with the random values and the provided predicate
    query_with_random_values = query % (subject, predicate, object)

    # Send the SPARQL query to the GraphDB server using the HTTP POST method
    response = requests.post(graphdb_endpoint, data={"update": query_with_random_values})
    
    print(response)
    # print(response.content)

# insert("roit", "name", "John", "http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/try/statements")



sparql = SPARQLWrapper("http://graphdb:7200//repositories/Nomad")
   


def formula(form,abx3):

    query_template = '''
    
        
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
        PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
        PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX bacdive: <http://kg.bacdive.dsmz.de/>
        PREFIX qudt: <http://qudt.org/2.1/schema/qudt#> 
        PREFIX matvoc:	<http://stream-ontology.com/matvoc-core/>
        PREFIX nomad: <http://https://nomad-coe.eu/ontology#> 
        PREFIX sosa: <http://www.w3.org/ns/sosa/> 
        
        select ?subject
        
        where
        
        {{
            
            ?subject a sosa:Sample;
              nomad:has_formula <{object}>.
            
                               
            
        
                                                                       
        }}
        
    '''
    query = query_template.format(object=form)
    
    # create a SPARQLWrapper object and set the query and endpoint URL
    # sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    
    # set the query format and execute the query
    sparql.setReturnFormat(JSON)
    results_query1 = sparql.query().convert()
    # print('rohit')
    # print(t)


    x1 = abx3    
    for result in results_query1["results"]["bindings"]:
        material_id = result["subject"]["value"]
        # print(material_id)
        m = (material_id.split('matvoc-core/')[-1])
        print('gupta')
        print(m)
            
            # insert(m,x1)
        insert(m, "has_canonical_form", x1,"graphdb:7200/repositories/Nomad_hybrid/statements")
            
                



for x, y in zip(t1,t):
    # print(x,y)
    # print(x)
    matvoc = 'http://stream-ontology.com/matvoc-core'
    form = matvoc+'/'+x
    # print(form)
    formula(form,y)
    

    

# print(results_list)

# sparql.setQuery("""
 
# PREFIX dc: <http://purl.org/dc/elements/1.1/> 
# PREFIX nomad: <http://https://nomad-coe.eu/ontology#> 
# PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>  
# PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
# PREFIX sosa: <http://www.w3.org/ns/sosa/> 
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
# PREFIX matvoc:	<http://stream-ontology.com/matvoc-core/>

# select ?material_id
# WHERE
# { 
    
#     ?material_id a sosa:Sample.
#       nomad:has_formula ?formula.
#     }
# """)

# results = sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query1 = sparql.query().convert()

# ''' storing results locally '''
# query1=[]
    
# for result in results_query1["results"]["bindings"]:
#     query1.append((result["formula"]["value"]))
# with open('query1_nomad_hybrid_try.txt', 'w') as f:
#     for s in query1:
#         f.write(str(s)+'\n')   
#         # f.write(str(s)+'\n')   

# ''' query2a '''
# from SPARQLWrapper import SPARQLWrapper, POST, DIGEST

# import requests

# headers = {
#     'Content-Type': 'application/sparql-update',
# }

# data = "PREFIX hybrid3:<https://materials.hybrid3.duke.edu/materials/> PREFIX matvoc:<http://stream-ontology.com/matvoc-core/> INSERT DATA {  matvoc:mat_H4I3NSn_5GtoP8hRMTumn5BdRjRIz2KmQhqE hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_5t5UAGHT7IiC_5xHQOPLGtJr4GQg hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_74HvXZGCKjmSO6EqNnI_g6NIRybd hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#       matvoc:mat_H4I3NSn_8stpfIPNKDYOBXEZfCiwo0zx7-fQ hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#       matvoc:mat_H4I3NSn_9RTICR94OwIZtLP9GvO__5_jJ0NR hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#       matvoc:mat_H4I3NSn_A7dsIk5t1fdhrtYZkE5qRVVgLPQ6 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_CGjml8uMtvaQeG80Rrd1nsHEdEsO hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_DEfGEi-OkUrVzFxJpwcIQQV_CbMR hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_R8FPQWf_-3DKXxHmnqImSo4Be1NO hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_SryfCgNfSzLkUTWhTtSaXg_CA0nA hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_U-vmGNCz-HCnrt3Am0DTEGOQtbD5 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#   matvoc:mat_H4I3NSn_VEVuWioZK4rVePtfvlL3Z2CNA4t5 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_WquVr6Kz8ozKGlGPcXvarbZJdQB5 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#       matvoc:mat_H4I3NSn_XMSWSgNkvzth0LiplVCNKDbgTo47 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#       matvoc:mat_H4I3NSn_XcQum__URK5o-36WHKnWDhOF7IuO hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn__Uk4KzdxnB-pXwtiPsFsqC5nG_Ighybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn__irtejxyx6pjKa2fBz5IaEaBLHT4 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#       matvoc:mat_H4I3NSn_dzJjLOa4ZzFQuWJUfqhDcrzkHpbw hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#   matvoc:mat_H4I3NSn_i0lDKg57ZvSd1seUOzevzdYhD2Ov hybrid3:has_canonical_formula matvoc:NH4SnI3.\
# matvoc:mat_H4I3NSn_mKtSnoMiULqs37w9j4ZsU7N2NEC6 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#     matvoc:mat_H4I3NSn_p2p5DbVK3HYJmZictSNgNzpShJl2 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#      matvoc:mat_H4I3NSn_rmgnidxtZE7zZZAWryTWyUSfqytF hybrid3:has_canonical_formula matvoc:NH4SnI3.   matvoc:mat_H4I3NSn_sLt8QR7A6GyjwtO010IeWuvryC35 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#        matvoc:mat_H4I3NSn_tcMB0a7ifyVXBSgmnKj1-4w3XX21 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
#        matvoc:mat_CH6Br3GeN_5Zhy4ZxzqZk-jheF3RXlQ6-j8wjD hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_5Zhy4ZxzqZk-jheF3RXlQ6-j8wjD hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_88OxGoWJnJ-kEn3UssRgBxKi9Wz3 hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_98FdrKisJyOBJcjoUiImyX1sItAs hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_AdT5rdaIP0xTpTd67kYumT1M4QSj hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_AkgW6DC4fejLt8xXSKpoYyNJLLm_ hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_DJ_Jxi2K_sijlq-Yo2uCuKtI9YjA hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_EPGSwuwMabAgtt-UZh_grY8rZbEY hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_GIJAZ2tFqDPbsBooxmvglUnAgfFy hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_Gj2JbqreSHFCaa3aSRiX7WZipDrU hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_H-UcTgFyZvzjYKLW9SjHIiV-OpLe hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_Ja21yOdQmCtzX6quUGuclOOr5YsS hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_Jw1jiCDYOb5cLF7HlEj-DSuX33hD hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_L_B-PXSjhfLhclVZzp5dAq3x6G_d hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_NvjmqnWbAU5Y3UOCGr5tuxSbFz5d hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_P4aehyyI5JYd944WQ4ib_Ge_OxoI hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_P8_SSRF9zTAGKtWYBt97yC4FsBpS hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_SgRtUE-c6nUuePe5Ug8MYjmUqhMg hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_TwLDmaYczHk5GFfDN2YPLt9iMiWM hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_U3pGABdWnvSRk_v7rAimGCK0-gFv hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_Wg_E-cP0eLT0Yze_VJ2oV_n3vKL3 hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_aZVRj3uBRFL4slHt3krK8FfQqWx_ hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_bQZvu7cJem7AGAd3zcJVs4hhM0tP hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_b_mbxaJMlwDc0hqkG8SgmwyCT6KZ hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_gtYUrTtzwFobZdLbjSuVxGr_QXce hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_h4TfUyKCONaLgSi5jy6VeHlP2rv0 hybrid3:has_canonical_formula matvoc:CH6NGeBr3. matvoc:mat_CH6Br3GeN_hcbtlYOddaUil8CYJwTLJBxLeKTR hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_hpuPxDic0LgPKIY6_fWlP8XQpu9J hybrid3:has_canonical_formula matvoc:CH6NGeBr3. matvoc:mat_CH6Br3GeN_lCLMGJ7_B_7jUAufiqNaK1FluxeI hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_n4p5qR3n0o4-eFhBNvWPm7vWz3BQ hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_nsVRQdaEw9qbYmKjL43jAOUHdauh hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_pOOraVuVg2DMSp1UD6flY3oalv9w hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_qD46xJUE5sDq4f0P-xdC4ZwkB9mm hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_sRCaOWKL9cnY7UFGMu7l_2v_Ef11 hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_vFdu24syS3f6vWyghYhAD3KZMWJC hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH6Br3GeN_vsWt8RyjYjXHKqUXDscdO564SzKL hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
# matvoc:mat_CH5Br3N2Pb_3mMuRJiKLlfqJ3tmzwPfgl_M0y9P hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_5GOtCgMIpyxxop8FgiubrYMytHvU hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_8kmtSqhs4Vzrv40vbGxpSlKaY0bM hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_9H6gjdnXZfBb1mGGjJHrZix-kWqU hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_JIGMU02mJ5xGUdL3GHTEnmu_iQ3- hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_R1Jd6-6KvwmRC-E99nyJnM4h2xsk hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_RpdhBT3DcpC-Jqt1f3dOqwyrU9Fo hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_S5vOenl19vAngeC0zf_44GrFlqfa hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_YGZsX22g5rotnlQkOeAypRZ_Owsi hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_aNIOR0n5mtu-gHUWKsPBLfkLon8X hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_bqeBwCg4_dZkSb4upAc_paVx5hq3 hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_eG1G_Cu6_vrQyBPcYn1CSHYVQJY7 hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_erekcQqiMmGEs-HYDCJjF0ZpThyP hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_f3rZY4yPBsB3OWquv1Lr-h_KjTgE hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_ink19SnGrnRvvYnzorUAoFCsw9t5 hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_m-0wA23O2c7UDaMOhug7z5won4ay hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_rM9JaP2mS0XixoSyT1EAFm1yXw84 hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
# matvoc:mat_CH5Br3N2Pb_vlvoT-f8k-JWlUdSP_DIB-q92-AM hybrid3:has_canonical_formula matvoc:CH5N2PbBr3. \
# matvoc:matvoc:mat_C3H5I3N2Sn_-kwzT9D4XOlu9QV_E-toxSLvKkI0 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_0BFYoL3UZ_9_U8oL30C02SpYxeEO hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_15EU0Lam-jo378S5m07CRjwWlwkV hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_2Qw8CNkQ6LoaeVaWsUYOOMw4VVZp hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_3l1Nb4Z2FrsN3LwoyRK-9icgMzOY hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_3zCqYVgT2kr36-6__9Ux6mZEtjqi hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_4FlfGF9u-t1YalpkonZxapyCOVFt hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_5VQ_mWi1XhEbnmfkiib7mMKrDz2M hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_61abSmcNoCgtuVeT8PaapCCLFb8i hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_CDTHisCDa7hzfRRjJmB7sR9pWCNj hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_DBCDOwOSyM22N2FAYCX626huwLaB hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_DEIbeUbLXl6IQf_xgqH8c3i644m7 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_FRFA15wgvkEoTJdBqseK6W-u-ZxD hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_H1g7zUdKv9HPce90uFPepiT1_1s3 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_HcOSyRL4v34XhDB4rt-hAloMpp-F hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_IT1mKNfLiqhHYZXacMQQi6mXPmnS hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_KngGQHdR2aJnCydwIgLRmIom7gpZ hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_LBcRXcMdBfPBViOK92On183w05uo hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_LIpIx5OmW02t3ql_H-zm2XDgKktV hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_LJ_fUjOAPtS2YuP5uRvzJS1Ir_hJ hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_LVu3UD5XB80o5lnjs14lqQtoi51J hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_Leioul4T1rewyoCxKq6Z4qUE5B5f hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_OY_TI4l_UmSo145pfMskg_EebHNV hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_QeahuXIVSonQD-VA-zZMLMzO8vOH hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_SDN1e0kKeWnQsr0yOnlWmfCIFiCd hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_UugaoSrSW2tRCVk-kUnJzqld3g3z hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_W3G1Yt96doVRrtzs_JsYWgKMAmZQ hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn__tA8jBUhVgKHNNgMNWPTzKjiLQKN hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_bu6sL6mXdko02C7YGyt2_FgcKNID hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_cf8kl9R3XDklstNxrvbC6GbuWSJ9 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_dRFdRGQ_8R_plANMZcoCLSaNxE8c hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_dWMbbghrpWD36S2gbpVsiF7_EjAf hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_f1TS5wDElni3yt7Ct2uu0z37mY_l hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_fKJISX4nd0KtIsgdW0du3tfmQVZA hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_faRp7iWoDOP2zoqPq-5kNGXjKkZZ hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_g5vAbdYDrfkqStqaT4bvFnMadJG8 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_g6yrAiEQWGpmrzsANvHHk8zVqJvr hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_gNCgdqafQoKJLz84cPyhlkf3QRA9 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_go0xeWPMjMIbWtd2Nb-7aOKOhy_D hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_hCscn61g7ToL4DG9-ihDQrlMAKAd hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_j8oIHEXfVsazoLBEMF66OqkNl3nH hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_k1-DN7jRFw7C31Bk0CY3Unbd2yxS hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_kiH4ggDVMuFEdEboCCBWR8Aub7oV hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_lNzTjGmPmLjq4za0Zm18oHazVmzG hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_nccsUxsNoZn6PjoU0QEsQm590RwW hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_oDnjRbzycp7MHbknro1Fo-xT80R3 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_q-YdP-fbtqafmph0fjX3perahBru hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_rstgTTOPo0PJm8okmKQFVK0iSQ6n hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_sAmgY-5Rd9763rvg6zl1p8Dunrrz hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_tgD2Vx6JGlj00Sf8ZFUfDzmPZL_R hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_xAbPWXRly3x_2yyvSCKczxGC80i4 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_y_HCaTrH1kC8D9tNU4I5TyZjo3cE hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_z0gBrORRzauIobOkVBRcQFsqn4cj hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_C3H5I3N2Sn_zrO2-S9YTgMobbxCEDlu4ILkBmUc hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
# matvoc:mat_CH5I3N2Pb_30F6rw0xqsk_iTbjWUusd9bUViAy hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_4HsmfmOnqQeKCKGIySWvbc861yG1 hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_89ZsUFCpTjYPleRaJdq1pQQBETng hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_99qZq9crkqEfevWpa5Wq-_0aw-ol hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_Df-LkhdYHCr4Wh2kaK6Hvml60ETg hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_IG91UeXBMYMX1Slz_s77d86zNiib hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_J7DILGe0QMFnF5aEtRzyICUzUhkT hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_Lp3IY5Uz2P-UkhpfzNtqMyXr9fse hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_PX1SX6t9V3-ojacDwChsYX-2De9b hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_SIRiW0zByBDDjWa1vR-2upBUE6Bq hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_TOzY0msF1XGarSIhvLcJikOfZ0cy hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_YgFdR0J3TgFHL6OeySR1xvKsFqfP hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_Ytsi3qn7Bt_7949ISrpUieVO0DGj hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_ZMPuXE08HuMh1m-jWJ0b23PSY2N5 hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH5I3N2Pb_c-5Itp9xhN7rPErrsv8SF3DxAs9K hybrid3:has_canonical_formula matvoc:CH5N2PbI3.\
# matvoc:mat_CH5I3N2Pb_fkUjeY3ghtmz6W1qG1dVus7NIXKZ hybrid3:has_canonical_formula matvoc:CH5N2PbI3.\
# matvoc:mat_CH5I3N2Pb_lPVA9-NO4O080K77kWYR-zo75gPR hybrid3:has_canonical_formula matvoc:CH5N2PbI3.\
# matvoc:mat_CH5I3N2Pb_xsx0EA9YYVdy36s3WbA3e4Lwlpoo hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
# matvoc:mat_CH6Br3NSn_4hX5EWYY3r-WulnTdLm-4GSnztPE hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_77hy58KEL2RJ2uaZdklydIJM0Hk2 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_7VRqHzhznVh8g8AjBtwI15_zrYo7 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_8OD2pfYr0z47JJiL8MqjV63vJgYp hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_ANW_pLHkZyrlgBApiqKNJOVa3NjZ hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_CWKU6OPEfPBcZ0jQYSBkDPSMuuoG hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_CxwCHcNz0wDyHWqPAU3CuGG3hFwl hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_DQLz_3Yfvq2Rcb1QhenWI9LaQDab hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_FCRz_CJ_YueraeqWaTKSliRtRTE6 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_G28dyiEuBIzN8qbWSDAp_93bWHS9 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_IMrGK-FpLg3QbCvEA9yVCpAZ_Mtg hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_IWA3-HQBsvnwLCURmFFsSQIF2S7_ hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_JN9jZysgacCZL5Tr4WJKAEjNQIK1 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_JZTohq0HZMLugAB60UFtTqvA3Ujv hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_P_9efogaIN2zRC1PGZxU05Wu1aGt hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_ROQBi8F0GkuORzlQIvR-vlWEfTMA hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_RtE4UGlV5GAx7MSZB6KJ2cq0OKkw hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_UYfoUa3Xl_Ta1KGw5pVhhQzs1vsd hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_UbRX1K1ldQvMBoUGkFcZQWir-LcO hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_Y2B3KbWcahYw8KCigkh62O9-99Lk hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_aFNX9V153WATn17HrbnKVTNL851I hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_aJ8y4l0cPLuS3xjOJrbKH2t-svei hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_f8uARR6qE7teUFqkfuCEHI46ij0i hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_hfE8jy-VsARRojCuNnDgjJW8ugsE hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_joNRMj01YttdqKcwu-LWbzxWRnpP hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_kwWiL0kQoMUMXeczTuoX8lLA_1Lw hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_msGQgvnmZt6r1_a7LzXtwmJ_qAUZ hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_n8lfS0oxZ1qkzvxP6QflTmiwvfBK hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_q2z0f1BK2PbGogFBQ1cDuJOprYdy hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_v0CaYU-JNYnOED74iuONqtWJpN2a hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_vY_Gv_qUvMhTtxcxnNUsL5orKHyI hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_y9183C9W1IvzBhAaUAlzqKQ13Lfz hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_yERi6sdRe3NwW95h2DsgEMOn9c1z hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_yaiDAUgmnoYEJk5vv2X7gGY31YDP hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_CH6Br3NSn_zEHwCsKQwrWFHYr1qtLok0WMzjIi hybrid3:has_canonical_formula matvoc:CH6NSnBr3. matvoc:mat_CH6Br3NSn_zkPJNmtHNB3Ae6gTovZR1oalTCoj hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
# matvoc:mat_C3H8Br3NPb_-DHFm9kuAfH3seAfy9GNwh7kmh6n hybrid3:has_canonical_formula matvoc:C3H8Br3NPb. matvoc:mat_CH6Br3NPb_4FuXctl_VlayNvhk6qkHr12dbpDu hybrid3:has_canonical_formula matvoc:CH6NPbBr3. \
# matvoc:mat_C2H8I3NPb_-j6vzE9ZLj34lDgywyCKN2AMr5Az hybrid3:has_canonical_formula matvoc:C2H8NPbI3. } "
    


# response = requests.post('http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/Nomad_hybrid/statements', 
#                          headers=headers, data=data)


# print(response)




# INSERT
# { 
    
#     ?system hybrid3:has_canonical_formula ex:C2H8NPbI3. 
    
#     } 

# WHERE { 
#        ?system hybrid3:has_formula ex:C2H8NPbI3.
#        }
 
# """)


# sparql.setVariable("matvoc_formula", "matvoc:C2H8NPbI3")
# # http://stream-ontology.com/matvoc-core/C2H8NPbI3
# results = sparql.query()
# # sparql.method = 'POST'
# # sparql.query()
# # print(results)
# sparql.setReturnFormat(JSON)
# results_query1 = sparql.query().convert()




            
            


