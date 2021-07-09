# -*- coding: utf-8 -*-

# import libraries

import os
import sys
from franz.openrdf.repository.repository import Repository
import time
from franz.openrdf.sail.allegrographserver import AllegroGraphServer
from franz.openrdf.connect import ag_connect
from franz.openrdf.rio.rdfformat import RDFFormat

# connecting to allegrograph and printing number of repositories present in it

print("Connecting to AllegroGraph server --",
      "host:'%s' port:%s" % ('127.0.0.1', '10035'))
server = AllegroGraphServer('127.0.0.1', '10035',
                            'test', 'rohit')



print("Available catalogs:")
for cat_name in server.listCatalogs():
    if cat_name is None:
        print('  - <root catalog>')
    else:
        print('  - ' + str(cat_name))
        
        
catalog = server.openCatalog('')
print("Available repositories in catalog '%s':" % catalog.getName())
for repo_name in catalog.listRepositories():
    print('  - ' + repo_name)



''' query 1'''

conn = ag_connect('repo1', host='127.0.0.1', port='10035',
                user='test', password='rohit', create=True) 


start = time.time()


query_string = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

select (count(*) as ?triples)

where{
        { ?s a ab:Person;
             ?p ?o.}
      } '''

with conn.executeTupleQuery(query_string ) as result:
    df = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 

df.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query1.csv',sep='\t',encoding='utf-8')


''' query 2'''

conn = ag_connect('repo1', host='127.0.0.1', port='10035',
                user='test', password='rohit', create=True) 


start = time.time()


query_string = '''PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT ?first ?last
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
} '''

with conn.executeTupleQuery(query_string ) as result:
    query2 = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 

query2.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query2.csv',sep='\t',encoding='utf-8')
 
# print(query2.head())

 
'''  combining both repositories (repo1 and repo2) to query both the databases for the queries which uses triples from both 
repositories  '''

# connecting repo1
conn = ag_connect('repo1', host='127.0.0.1', port='10035',
                user='test', password='rohit', create=True) 



### triple count
print('triples size (default graph): {count}'.format(count=conn.size()))

# connecting repo2
conn = ag_connect('repo2', host='127.0.0.1', port='10035',
                user='test', password='rohit',  create=True) 

### triple count
print('triples size (default graph): {count}'.format(count=conn.size()))



### combining both repositories 

conn = server.openFederated(['repo1', 'repo2']) 


### triple count
print('triples size (default graph): {count}'.format(count=conn.size()))


''' query3'''
start = time.time()


query="""
        PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT ?last ?first ?c
WHERE
{
  
  ?s a ab:Person.  
  ?s ab:firstname ?first ;
     ab:lastname ?last . 
  
   
        ?s ab:employedat d:8254. 
        
    
   
         d:8254 a ab:Company.
         d:8254 ab:hasname ?c. 
        
} """
        
with conn.executeTupleQuery(query) as result:
    query3 = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 

query3.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query3.csv',sep='\t',encoding='utf-8')

# print(query3.head())

'''query4'''
start = time.time()


query="""
       PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 


SELECT (count(?c) as ?total_companies)

where{

SELECT DISTINCT ?c 

WHERE
{ 
        
  
            ?s ab:employedat ?c.}
        
} """
        
with conn.executeTupleQuery(query) as result:
    query4 = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 

query4.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query4.csv',sep='\t',encoding='utf-8')




'''query5'''
start = time.time()


query="""
       PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT DISTINCT ?c_id ?c_name ?c_emp

WHERE
{ 
      
  
            ?s ab:employedat ?c_id.
      
        ?c_id a ab:Company.
         ?c_id ab:hasname ?c_name;
               ab:hasempnumber ?c_emp.
 
            
        
        
} """
        
with conn.executeTupleQuery(query) as result:
    query5 = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 

query5.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query5.csv',sep='\t',encoding='utf-8')

# print(query5.head())


'''query6'''
start = time.time()


query="""
       PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT (count(distinct concat(str(?first), str(?last))) as ?unique)
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}"""
        
with conn.executeTupleQuery(query) as result:
    query6 = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 


query6.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query6.csv',sep='\t',encoding='utf-8')



'''query7'''
start = time.time()


query="""
       PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
  

SELECT ?first ?last 
(count(concat(str(?first), str(?last))) as ?unique)
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}
group by ?first ?last """
        
with conn.executeTupleQuery(query) as result:
    query7 = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 

query7.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query7.csv',sep='\t',encoding='utf-8')

# print(query7.head())


'''query8'''
start = time.time()


query="""
       PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT ?c_name  ?first ?last 

WHERE
{     
      ?s a ab:Person;
         ab:firstname ?first;
            ab:lastname ?last.
    
    
  
            ?s ab:employedat ?c_id.
    
        ?c_id a ab:Company.
         ?c_id ab:hasname ?c_name;
               
 
            
        
        
    } LIMIT 500 """
        
with conn.executeTupleQuery(query) as result:
    query8 = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 

query8.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query8.csv',sep='\t',encoding='utf-8')

# print(query8.head())

'''query9'''
start = time.time()


query="""
       PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
PREFIX d:  <http://learningsparql.com/ns/data#>
Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

select (count(?s) as ?unique)
where{
SELECT  ?s ?first ?last
WHERE
{
 ?s a ab:Person;
    ab:firstname ?first;
    ab:lastname ?last.
}
}
 """
        
with conn.executeTupleQuery(query) as result:
    query9 = result.toPandas()

end = time.time()

print('time taken to execute the query :', end -   start)

''' storing results locally ''' 

query9.to_csv(r'C:\Users\GuptaR\Desktop\results\allegrograph\query9.csv',sep='\t',encoding='utf-8')

# print(query9.head())








