Reading and writing to text files
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

with open('example.txt', 'r') as file:
    print(file.read())

Appending to a text file
with open('example.txt', 'a') as file:
    file.write('\nThis is a new line.')

Reading and writing to binary files
with open('example.bin', 'wb') as file:
    file.write(b'Hello, world!')

with open('example.bin', 'rb') as file:
    print(file.read())
