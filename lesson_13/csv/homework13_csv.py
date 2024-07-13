"""
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""
import csv


# detect used delimiter in csv file
def detect_delimiter(file):
    with open(file, "r", newline="") as csvfile:
        sample = csvfile.read(1024)  # read 1024 bytes of data
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample)
        return dialect.delimiter


def read_csv(file):
    list_of_items = []
    with open(file, "r", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=detect_delimiter(file))
        title_row = next(reader)
        # create a list of tuples (rows of data)
        for row in reader:
            list_of_items.append(tuple(row))  # convert to tuple for future convertion into set
    return title_row, list_of_items


title = read_csv("r-m-c.csv")[0]
set1 = set(read_csv("r-m-c.csv")[1])
set2 = set(read_csv("rmc.csv")[1])
symmetric_difference = set1.symmetric_difference(set2)


def write_symmetric_difference_csv():

    with open('result_marar.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(title)
        writer.writerows(symmetric_difference)


write_symmetric_difference_csv()
