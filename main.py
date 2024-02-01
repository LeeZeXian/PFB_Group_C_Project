# -*- coding: utf-8 -*-


import csv

from overheads import *
from profit_loss import *
from cash_on_hand import *


def input_file(file):
    with open(file, 'r') as file:
      data = list(csv.reader(file))[1:]  

    column_index = 1  

    for row in data:
        try:
            row[column_index] = float(row[column_index])
        except ValueError:
            print(f"WARNING: Unable to convert value '{row[column_index]}' to float in row {data.index(row) + 1}.")

    return data

### Main program main.py
def main():
    ### Find the highest overhead information
    data = input_file('./csv_reports/overheads.csv')
    overhead(data)
    
    ### Find the highest/lowest or fluctuating cash surplus or deficit formation
    data = input_file('./csv_reports/cash_on_hand.csv')
    cash_on_hand(data)
    
    ### Find the highest/lowest or fluctuating net profit surplus or deficit formation
    data = input_file('./csv_reports/Profits_and_Loss.csv')
    profit_and_loss(data)


if __name__ == "__main__":
    main()
 
