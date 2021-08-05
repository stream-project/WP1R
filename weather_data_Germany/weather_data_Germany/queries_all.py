# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 12:58:44 2021

@author: GuptaR
"""

from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import sparql_dataframe


# query1 

start = time.time()

endpoint = "http://localhost:7200/repositories/features"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#> 
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 



select ?feature ?sample ?sensor ?prop ?label ?result
where{
      ?feature a ?f.
      ?sample  sosa:isSampleOf ?feature.
      ?prop a ssn:Property.
    
  SERVICE <http://localhost:7200/repositories/platforms>{
        
    ?sensor a sosa:Sensor;
     sosa:observes ?prop.
    }
        SERVICE <http://localhost:7200/repositories/observations>{
      base:54960331temperature_air_200  a sosa:Observation;
           rdfs:label ?label;
           sosa:madeBySensor ?sensor;
          sosa:hasFeatureOfInterest ?sample;
          sosa:hasResult ?bl.
     ?bl qudt:numericValue ?result.
         }}
"""
df = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query1.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query1.csv" ,na_rep='NaN', header=None, mode='a')


# query2 platforms

start = time.time()

endpoint = "http://localhost:7200/repositories/features"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#> 
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 

select ?feature ?FOI ?prop ?label ?sensor
where{
    ?feature a ?FOI.
   base:sample90 sosa:isSampleOf ?feature;
     ssn:hasProperty ?prop.
    ?prop a ssn:Property;
       rdfs:label ?label.
SERVICE <http://localhost:7200/repositories/platforms> {
        ?sensor sosa:observes ?prop.
       
    }}
"""
df1 = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df1.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query2.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df1.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query2.csv" ,na_rep='NaN', header=None, mode='a')

# query3 platforms details

start = time.time()

endpoint = "http://localhost:7200/repositories/features"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

select ?station_id ?label ?lat ?lon ?alt 
where{
    SERVICE <http://localhost:7200/repositories/platforms> {
    
    ?station_id a sosa:Platform;
           rdfs:label ?label;
           geo:lat ?lat;
           geo:lon ?lon;
            geo:alt ?r.
    ?r qudt:numericValue ?alt.
}
}
"""
df2 = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df2.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query3.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df2.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query3.csv" ,na_rep='NaN', header=None, mode='a')

# query4 total samples

start = time.time()

endpoint = "http://localhost:7200/repositories/features"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

select ?sample
where{
    ?feature a ?FOI.
    
    ?sample sosa:isSampleOf ?feature.
}
"""
df3 = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df3.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query4.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df3.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query4.csv" ,na_rep='NaN', header=None, mode='a')

## query 5 count triples in each repo


start = time.time()

endpoint = "http://localhost:7200/repositories/features"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#> 
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 

select ((?co+?com+?co2) as ?total_triples_features)
((?co1+?b1+?com1) as ?total_triples_platforms)
 ((?co3+?co4+?co5) as ?total_triples_observations)

{
    {
        select (count(?s) AS ?co)
        { ?s a sosa:FeatureOfInterest ;
             ?o ?p.}
  }
    {
        select (count(?d) AS ?com) 
        { ?d a sosa:Sample;
             ?w ?q.} 
    
    
    
    }
              
              {
        select (count(?s2) AS ?co2)
        { ?s2 a sosa:ObservableProperty ;
             ?o1 ?p1.}
        }
        
        SERVICE <http://localhost:7200/repositories/platforms>{
           {
        select (count(?s1) AS ?co1)
        { ?s1 a sosa:Platform ;
             ?o2 ?p2.}
  }
                {
          select (count(?p2) AS ?b1) 
        { 
            ?p2  a qudt:quantityValue;
                ?q1 ?q2.
       
       } 
        }
        
        {
        select (count(?d1) AS ?com1) 
        { ?d1 a sosa:Sensor;
             ?w ?q.} 
    
    
    
    }
        }
     SERVICE <http://localhost:7200/repositories/observations> {
        {

select (count(?s3) AS ?co3)
        { ?s3 a sosa:Observation ;
             ?o ?p.}
        }
      
      {
     select (count(?p) AS ?co4)
        { ?p a qudt:quantityValue;
             ?p1 ?p2.
             }
        }
           
           {
     select (count(?p) AS ?co5)
        { ?p a time:Instant;
             ?p3 ?p4.
             }
        }
    
    }}
"""
df4 = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df4.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query5.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df4.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query5.csv" ,na_rep='NaN', header=None, mode='a',index=False)

