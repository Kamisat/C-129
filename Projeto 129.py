from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
import numpy

def merge():

    brown_darfs_data = pd.read_csv("brown_dwarfs_data.csv")
    bright_star = pd.read_csv("scraped_data.csv")
    temp_list = []

    for i in range(0, len(brown_darfs_data.Radius)):
        if float(brown_darfs_data.Radius[i]) != brown_darfs_data.Radius[i]:
            temp_list.append(i)
        brown_darfs_data.Radius[i] = float(brown_darfs_data.Radius[i]) * 0.102763

    
    for i in range(0, len(brown_darfs_data.Distance)):
        if float(brown_darfs_data.Distance[i]) != brown_darfs_data.Distance[i]:
            temp_list.append(i)

    
    for i in range(0, len(brown_darfs_data.Mass)):
        if float(brown_darfs_data.Mass[i]) != brown_darfs_data.Mass[i]:
            temp_list.append(i)
        brown_darfs_data.Mass[i] = float(brown_darfs_data.Mass[i]) * 0.000954588


    
    brown_darfs_new_data = brown_darfs_data.drop(labels = temp_list)


    print(temp_list)
    print(brown_darfs_new_data)

    
    headers = ["Name", "Radius", "Mass", "Distance"]
    dataframe = pd.DataFrame(brown_darfs_new_data, columns = headers)
    dataframe.to_csv("brown_dwarfs_new_data.csv",  index = True, index_label = "id")

    merge_dataframe = pd.merge(brown_darfs_new_data, bright_star, on = 'id')
    merge_dataframe.shape
    merge_dataframe.to_csv("finaL_dataframe.csv",  index = True, index_label = "id")


merge()
