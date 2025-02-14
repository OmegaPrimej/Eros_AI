#Reading a text file
with open('example.txt', 'r') as file:
    print(file.read())

#Writing to a text file
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

#Working with CSV files
import csv
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Working with JSON files
import json
data = {'name': 'John', 'age': 30}
with open('example.json', 'w') as file:
    json.dump(data, file)
