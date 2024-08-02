import csv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# file_name = os.path.join(BASE_DIR / 'employee_data.csv')
# file_name = os.path.join(BASE_DIR / 'username.csv')
file_name = os.path.join(BASE_DIR / 'clients_data.csv')

fields = []
rows = []

# Read the CSV file as a csv object
# with open(file_name, 'r') as csvFile:
#     csv_reader = csv.reader(csvFile, delimiter=';') # Convert the file csv_reader object

#     fields = next(csv_reader) # To extract field names through first row

#     for i in csv_reader:rows.append(i)

#     total_rows = csv_reader.line_num # A counter returns the rows that have been iterated

# for row in rows:
#     for col in row: print(col)


# Read the CSV file as a dictionary
# with open(file_name, 'r') as csvFile:
#     # DictReader read each row of the file as a dictionary
#     csv_reader = csv.DictReader(csvFile, delimiter=';')

#     data_obj = []

#     for row in  csv_reader: data_obj.append(row)

# for i in data_obj: print(i['Username'])


# Write into CSV file 
# with open(file_name, 'w') as csvFile:
#     fields = ['id', 'username', 'gender']
#     rows = [[1, 'james', 'male'], [2, 'maria', 'female'], [3, 'dexter', 'male'], [4, 'stephen', 'male']]

#     csv_writer = csv.writer(csvFile) # Create a CSV writer object

#     csv_writer.writerow(fields) #  writing the fields
#     csv_writer.writerows(rows) #  writing the rows


# Write into CSV file with dictionary data
with open(file_name, 'w') as csvFile:
    fields = ['id', 'username', 'gender']
    rows = [
        {'id': 1, 'username': 'james', 'gender': 'male'},
        {'id': 2, 'username': 'maria', 'gender': 'female'},
        {'id': 3, 'username': 'dexter', 'gender': 'male'},
        {'id': 4, 'username': 'stephen', 'gender': 'male'}
    ]

    csv_writer = csv.DictWriter(csvFile, fields) # Create a CSV writer object

    csv_writer.writeheader() # Write the fields

    csv_writer.writerows(rows)