import pandas as pd
import csv as csv

# This function reads a CSV file and creates a HTML table from it
def csv_to_html():
    csv_data = pd.read_csv('file.csv', index_col=False)
    return(csv_data.to_html(justify='center'))

def csv_reader():
    header = []
    csv_data = pd.read_csv('file.csv', index_col=False)
    for row in csv_data:
        header.append(row)
    csv_data = csv_data.to_dict()    
    return(header, csv_data)

print(csv_reader()[0])
print(csv_reader()[1])

print('#########')