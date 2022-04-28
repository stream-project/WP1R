# Steps to transform [Nomad data](https://nomad-lab.eu/) into RDF by using [RDFlib](https://rdflib.readthedocs.io/en/stable/)
 
   
## Nomad_metadata Folder:
     1. Contains python script that will connect to the mysql workbench and then will transform its tables into csv format, there is also a separate config file 
        to add the table names and querties that we want. 
     2. Contains some of the generated csv files based on the table names. 
     
## Nomad_method Folder
     1. Contains SDM-RDfizer tool and a python file to create config file that will be used to run the SDM-RDFizer. 
     2. Inside SDM-RDFizer, there is a folder named exam  and inside this folder, we have some mapping rules files that is used to 
        convert the csv file into rdf transformations. There is one folder output which is used to store the rdf transformed files. 
     3. rdf.py has a parameter "number_of_datasets", currently we are transforming six csv files that's why the parameter is set to six and can be changed accoring to the number of csv files.
    
 For detailed information on SDM-RDFizer please visit [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer)

## Nomad_observation Folder
    1. Contains python script to store generated rdf files into the graph database. 
    
   Go the graph database instance to see the files in it "http://194.95.157.29:7201/"
    
## Query_nomad Folder
    1. Contains script to query the rdf files store in the graph database. 
    2. We can also see the result of the query inside this folder. 
    
## We have used jenkins pipeline for the above steps, our pipeline will transform the database tables into csv and then will create rdf transformations of those csv file, will store it into the graph databse and will query the rdf files stored in the database. We have created four jobs for that, one job for each step. 
    1. In the Jobs folder, there are config files for each job. 
    2. copy these config files to your job folder inside your jenkins directory respectively.
    3. Go to your jenkins local instance and click on manage jenkins there we have "reload configuration from disk" option, click on this option. 
## Steps to create jenkins jobs: 
     1. Install jenkins and create four freestyle jobs:
            - db_to_csv
            - rdf_map
            - store_to_graph
            - query 
     2. After installing jenkins; go the .jenkins folder in your directory where jenkins has been installed, now go the workspace folder inside the .jenkins folder, there you will see workspace has already been created for the 4 freestyle projects that you have created. 
     
     3. Copy the contents of the above folders (db_to_csv, rdf_map, store_to_graph, query) respectively. 
 
 ## Inside the automate folder there are two files:
     1. automate.py, is a python script to run our jenkins pipeline from any IDE'S or terminal.  
     2. jobs.properties is a config file, where we can specify the jobs and their order of execution. 
     
 ## Steps to run complete jenkins pipeline
     1. create a folder "automate" on your pc and copy automate.py and jobs.properties into it, please change the username and password of your jenkins instance inside the automate.py file 
On the terminal run <mark> "python automate.py" </mark> and you can see the results whether the job is success or failure on your terminal. Go to the jenkins workspace to check the outputs.