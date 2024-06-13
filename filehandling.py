'''
#'r'read and 'w' write the file
file = open("C:\\Users\ms900\OneDrive\Desktop\sample.txt","w")
#file.read()
file.write("my first read the file")
'''
#view data from csv file
import csv
with open("C:\\Users\ms900\OneDrive\Desktop\samples.csv") as new :
    data = csv.reader(new)
    for i in data:
        print(i)
'''
#anothe file
import csv
with open("C:\\Users\ms900\OneDrive\Desktop\samples.pptx",'w') as d:
    get = d.write("hi welcom")
'''