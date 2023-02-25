# encoding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_data(file_path):
    """
    This function reads the data from the specified file path using pandas and returns a pandas dataframe.
    """
    return pd.read_csv(file_path, sep='|')

def filter_low_prices(data, ground):
    ground = np.array([str(x) for x in range(ground+1)])

    # Filter out rows where the Ether price is outside the range 0 to ground
    count = 0
    for price in data['Ether Price']:

        if price in ground:
            data['Block Height'].pop(count)
            data['Ether Price'].pop(count)

        else: data['Ether Price'][count] = int(price)

        count += 1
    
    return data

def plot_data_BHEP(data, step, ground):

    data = filter_low_prices(data, ground)

    # Plot the data with the specified step size and no logarithmic scaling
    plt.figure(figsize=(14, 7))
    plt.plot(data['Block Height'][::step], data['Ether Price']
             [::step], linewidth=0.1, marker='.')
    plt.xlabel('Block Height*10^1')
    plt.ylabel('Ether Price ($)')
    plt.title('Ether Price Variation')
    plt.xticks(np.arange(data['Block Height'][::step].min(), data['Block Height'][::step].max(
    ), (data['Block Height'][::step].max() - data['Block Height'][::step].min()) / 15))
    plt.yticks([50, 600, 1360, 2750, data['Ether Price'][::step].max()])
    plt.grid(True)
    plt.show()

def plot_data_TEP(data, step, ground):

    data = filter_low_prices(data, ground)
    lenData = len(data['Timestamp'])

    # Plot the data with the specified step size and no logarithmic scaling
    plt.figure(figsize=(14, 7))
    plt.scatter(data['Timestamp'][::step], data['Ether Price'][::step], linewidth=0.1, marker='.', color='g')
    plt.xlabel('Timestamp')
    plt.ylabel('Ether Price ($)')
    plt.title('Ether Price Variation')
    plt.xticks(np.arange(0, 600, 60), [data['Timestamp'][x] for x in range(0, lenData, int(lenData/9))], rotation=90)
    plt.yticks([50, 600, 1360, 2750, data['Ether Price'][::step].max()])
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    file_path = './data/model/_eth3125EtherPrice.csv'
    file_path_bis = './data/model/_eth3125TimestampEtherPrice.csv'
    data = read_data(file_path)
    data_bis = read_data(file_path_bis)
    step, ground = 10, 5
    plot_data_BHEP(data, step, ground)
    plot_data_TEP(data_bis, step, ground)