df4.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query5.csv",index=False)

## query 6 sample 1 info


start = time.time()

endpoint = "http://localhost:7200/repositories/features"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

## retrieving all observations for a particular properties of sample1

select ?sample ?prop ?sensor ?result
where{
    ?feature a ?FOI.
    ?sample sosa:isSampleOf ?feature;
            ssn:hasProperty ?prop.
    SERVICE <http://localhost:7200/repositories/platforms>{
        
        ?sensor sosa:observes ?prop
          
    }
    SERVICE <http://localhost:7200/repositories/observations>{
        ?ob a sosa:Observation;
            sosa:madeBySensor ?sensor;
            sosa:hasResult ?r.
        ?r qudt:numericValue ?result.
        
       
    }
        Filter(?sample = base:sample1)
 
}
"""
df5 = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df5.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query6.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df5.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query6.csv" ,na_rep='NaN', header=None, mode='a')

## prop info

## query 7 prop info


start = time.time()

endpoint = "http://localhost:7200/repositories/features"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

## retrieving all observations for a particular properties of sample1

select ?sample ?prop ?sensor ?result
where{
    ?feature a ?FOI.
    ?sample sosa:isSampleOf ?feature;
            ssn:hasProperty ?prop.
    SERVICE <http://localhost:7200/repositories/platforms>{
        
        ?sensor sosa:observes ?prop
          
    }
    SERVICE <http://localhost:7200/repositories/observations>{
        ?ob a sosa:Observation;
            sosa:madeBySensor ?sensor;
            sosa:hasResult ?r.
        ?r qudt:numericValue ?result.
        
       
    }
        Filter(?prop = base:temperature_air_min_005)
 
}
"""
df6 = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df6.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query7.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df6.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query7.csv" ,na_rep='NaN', header=None, mode='a',index=False)

## query 8 station_details


start = time.time()

endpoint = "http://localhost:7200/repositories/features"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#>
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>


select ?sample ?prop ?station ?lat ?lon ?alt ?result
where{
    ?feature a ?FOI.
    ?sample sosa:isSampleOf ?feature;
            ssn:hasProperty ?prop.
    SERVICE <http://localhost:7200/repositories/platforms>{
        
        ?sensor sosa:observes ?prop.
        ?station sosa:hosts ?sensor;
                 geo:lat ?lat;
                 geo:lon ?lon;
                 geo:alt ?a.
        ?a qudt:numericValue ?alt.
          
    }
    SERVICE <http://localhost:7200/repositories/observations>{
        ?ob a sosa:Observation;
            sosa:madeBySensor ?sensor;
            sosa:hasResult ?r.
        ?r qudt:numericValue ?result.
        
       
    }
        Filter(?sample = base:sample1 && ?prop = base:temperature_air_200)
 
}
"""
df7 = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df7.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query8.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df7.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query8.csv" ,na_rep='NaN', header=None, mode='a',index=False)





## query 9 rdf


start = time.time()

endpoint = "http://localhost:7200/repositories/observations"

g = """PREFIX base: <http://example.org/data/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX cdt: <http://w3id.org/lindt/custom_datatypes#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX qudt: <http://qudt.org/2.1/schema/qudt#> 
PREFIX qudt_unit: <http://qudt.org/2.1/vocab/unit#> 
select ?s ?p ?o ?o1 ?p2 ?o2 ?o3 ?p4 ?o4

where{
    

    { ?s a sosa:Observation;
        ?p ?o.
        FILTER(?s = base:60633601humidity)}
UNION
{
      ?s1 ?p1 ?o1.
    ?o1 a qudt:quantityValue;
       ?p2 ?o2.
         

   FILTER (?s1 = base:60633601humidity)}
 union
    {
             ?s2 ?p3 ?o3.
    ?o3 a time:Instant;
       ?p4 ?o4.
         

   FILTER (?s2 = base:60633601humidity)
        
        
    }
    
}
"""
df8 = sparql_dataframe.get(endpoint, g)

end = time.time()

print('time taken to execute the query',end -   start)

pd.DataFrame(columns=df8.columns).to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query9.csv", index=False)
#alternative for empty df
#df.iloc[:0].to_csv("test.csv", index=False)
df8.to_csv(r"C:\Users\GuptaR\Desktop\repo_all\results\query9.csv" ,na_rep='NaN', header=None, mode='a')
