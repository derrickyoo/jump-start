import csv
import os
import statistics

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

        return purchases


# replaced by lambda function
# def get_price(p):
#     return p.price

def query_data(data):
    # if data was sorted by price
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchases = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths.'.format(
        high_purchases.price, high_purchases.beds, high_purchases.baths))
    
    # least expensive house?
    low_purchases = data[0]
    print('The cheapest house is ${:,} with {} beds and {} baths.'.format(
        high_purchases.price, high_purchases.beds, high_purchases.baths))

    # average price house?
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)


    prices = [
        p.price # projection or items to create 
        for p in data # the set to process
    ]

    avg_price = statistics.mean(prices)
    print("The average house price is ${:,}.".format(int(avg_price)))

    # average price of 2 bedroom houses
    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)
    
    two_bed_homes = [
        p # projection or items to create
        for p in data # the set process
        if p.beds == 2 # test/condition
    ]

    avg_price = statistics.mean([p.price for p in two_bed_homes])
    avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    print("The average 2 bedroom house price is ${:,}, baths={}, sq. ft={:,}.".format(int(avg_price), round(avg_baths, 1), round(avg_sqft, 1)))

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

if __name__ == '__main__':
    main()
