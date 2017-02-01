import csv
import os

from purchase import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('--------------------------------------------')
    print('       Real Estate Data Miner App           ')
    print('--------------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


# Example using csv.DictReader
def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        # Refactored using DictReader
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        print(purchases)

# Example
# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header:' + header)
        
#         # Example 1
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)

#         # Example 2
#         reader = csv.reader(fin, delimiter=',')
#         for row in reader:
#             print(type(row), row)
#             beds = row[4]



def query_data(data):
    pass


if __name__ == '__main__':
    main()
