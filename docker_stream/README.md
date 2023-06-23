# Containerized version of the Stream Project 

This is the containerized version of the RDF counterpart of the Nomad and Hybri Database produced by TIB in the context of the Stream project.
In order to automate the transformation process and control the intermediate and final outputs, a CI/CD automation pipeline has been employed.
The pipeline is maintained under the same source control and versioning mechanisms to facilitate access, configuration, and re-execution. 

Separate steps has been used for diffrenet database, three databases has been used for the rdf transformation, Nomad, Hybrid and Dsms. 

For Nomad, 
The pipeline is composed of a sequence of steps, each performing a set of related operations e.g., fetching data from the Nomad database, cleaning, 
transforming into RDF triples, storing the triples in the triple store GraphDB, querying, validating the triples and converting the formulas in cannonical form.

For Hybrid,
For the rdf transformation of Hybrid database, the pipeline takes the data from mysql bacdive database,
cleans it and transform the hybrid data into the rdf form, store the data into triple store of choice, querying, validating the triples and converting the formulas in cannonical form.

For Dsms,
The pipeline takes the stored rdf data, stores the triples in the triple store GraphDB, and does querying and validation of the triples.

# In order to run the pipeline and the steps following software and language have been used:
           1 Python
           2 MySQL workbench
           3 Jenkins 
           4 GraphDB 
  In order to install the following software, docker compose has been used which makes the installation of the software much easier and maintainable. 

# Installation prerequisites:

  ## Installation of docker environment:
     1 Update the apt package index and install packages to allow apt to use a repository over HTTPS:
     
         ```
           sudo apt-get update
           sudo apt-get install \
           ca-certificates \
           curl \
           gnupg \
           lsb-release
          
          ```
      2 Add Docker’s official GPG key:
          ```
          sudo mkdir -p /etc/apt/keyrings
          
          curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
       
          
          ```
      3 Use the following command to set up the repository:
          ```
          echo \
         "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
          $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       
          
          ```
       4 Install Docker Engine
       
       
          ```
             sudo apt-get update
             sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
       
          ```
     
 # Executing the docker compose:
 
 1. Create a local path for the Git repository e.g., in C:\Users\<your_user>\github\projects. This will be used as `local_repo_path` in the next steps:

 2. Change to `local_repo_path` 

 3. Clone the GitHub repository to `local_repo_path` 
    ```
     git clone https://github.com/stream-project/WP1R.git
    ```

 4. Access repository:

  ```
     cd WP1R/docker_stream
     
  ```
 5. Run the command:
     ```
     docker compose up
     
     ```
 6. Executing the jenkins pipeline:
    1. Once all the docker is running, go to folder:
    
     ```
     cd WP1R/docker_stream/automate
     
     ```
     2. Run the command:

     ```
     pip3 install python-jenkins
     pip3 install jenkinsapi
     python3 automate.py
     
     ```
     This script contains python file to run all the jobs of jenkins pipeline, this script will take the names of the jobs that we want to run from the file jobs.properties
     which is alsp present in the automate folder.
  
  7. Accessing GraphDB repository.
     once, all the jobs are executed go to: 
      ```
      http://localhost:7200/     
      ```
      and here all the repositories with stored triples are there.
     
