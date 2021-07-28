# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:01:33 2021

@author: GuptaR
"""



import pandas as pd
from wetterdienst import Wetterdienst

API = Wetterdienst("dwd", "observation")
request = API(
    parameter=["climate_summary"],
    resolution="daily",
    start_date="2010-01-01",  # Timezone: UTC
    end_date="2021-01-01",  # Timezone: UTC
    tidy=True,# default, tidy data
    humanize=True,).filter_by_station_id(station_id=(44,73,78,90,420,1078,1975,2014,3379,4931))



stations = request.df  # station list

stations.to_csv(r'C:\Users\GuptaR\Desktop\test_all\station_details_v.csv', encoding='utf-8', index=False)



values = request.values.all().df  

values.to_csv(r'C:\Users\GuptaR\Desktop\test_all\station_values_1.csv', encoding='utf-8', index=False)





