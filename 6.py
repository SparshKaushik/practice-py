import names
import random
import csv

def create():
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['S.No.', 'First Name', 'Last Name', 'Age'])
        for i in range(100):
            writer.writerow([i+1, names.get_first_name(), names.get_last_name(), random.randint(1, 100)])

def read():
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

if __name__ == '__main__':
    create()
    read()