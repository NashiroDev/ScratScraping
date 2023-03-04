# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
# from selenium.webdriver.chrome.options import Options

class Block:
    def __init__(self, block_number):
        # Set the path to the ChromeDriver executable
        path_to_chromedriver = 'C:/WebDriver/chromedriver.exe'

        # Create a Service object
        s = Service(executable_path=path_to_chromedriver)

        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-gpu')
    
        # Pass the Service object to the Chrome constructor
        self.driver = webdriver.Chrome(service=s)

        # Init object variables
        self.block_number = block_number
        self.data = []

    '''get the data from the ChromeDriver'''
    def scrapData(self, stop, step):
        count = 1

        try:
            for i in range(self.block_number, stop, step):
                self.data = []
                rows = []
                urlPart = self.block_number + (count*step)

                # Construct the URL for the block page
                url = f'https://etherscan.io/block/{urlPart}'
                
                # Wait 0.31s to avoid ban while browsing blocks
                time.sleep(0.31)

                # Load the page
                self.driver.get(url)

                # Wait
                WebDriverWait(self.driver, 10, 2.2)

                # Get the content with the class specified
                rows.extend(self.driver.find_elements('class name', 'row'))
                rows.remove(rows[-1])

                # Wash data
                for row in rows:
                    self.data.append(row.text.replace('\n', '').split(':', 1))

                # Reconstruct the data while excluding blank fields
                self.data = [x for x in self.data if len(x)>1]

                # Call writeToCsv method to save current block data
                self.writeToCsv(step)

                # Notify the script state
                if count % 25 == 0:
                    print(f'Block n°{count} sur {round((stop-self.block_number)/step)}\nCurrent block : {i}')

                count += 1
        except:
            print('Error while proccessing a block')

    '''show the current block data'''
    def displayData(self):
        for item in self.data:
            print(item)

    '''save the current block in data/eth{step}.csv'''
    def writeToCsv(self, step):
        # Set the filename for the CSV file
        filename = f'data/eth{step}.csv'

        # Check if the file exists
        file_exists = os.path.isfile(filename)

        # Open the file in append mode
        with open(filename, 'a') as file:
            # If the file doesn't exist, write the header row
            if file_exists:
                for x in self.data:
                    # Some filters
                    if x[0] != ('Extra Data' or 'More Details'):
                        if x[0] == 'Burnt Fees' and not x[1][0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            x[1] = x[1][2:]
                        header = x[0] + ':' + x[1]
                        try:
                            file.write(header + '\n')
                        except:
                            pass