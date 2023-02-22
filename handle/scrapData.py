from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import os

class Block:
    def __init__(self, block_number):
        # Set the path to the ChromeDriver executable
        path_to_chromedriver = 'C:/WebDriver/chromedriver.exe'

        # Create a Service object
        s = Service(executable_path=path_to_chromedriver)

        # Pass the Service object to the Chrome constructor
        self.driver = webdriver.Chrome(service=s)

        self.block_number = block_number
        self.data = []

    def scrapData(self):

        # Construct the URL for the block page
        url = f'https://etherscan.io/block/{self.block_number}'

        # Load the page
        self.driver.get(url)
        WebDriverWait(self.driver, timeout=500)

        # Find all the rows with the class name "row.mb-5"
        rows = self.driver.find_elements('class name', 'row.mb-4')
        rows.append(self.driver.find_element('id', 'ContentPlaceHolder1_closingEtherPrice'))
        # rows.append(self.driver.find_element('class', 'row'))

        # Wash data
        for row in rows:
            self.data.append(row.text.replace('\n', '').split(':', 1))

        self.data = [x for x in self.data if len(x)>1]

        # Close the browser window
        self.driver.quit()

        return self.data

    def displayData(self):
        for item in self.data:
            print(item)

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
                    if not x[0] == 'Extra Data':
                        if x[0] == 'Burnt Fees' and not x[1][0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            x[1] = x[1][2:]
                        header = x[0] + ':' + x[1]
                        file.write(header + '\n')