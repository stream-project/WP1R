##  In order to automate the transformation process, as well as the intermediate and final outputs, a CI/CD automation pipeline has been employed. The pipeline is maintained under the same source control and versioning mechanisms to facilitate access, configuration, and re-execution. The pipeline is composed of a sequence of steps, each performing a set of related operations e.g., fetching data from the Nomad database, cleaning, transforming into RDF triples, storing the triples in the triple store GraphDB, and querying and validating the triples.

## For the rdf transformation of Nomad database, The pipeline is used which takes the data from Nomad api's, cleans it and transform the data into the rdf form and finally store the data into triple store (GraphDB is used ),
## Jenkins
Jenkins is used to execute the pipeline, pipeline consists of following jobs:

Nomad_dcat, It transforms the dcat compatible metadata into rdf.
Nomad_metadata, This job converts metadata about materials from Nomad database into matvoc compatible rdf. 
Nomad_method, Tranforms method used for performing calculations into matvoc compatible rdf
Nomad_observation, It output matvoc annotated rdf representations of single configuration calculations.
Nomad_store_to_graph, this job stores geberated rdf into Graphdb 
Nomad_query, For querying the database, (tested the database on few queries provided by experts)
Nomad_validate, This job is used to validate the query results.
Nomad_clean_workspace, Once the rdf files are stored in the database, this job can be executed to clean up the workspace.

3. GraphDB

We have used GraphDB to store transformed RDF triples, for querying the triples ( used several sparql queries ) and for the visualization of the knowledge graph. 

                                "Hybrid database"
								
This is the containerized version of the RDF counterpart of the Hybrid database produced by TIB in the context of the Stream project.

Created rdf reprentation of Hybrid database using sdm-rdfizer and rml mapping rules.

For the rdf transformation of Hybrid database, we have used the pipeline which takes the data from mysql bacdive database,
cleans it and transform the hybrid data into the rdf form and finally store the data into triple store (
We have used GraphDB for this )

Tools used for the transformation

1. Docker
2. Jenkins
3. MySQL
4. GraphDB

1. Docker

In order to automate the transformation process and control the input tables as well as the intermediate and final outputs, a CI/CD automation pipeline has been employed.
The pipeline is maintained under the same source control and versioning mechanisms to facilitate access, configuration, and re-execution. 
The pipeline is composed of a sequence of steps, each performing a set of related operations e.g., fetching data from the Hybrid database, converting into csv, cleaning, transforming into RDF triples, storing the triples in the triple store, and querying and validating the triples.

For the rdf transformation of Hybrid database, we have used the pipeline which takes the data from mysql bacdive database,
cleans it and transform the hybrid data into the rdf form and finally store the data into triple store (
We have used GraphDB for this ).

2. Jenkins 

Jenkins is used to execute the pipeline, pipeline consists of following jobs:
Hybrid_db_to_csv, This job converts database into csv form and cleans the database. 
Hybrid_rdf_map, This transform csv files into rdf.
Hybrid_store_to_graph, This stores the rdf triples into triple store ( graphdb ).
Hybrid_query, For querying the triple store.
Hybrid_validate, This job is used to validate the query results.
Hybrid_clean_workspace, Once the rdf files are stored in the database, this job can be executed to clean up the workspace.

3. MySQL

We used MySQl database to load Hybrid database dump and then used it to convert them into csv files to further transform them into rdf.  

4. GraphDB

Graphdb is used here also to store transformed rdf files from Hybrid database, used several sparql queries for testing the knowledge graph. 


Also, to find the common materials between both the databases ( hybrid, Nomad ), we have
created another job ( Hybrid_canonical_form and Nomad_canonical_form )for the both the databases which converts the formulas 
into cannonical form whoich can be further used in sparql query to identify the common materials 
between both the databases
