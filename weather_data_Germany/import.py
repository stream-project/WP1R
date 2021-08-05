# -*- coding: utf-8 -*-




import pandas as pd
from wetterdienst import Wetterdienst
import pickle

API = Wetterdienst("dwd", "observation")
request = API(
    parameter=["climate_summary"],
    resolution="daily",
    start_date="2010-01-01",  # Timezone: UTC
    end_date="2021-01-01",  # Timezone: UTC
    tidy=True,# default, tidy data
    humanize=True,).all()



stations = request.df  # station list

stations.to_csv(r'C:\Users\GuptaR\Desktop\test_all\station_details_v.csv', encoding='utf-8', index=False)

# with open(r'C:\Users\GuptaR\Desktop\repo_all\un.txt', "wb") as fp:   
#     pickle.dump(un, fp)


all_ids = stations['station_id'].unique()
all_ids = all_ids.tolist()

type(all_ids)
len(all_ids)


un=[]


# with open(r'C:\Users\GuptaR\Desktop\repo_all\un.txt', "wb") as fp:   
#     pickle.dump(un, fp)

with open(r'C:\Users\GuptaR\Desktop\repo_all\un.txt', "rb") as fp:
    v = pickle.load(fp)

un = v

len(un)

number = 5
length = len(un) + number
print(length)
un1 = []
for j in all_ids[0:length]:
        if j not in un:
            un.append(j)
            un1.append(j)


len(un1) 
un1  
un
len(un)

# i = [i for i in all_ids[initial:length]]

# print(i)

request = API(
    parameter=["climate_summary"],
    resolution="daily",
    start_date="2010-01-01",  # Timezone: UTC
    end_date="2021-01-01",  # Timezone: UTC
    tidy=True,# default, tidy data
    humanize=True,).filter_by_station_id(station_id=(un1))



stations = request.df  # station list

stations.to_csv(r'C:\Users\GuptaR\Desktop\repo_all\station_details_v2.csv', encoding='utf-8', index=False)


values = request.values.all().df  

values.to_csv(r'C:\Users\GuptaR\Desktop\repo_all\station_values_v2.csv', encoding='utf-8', index=False)

with open(r'C:\Users\GuptaR\Desktop\repo_all\un.txt', "wb") as fp:   
    
    pickle.dump(un, fp)
    





