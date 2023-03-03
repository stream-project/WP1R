# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:30:52 2023

@author: GuptaR
"""


# -*- coding: utf-8 -*-




from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys


from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib import URIRef








''' query2a '''


from SPARQLWrapper import SPARQLWrapper, POST, DIGEST






import requests

print('insert_canonical_formulas_in_hybrid')

headers = {
    'Content-Type': 'application/sparql-update',
}

data = "PREFIX hybrid3:<https://materials.hybrid3.duke.edu/materials/> PREFIX matvoc:<http://stream-ontology.com/matvoc-core/> INSERT DATA { <https://materials.hybrid3.duke.edu/materials/system/113> hybrid3:has_canonical_formula matvoc:NH4SnI3.\
<https://materials.hybrid3.duke.edu/materials/system/188> hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
    <https://materials.hybrid3.duke.edu/materials/system/41> hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
                <https://materials.hybrid3.duke.edu/materials/system/105> hybrid3:has_canonical_formula matvoc:C3H10NGeI3.\
            <https://materials.hybrid3.duke.edu/materials/system/106> hybrid3:has_canonical_formula matvoc:C3H10NGeI3.\
                <https://materials.hybrid3.duke.edu/materials/system/333> hybrid3:has_canonical_formula matvoc:C3N2H5SnI3\
                    <https://materials.hybrid3.duke.edu/materials/system/79> hybrid3:has_canonical_formula matvoc:CH5N2GeI3.\
                        <https://materials.hybrid3.duke.edu/materials/system/39> hybrid3:has_canonical_formula matvoc:CH5N2PbI3.\
                            <https://materials.hybrid3.duke.edu/materials/system/94> hybrid3:has_canonical_formula matvoc:C2H7N2GeI3.\
                                <https://materials.hybrid3.duke.edu/materials/system/191> hybrid3:has_canonical_formula matvoc:CH6NSnBr3.\
                                    <https://materials.hybrid3.duke.edu/materials/system/348> hybrid3:has_canonical_formula matvoc:C3H8Br3NPb.\
            <https://materials.hybrid3.duke.edu/materials/system/402> hybrid3:has_canonical_formula matvoc:C3H8Br3NPb.\
      <https://materials.hybrid3.duke.edu/materials/system/95> hybrid3:has_canonical_formula matvoc:CH6N3GeI3.\
          <https://materials.hybrid3.duke.edu/materials/system/362> hybrid3:has_canonical_formula matvoc:CH6NPbBr3.\
    <https://materials.hybrid3.duke.edu/materials/system/190> hybrid3:has_canonical_formula matvoc:CH6NSnCl3.\
        <https://materials.hybrid3.duke.edu/materials/system/184> hybrid3:has_canonical_formula matvoc:C2H8NPbI3.\
    <https://materials.hybrid3.duke.edu/materials/system/1> hybrid3:has_canonical_formula matvoc:CH6NPbCl3.\
      <https://materials.hybrid3.duke.edu/materials/system/44> hybrid3:has_canonical_formula matvoc:CH5N2SnI3.}"

response = requests.post('http://graphdb:7200/repositories/Hybrid3/statements', 
                         headers=headers, data=data)


print(response)








            
            


