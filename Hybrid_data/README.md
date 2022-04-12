# This Folder contains four sub-folder: 
  
     1 db_to_csv : which contains script to transform hybrid database into csv files, we can also the the generated csv files in the folder.
     2 rdf_map :   It contains folders, scripts and mapping rules to convert csv files into rdf transfomation.
     3 store_to_graph: It contains script to store rdf files into Graph Database(GraphDB)
     4 Query: Contains query to run against the rdf files. 
       
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
    1. 
