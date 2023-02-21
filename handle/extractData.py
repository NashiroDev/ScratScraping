from os import listdir
from os import remove
class Model:
    def __init__(self, filename):
        self.filename = filename
        self.dataDict = dict()
        self.sortedDataDict = dict()
    
    def readFile(self):
        with open(self.filename, 'r') as file:
            data = file.read()
            fieldLine = data.split('\n')
            blockTemp= ['', {}]

            for line in fieldLine:
                line = line.split(':', 1)

                if (line[0] == 'Block Height'):
                    if len(blockTemp[1]) < 1:
                        blockTemp[0] = line[1]
                    else:
                        self.dataDict[blockTemp[0]] = blockTemp[1]
                        blockTemp = [line[1], {}]

                elif not line[0] == '':
                    blockTemp[1][line[0]] = line[1]

        return self.dataDict
    
    def sortFields(self, fields=[]):
        self.sortedDataDict = dict()

        for key, value in self.dataDict.items():

            self.sortedDataDict[key] = {}
            for key0, value0 in value.items():
                if key0 in fields:
                    self.sortedDataDict[key][key0] = value0

        return fields
    
    def createView(self, fields):
        self.sortFields(fields)

        origin = self.filename.split('h', 1)
        origin = origin[-1].split('.', 1)

        if not fields == []:
            fileName = f'_eth{origin[0]}'
            for field in fields:
                fileName += field.replace(' ', '')

            fileName += '.csv'
            path = f'data/model/{fileName}'
            with open(path, 'w') as file:

                for key, value in self.sortedDataDict.items():
                    toWrite = f'Block Height:{key}\n'

                    for key0, value0 in value.items():
                        toWrite += f'{key0}:{value0}\n'

                    file.write(toWrite)

        else:
            print("Invalid: must have at least one filter to create a view.")
    
    def visualizeViews(self):
        files = listdir('data/model')
        count = 1
        for file in files:
            print(count, ' : ' , file)
            count += 1
        return files

    def deleteView(self):
        files = self.visualizeViews()
        loop = 1
        
        while loop:
            try:
                userInput = str(input(f"Please enter the id of the file to delete or !q to quit : "))
                if '!q' in userInput:
                    loop = 0
                elif int(userInput) < 1 or int(userInput) > len(files):
                    print(f"Error: Input must be between 1 and {len(files)}")
                else: loop = 0
            except ValueError:
                print("Error: Please enter an integer in the correct range.")

        if userInput != '!q':
            loop = 1

            while loop:
                try:
                    userConfirm = str(input(f"Are you sure you want to delete {files[int(userInput)-1]} ? [Y/N] : "))
                    if (userConfirm.lower() == 'y' or userConfirm.lower()) == 'n':
                        loop = 0

                        if userConfirm.lower() == 'y':
                            userConfirm = True
                        else: userConfirm = False
                        
                    else: print(f"Error: Input must be y or n")
                except ValueError:
                    print("Error: Please enter a string.")

            if userConfirm:
                pathToDelete = f'/data/model/{files[int(userInput)-1]}'
                remove(pathToDelete)
                print("File deleted successfully.")