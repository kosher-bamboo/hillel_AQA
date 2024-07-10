"""
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""
from pathlib import Path
import csv


def read_csv_with_comma_delimater(file):
    list_of_items = []
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        title_row = next(reader)
        # create a list of tuples (rows)
        for row in reader:
            list_of_items.append(tuple(row))  # convert to tuple for future convertion into set
    return title_row, list_of_items


def read_csv_with_semicolon_delimater(file):
    list_of_items = []
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        title_row = next(reader)
        # create a list of tuples (rows)
        for row in reader:
            list_of_items.append(tuple(row))  # convert to tuple for future convertion into set
    return title_row, list_of_items


title = read_csv_with_comma_delimater("r-m-c.csv")[0]

set1 = set(read_csv_with_comma_delimater("r-m-c.csv")[1])
set2 = set(read_csv_with_comma_delimater("rmc.csv")[1])
common_items = set1 & set2
items_only_in_first = set1 - set2
items_only_in_second = set2 - set1


with open('result_marar.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(title)
    writer.writerows(common_items)
