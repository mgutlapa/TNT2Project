import pandas as pd
import numpy as np
from openpyxl import Workbook

# read by default 1st sheet of an excel file
df1 = pd.read_excel("Health Check 20240626194521.xlsx")
# Firmware Version to match
firmwarever=['SSL3_00_L_1_12']

print("==========================")
print("HealthCheck Input List")
print("==========================")
print(df1)
#print(df1["Firmware Version"][0])

while True:
    print("\n")
    print("*****************************")
    IMEI = input("Scan the IMEI barcode: ")
    #print(f"Scanned unit {IMEI}")
    #match = df1.loc[df1["IMEI"] == int(IMEI)]
    #print (len(match))
    #print (match)
    #print (match["Firmware Version"])
    
    if IMEI == "exit" or IMEI == "Exit" or IMEI == "EXIT" :
        exit()
    if len(df1.loc[df1["IMEI"] == int(IMEI)]) == 1 :
        #Find the dataframe row and store into new dataframe
        df2 = df1.loc[df1["IMEI"] == int(IMEI)]
        if len( df2[df2['Firmware Version'].isin(firmwarever)]) == 1 :
            #print (df2['Firmware Version'])
            print ("Pass")
        else :
            print (df2['Firmware Version'])
            print ("Fail")
    if len(df1.loc[df1["IMEI"] == int(IMEI)]) != 1 :
        print ("Unit does not exist in list")
    print("*****************************")