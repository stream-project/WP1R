# Steps to transform [Hybrid data](https://materials.hybrid3.duke.edu/) into RDF by using [SDM-RDFIzer](https://github.com/SDM-TIB/SDM-RDFizer) and [RML](https://rml.io/specs/rml/#overview-0) mapping rules 
 
   
## Db_to_csv Folder:
     1. Contains python script that will connect to the mysql workbench and then will transform its tables into csv format, there is also a separate config file 
        to add the table names and querties that we want. 
     2. Contains some of the generated csv files based on the table names. 
     
## rdf_map Folder
     1. Contains SDM-RDfizer tool and a python file to create config file that will be used to run the SDM-RDFizer. 
     2. Inside SDM-RDFizer, there is a folder named exam  and inside this folder, we have some mapping rules files that is used to 
        convert the csv file into rdf transformations. There is one folder output which is used to store the rdf transformed files. 
     3. rdf.py has a parameter "number_of_datasets", currently we are transforming six csv files that's why the parameter is set to six and can be changed accoring to the number of csv files.
    
 For detailed information on SDM-RDFizer please visit [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer)

## store_to_graph
    1. Contains python script to store generated rdf files into the graph database. 
    
## Query
    1. Contains script to query the rdf files store in th egraph database. 
    
## We have used jenkins pipeline for the above steps, our pipeline will transform the database tables into csv and then will create rdf transformations of those csv file, will store it into the graph databse and will query the rdf files stored in the database. We have created four jobs for that, one job for each step. 
    1. In the Jobs folder, there are config files for each job. 
    
# Steps to run jenkins jobs: 
     1. Install jenkins and create four freestyle jobs:
            - db_to_csv
            - rdf_map
            - store_to_graph
            - query 
     2. After installing jenkins; go the .jenkins folder in your directory where jenkins has been installed, now go the workspace folder inside the .jenkins folder, there you will see workspace has already been created for the 4 freestyle projects that you have created. 
     
     3. Copy the contents of the above folders (db_to_csv, rdf_map, store_to_graph, query) respectively. 
 
 # Inside the automate folder there are two files:
     1. 
    
