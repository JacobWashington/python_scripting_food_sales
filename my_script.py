# Read only

def read_only():
    ''' a method that only reads the file '''
    try:
        file1 = open('data.txt')
        text = file1.read()
        print(text)
        file1.close()  # the reason for closing, is to prevent a file from remaining open in memory
    except FileNotFoundError:
        text = None
        print(text)


def write_only():
    ''' a method that only writes to a file '''
    file2 = open('more_data.txt', 'w')
    # if file exists, it will be overwritten
    # if a file does not exist, it will be created
    file2.write('tomatoes')
    file2.close()


# python will know to close this file, even if there are errors
# with open('data.txt') as f:
#     txt = f.read()
#     print(txt)

# def read_food_sales():
#     all_dates = []
#     with open('sampledatafoodsales.csv') as f:
#         data = f.readlines()
#         for food_sale in data:
#             split_food_sale = food_sale.split(',')
#             # print(split_food_sale)
#             order_date = split_food_sale[0]
#             all_dates.append(order_date)
#     print(all_dates)

#     with open('dates.txt', 'w') as f:
#         for date in all_dates:
#             f.write(date)
#             f.write('\n')

# def append_text():
#     ''' append data to an existing file '''
#     with open('dates.txt', 'a') as f:
#         f.write('01/03/1993')
#         print('done')

def read_food_sales():
    regions = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            # print(split_food_sale)
            region = split_food_sale[1]
            regions.append(region)
    print(regions)


if __name__ == '__main__':
    #      read_only()
    #      write_only()
    # read_food_sales()
    # append_text()
    read_food_sales()

