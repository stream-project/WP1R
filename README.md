# WP1R
STREAM WP1: MatVoc Ontology Entwicklung

# Performance Comparison of uploading and querying RDF Triples of following repositories: 
           1. GraphDB
           2. RDFox
           3. ALllegroGraph
           4. Virtuoso

In the Experiment folder we have two sub-folders and two files, file "Queries.txt" has all the queries that are used for comparing time of uploading and querying rdf triples of the above mentioned repositories and the file named "comparison of uploading and querying triples" has uploading and querying time comparison of the four repositories used in our work.

## Sub-folder "datasets" consists of all the datasets used in our work, it has Four RDF files namely:
          1. person.ttl: which contains details of the person's like first and last names.
          2. company.ttl: which contains details of the company.
          3. relation.ttl: which defines the relation between person and the company.
          4. company_relation.ttl: it is the combined version of relation and company datasets.
          
### Sub-folder "scripts" has two folders in it:
          1. upload_script: which contains four python scripts that we have used to upload the triples into the repositories and to measure the uploading time.
          2. query_script: It also contains python scripts that we have used to query the above mentioned repositories. 
          
    Note: Inside the query_script, there is another folder named "rdfox" which contains python script that we have 
    used to query rdfox and also it contains one text file which has three queries that we have used with 
    Jena Fuseki Server. 
          
         
