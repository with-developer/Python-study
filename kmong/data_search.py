import csv
import xmltodict

#2
# Reading xml file
with open("data_test.txt", 'r') as file:
    filedata = file.read()

# Converting xml to python dictionary (ordered dict)
data_dict = xmltodict.parse(filedata)
print(data_dict)
# data_list = dict(data_dict.values())