# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:54:40 2022

@author: GuptaR
"""


import re
import io

import os

import sys

import pandas as pd 


from rdflib import Graph

from pathlib import Path

import pickle

import configparser

import unidecode

import numpy as np

import time

import mysql.connector




""" reading the path from path.properties file,specify the path of path.properties file """

config = configparser.ConfigParser()

''' specify the path of path.properties file here '''

config.readfp(open('./tables.properties'))

''' taking tables name '''

table1 = config.get('TABLES','materials_dataset')

# ''' taking queries '''

# query1 = config.get('QUERIES','query1')

print(table1)


mydb = mysql.connector.connect(
    host = 'db',
    user = 'root',
    passwd = 'root',
    database= 'hybrid',
    auth_plugin='mysql_native_password')

#mydb = mysql.connector.connect(
#    host = 'localhost',
#    user = 'root',
#    passwd = '8227',
#    database= 'hybrid')

# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("select database();")

database = mycursor.fetchone()

print(database)

    
for each_section in config.sections(): 
    for each_key, each_val in config.items(each_section):
        
        query = each_val
    
       
        print(query)
            
  
        # query = 'select * from materials_dataset' 
        
        results = pd.read_sql_query(query, mydb)
        
        def remove_accents(a):
            return unidecode.unidecode(a.encode().decode('utf-8'))
        
        if each_key == 'materials_dataset':
            
            results['secondary_property_id'] =  results['secondary_property_id'].astype('Int64')
            results.to_csv(each_key + ".csv", index=False)
            
        elif each_key == 'materials_author':


          
            results['first_name'] = results['first_name'].apply(remove_accents)
            results['last_name'] = results['last_name'].apply(remove_accents)
            results['institution'] = results['institution'].apply(remove_accents)
            # unidecode.unidecode(u)
            results.to_csv(each_key + ".csv", index=False)
            
        elif each_key == 'materials_experimentaldetails':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r') as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
            for col in result.columns:
                if result[col].dtype == np.object_:
                    result[col] = result[col].str.replace('\n','')
            result.to_csv(each_key+".csv", index=False)
        
        # elif each_key == 'materials_computationaldetails':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r') as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
        #     print(result)
        #     print(result.columns)
        #     for col in result.columns:
        #         if col == 'text':
        #             if result[col].dtype == np.object_:
        #                 result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)
        
        
        # elif each_key == 'materials_synthesismethod':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r') as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)),on_bad_lines='skip')
        #     for col in result.columns:
        #         if result[col].dtype == np.object_:
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)
            
            
        elif each_key == 'materials_system':
     
            
            results['compound_name'] = results['compound_name'].apply(remove_accents)
            results['description'] = results['description'].apply(remove_accents)
            results['iupac'] = results['iupac'].apply(remove_accents)
            results.to_csv(each_key + ".csv", index=False)
            
        elif each_key == 'materials_reference':
            
   
            results['title'] = results['title'].apply(remove_accents)
            results.to_csv(each_key + ".csv", index=False)

            
        else:
            results.to_csv(each_key + ".csv", index=False)
            
            


