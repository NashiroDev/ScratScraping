# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''read the data from the specified file path using pandas and returns a pandas dataframe.'''
def read_data(file_path):
    data = dict()
    
    with open(file_path, "r") as file:
        lines = file.read()
        lines = lines.split('\n')
        
        header = lines[0].split('|')
        lines.pop(0)
        
        for head in header:
            data[head] = []

        for line in lines:
            if not line == '':
                line = line.split('|')

                for i in range(len(header)):
                    try:
                        data[header[i]].append(line[i])
                    except:
                        pass
    return data

'''exclude blocks where eth price < ground'''
def filter_low_prices(data, ground):

    # Transform ground to an array of this type : ['0', '1', '2', ..., 'ground-1', 'ground']
    ground = np.array([str(x) for x in range(ground+1)])

    # Filter out rows where the Ether price is outside the range 0 to ground
    count = 0
    for price in data['Ether Price']:

        if price in ground:
            # Pop unwanted lines
            data['Block Height'].pop(count)
            try:
                data['Ether Price'].pop(count)
            except: pass
            try:
                data['Timestamp'].pop(count)
            except: pass
        else:
            # Transform from str() type to int()
            data['Ether Price'][count] = int(price)

        count += 1

    return data

'''create a camembert view of the principals miners'''
def plot_data_BHMB(data, limited):

    data2 = [[], []]
    lenData = len(data['Mined by'])

    for i in range(0, lenData):
        if pd.isna(data['Mined by'][i]):
            pass
        elif data['Mined by'][i] not in data2[0]:
            data2[0].append(data['Mined by'][i])
            data2[1].append(1)
        else:
            index = data2[0].index(data['Mined by'][i])
            data2[1][index] += 1

    finalData = [[], []]
    currentMax = data2[1].index(max(data2[1]))
    for i in range(limited):
        finalData[0].append(data2[0][currentMax])
        finalData[1].append(int(data2[1][currentMax]))
        data2[0].remove(data2[0][currentMax])
        data2[1].remove(data2[1][currentMax])
        currentMax = data2[0].index(max(data2[0]))

    others = ['others', len(data2[0])-limited]

    finalData[1].append(others[1])
    finalData[0].append(others[0])

    plt.figure(figsize=(14, 7))

    plt.pie(finalData[1],
            labels=finalData[0],
            startangle=230,
            shadow=True,
            explode=np.zeros(len(finalData[0])),
            autopct='%1.1f%%',
            rotatelabels=185
            )
    plt.title('Miners weight in a sample of Blocks.')

    plt.show()

'''create a camembert view of the principals validators since eth2.0'''
def plot_data_BHFR(data, limited):
    data2 = [[], []]
    lenData = len(data['Fee Recipient'])

    for i in range(0, lenData):
        if pd.isna(data['Fee Recipient'][i]):
            pass
        elif data['Fee Recipient'][i] not in data2[0]:
            data2[0].append(data['Fee Recipient'][i])
            data2[1].append(1)
        else:
            index = data2[0].index(data['Fee Recipient'][i])
            data2[1][index] += 1

    finalData = [[], []]
    currentMax = data2[1].index(max(data2[1]))
    for i in range(limited):
        finalData[0].append(data2[0][currentMax])
        finalData[1].append(int(data2[1][currentMax]))
        data2[0].remove(data2[0][currentMax])
        data2[1].remove(data2[1][currentMax])
        currentMax = data2[0].index(max(data2[0]))

    others = ['others', len(data2[0])-limited]

    finalData[1].append(others[1])
    finalData[0].append(others[0])

    plt.figure(figsize=(14, 7))

    plt.pie(finalData[1],
            labels=finalData[0],
            startangle=45,
            shadow=True,
            explode=np.zeros(len(finalData[0])),
            autopct='%1.1f%%',
            rotatelabels=185
            )
    plt.title('Share of blocks validated since The Merge.')

    plt.show()

