# -*- coding: utf-8 -*-


import jenkins 
import time
from jenkinsapi.jenkins import Jenkins
# It comes with pip module python-jenkins
# use pip to install python-jenkins

# Jenkins Authentication URL

JENKINS_URL = 'http://localhost:8080'
JENKINS_USERNAME = "your_name"
JENKINS_PASSWORD = "your_password"


import configparser


""" reading the path from path.properties file,specify the path of path.properties file """

config = configparser.ConfigParser()

''' specify the path of path.properties file here '''

config.readfp(open('./jobs.properties'))


server = Jenkins(JENKINS_URL, username = JENKINS_USERNAME , password = JENKINS_PASSWORD)


server_build = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)


    
for each_section in config.sections(): 
    for each_key, each_val in config.items(each_section):
        
        print(each_key, each_val)
        
        
        build_number = server_build.get_job_info(each_val)['nextBuildNumber']
    
        server_build.build_job(each_val)
        
    
        time.sleep(30)
        
        
        job_instance = server.get_job(each_val)
        
        latestBuild = job_instance.get_last_build()
        
        if (latestBuild.get_status()) == 'SUCCESS':
            print('job is success', build_number)
        else:
            print('job is failure')
        
        print(server_build.get_build_console_output(each_val,build_number))
        
        
        











    