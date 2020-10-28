import numpy as np
import pandas as pd
import sys
import os

#get the input of directory path
directory_path = sys.argv[1]
#get the inputted extension of file
extension = sys.argv[2]
#get the search parameter
para1 = sys.argv[3]
#set the desired condtional
para2 = sys.argv[4]
#retrieve the desired search parameter
para3 = sys.argv[5]


#looping through list of excel files
for individual_excel_file in os.listdir(directory_path):
    #if the index endswith excel extension carry  out logic
    if individual_excel_file.endswith(str(extension)):
        #create dataframe
        df = pd.read_excel(individual_excel_file)
        #set variable to wanted seaarch parameter/conditional
        programmers = df[para1].where(df[str(para2)] == str(para3)).dropna()
        #brush this up later
        print("File Name: " + individual_excel_file)
        print(programmers)
    else:
        print('no results')
