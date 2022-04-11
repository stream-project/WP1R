# -*- coding: utf-8 -*-





import os 

import sys

# import pypyodbc as podbc

import pandas as pd 

import mysql.connector

from rdflib import Graph

from pathlib import Path

import pickle

import configparser




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
    host = 'localhost',
    user = 'root',
    passwd = '8227',
    database= 'hybrid')

# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("select database();")

database = mycursor.fetchone()

print(database)


# i = 0
    
for each_section in config.sections(): 
    for each_key, each_val in config.items(each_section):
        
        query = each_val
            
  
        # query = 'select * from materials_dataset' 
        
        results = pd.read_sql_query(query, mydb)
        
        if each_key == 'materials_dataset':
            
            results['secondary_property_id'] =  results['secondary_property_id'].astype('Int64')
            results.to_csv(each_key + ".csv", index=False)
            
        else:
            
            
            results.to_csv(each_key + ".csv", index=False)
            

        



