# Pipeline for Nomad Database

									
This is the containerized version of the RDF counterpart of the Nomad database produced by TIB in the context of the Stream project.
Created matvoc annotated rdf rtepresentation of the Nomad Dataset using ssn and sosa ontology.
Used rdflib library for generating rdf.


Tools used to transform Nomad database into rdf are:

1. Docker, 
2. jenkins, 
3. GraphDB 

## Docker

Used docker container to run the services; jenkins, graphdb 

In order to automate the transformation process, as well as the intermediate and final outputs, a CI/CD automation pipeline has been employed.
The pipeline is maintained under the same source control and versioning mechanisms to facilitate access, configuration, and re-execution. 
The pipeline is composed of a sequence of steps, each performing a set of related operations e.g., fetching data from the Nomad database, cleaning, transforming into RDF triples, storing the triples in the triple store GraphDB, and querying and validating the triples.

For the rdf transformation of Nomad database, the pipeline is used which takes the data from Nomad api's,
cleans it and transform the data into the rdf form and finally store the data into triple store (
We have used GraphDB for this ).

## Jenkins
Jenkins is used to execute the pipeline, pipeline consists of following jobs:

	Nomad_dcat: It transforms the dcat compatible metadata into rdf.
	Nomad_metadata: This job converts metadata about materials from Nomad database into matvoc compatible rdf. 
	Nomad_method: Tranforms method from nomad database used for performing calculations into matvoc compatible rdf.
	Nomad_observation: It output matvoc annotated rdf representations of single configuration calculations.
	Nomad_store_to_graph: this job stores geberated rdf into Graphdb.
	Nomad_query: For querying the database, (tested the database on few queries provided by experts).
	Nomad_validate: This job is used to validate the query results.
	Nomad_clean_workspace: Once the rdf files are stored in the database, this job can be executed to clean up the workspace.

## GraphDB

GraphDB is used to store transformed RDF triples, for querying the triples ( used several sparql queries ) and for the visualization of the knowledge graph. 

# Pipeline for Hybrid Database
								
This is the containerized version of the RDF counterpart of the Hybrid database produced by TIB in the context of the Stream project.

Created rdf reprentation of Hybrid database using sdm-rdfizer and rml mapping rules.

For the rdf transformation of Hybrid database, the pipeline is used which takes the data from mysql hybrid database,
cleans it and transform the hybrid data into the rdf form and finally store the data into triple store.

Tools used for the transformation

1. Docker
2. Jenkins
3. MySQL
4. GraphDB

## Docker

In order to automate the transformation process and control the input tables as well as the intermediate and final outputs, a CI/CD automation pipeline has been employed.
The pipeline is maintained under the same source control and versioning mechanisms to facilitate access, configuration, and re-execution. 
The pipeline is composed of a sequence of steps, each performing a set of related operations e.g., fetching data from the Hybrid database, converting into csv, cleaning, transforming into RDF triples, storing the triples in the triple store, and querying and validating the triples.

## Jenkins 

Jenkins is used to execute the pipeline, pipeline consists of following jobs:

	Hybrid_db_to_csv: This job converts database into csv form and cleans the database. 
	Hybrid_rdf_map: This transform csv files into rdf.
	Hybrid_store_to_graph: This stores the rdf triples into triple store ( graphdb ).
	Hybrid_query: For querying the triple store.
	Hybrid_validate: This job is used to validate the query results.
	Hybrid_clean_workspace: Once the rdf files are stored in the database, this job can be executed to clean up the workspace.

## MySQL

MySQl database is used to load Hybrid database dump and then used it to convert them into csv files to further transform them into rdf.  

## GraphDB

Graphdb is used here to store transformed rdf files from Hybrid database, used several sparql queries for testing the knowledge graph. 


## NOTE: Also, to find the common materials between both the databases ( hybrid, Nomad ), another job is created  ( Hybrid_canonical_form and Nomad_canonical_form ) for the both the databases which converts the formulas into cannonical form whoich can be further used in sparql query to identify the common materials between both the databases. To find the common materials between Hybrid and Nomad, following jobs can be executed in jenkins pipeline:

        Hybrid_canonical_form: convert the formulas from hybrid database into canonical form.
        Nomad_canonical_form: convert the formulas from hybrid database into canonical form.
        Cannonical_formulas: executing this job will find the common formulas between both the databases. 


 ## Running all the jobs:

 In this directory, there is a folder named automate with two files:
             
    jobs.properties: here all the jobs can we mentioned that needs to be executed.
    automate.py: running this script will run all the jobs in the jenkins.




