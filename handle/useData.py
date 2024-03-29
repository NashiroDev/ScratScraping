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
# La fonction plot_data_BHMB prend deux arguments en entrée: data qui est un dictionnaire représentant les données de la base de données, et limited qui est un entier qui limite le nombre de mineurs de blocs affichés dans le diagramme.

# La fonction commence par initialiser une liste vide data2 qui stockera les noms des mineurs de blocs et le nombre de blocs qu'ils ont minés. Ensuite, elle parcourt les données de la base de données et compte le nombre de blocs minés par chaque mineur. Elle stocke les noms des mineurs de blocs et le nombre de blocs qu'ils ont minés dans la liste data2.

# La fonction calcule ensuite les limited mineurs de blocs qui ont miné le plus grand nombre de blocs en triant la liste data2 dans l'ordre décroissant et en prenant les limited premiers éléments. Les autres mineurs sont regroupés dans une catégorie "autres" et leur nombre de blocs est ajouté à la liste finalData.

# Enfin, la fonction utilise la bibliothèque matplotlib pour créer un diagramme circulaire à partir des données de finalData.
def plot_data_BHMB(data, limited):

    data2 = [[], []]
    try:
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
    except:
        print('Error, model might have a required row name missing or the parameters given are incorrects.')

'''create a camembert view of the principals validators since eth2.0'''
# La fonction plot_data_BHFR prend deux arguments en entrée: data qui est un dictionnaire représentant les données de la base de données, et limited qui est un entier qui limite le nombre de destinataires de frais affichés dans le diagramme.

# La fonction commence par initialiser une liste vide data2 qui stockera les noms des destinataires de frais et le nombre de transactions avec ces destinataires. Ensuite, elle parcourt les données de la base de données et compte le nombre de transactions pour chaque destinataire de frais. Elle stocke les noms des destinataires de frais et le nombre de transactions dans la liste data2.

# La fonction calcule ensuite les limited destinataires de frais qui ont reçu le plus grand nombre de transactions en triant la liste data2 dans l'ordre décroissant et en prenant les limited premiers éléments. Les autres destinataires sont regroupés dans une catégorie "autres" et leur nombre de transactions est ajouté à la liste finalData.

# Enfin, la fonction utilise la bibliothèque matplotlib pour créer un diagramme circulaire à partir des données de finalData.
def plot_data_BHFR(data, limited):
    data2 = [[], []]
    try:
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
    except:
        print('Error, model might have a required row name missing or the parameters given are incorrects.')

'''Create an histogram of the value distributed per block and their frequency'''
# La fonction plot_data_BHBR prend en entrée un objet data qui contient les données de récompense de bloc Ethereum.

# Dans cette fonction, les valeurs de récompense de bloc sont arrondies à trois décimales et stockées dans la liste finalData.
def plot_data_BHBR(data):

    finalData = []
    for value in data['Block Reward']:
        finalData.append(round(float(value), 3))

    # Create histogram
    plt.hist(finalData, bins=300, width=0.098, edgecolor='lightgrey')
    plt.xlim(0.01, 0.9)
    plt.xlabel('Reward Amount')
    plt.ylabel('Frequency')
    plt.title('Distribution of Ethereum Block Mining Rewards')
    plt.show()
