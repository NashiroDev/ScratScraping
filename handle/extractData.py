from os import listdir
from os import remove
class Model:
    def __init__(self, filename):
        self.filename = filename
        self.dataDict = dict()
        self.sortedDataDict = dict()
    
    '''read raw or sorted data'''
    def readFile(self):
        with open(self.filename, 'r') as file:
            data = file.read()
            fieldLine = data.split('\n')
            blockTemp= ['', {}]
            lineCompare = [[], []]

            for line in fieldLine:
                line = line.split(':', 1)

                # Seek block height field to change block references
                if (line[0] == 'Block Height'):
                    if line[1] == lineCompare[1]:
                        pass
                    elif len(blockTemp[1]) < 1:
                        blockTemp[0] = line[1]
                    else:
                        self.dataDict[blockTemp[0]] = blockTemp[1]
                        blockTemp = [line[1], {}]

                elif not line[0] == '':
                    blockTemp[1][line[0]] = line[1]

                # save current line to avoid saving duplicate blocks
                lineCompare = line

        return self.dataDict
    
    '''sort fields'''
    def sortFields(self, fields):
        self.sortedDataDict = dict()

        for key, value in self.dataDict.items():

            self.sortedDataDict[key] = {}
            for key0, value0 in value.items():
                if key0 in fields:
                    self.sortedDataDict[key][key0] = value0

        return fields

    '''clean the fields to have the wanted form'''
    def cleanField(self, type, field):

        if type == 'Timestamp':

            field = field.split(' ')
            cleanedField = field[-4].replace('(', '')

        elif type == 'Ether Price':

            if len(field) < 5:
                cleanedField = '0'
            else:
                field = field.split(' ')
                field = field[0].replace('$', '')
                if field[-3] == '.':
                    field = field.split('.')
                    cleanedField = field[0].replace(',', '')
                else: cleanedField = field.replace(',', '')

        elif type == ('Block Reward' or 'Burnt Fees'):

            field = field.split(' ')
            cleanedField = field[0]

        elif type == 'Mined by':

            field = field.split('in')
            cleanedField = field[0]
        elif type == 'Fee Recipient':
            if ' in 12 secs' in field:
                field = field.split(' in 12 sec')
                cleanedField = field[0]

                if 'Fee Recipient' in cleanedField:
                    field = cleanedField.split('pient: ')
                    cleanedField = field[1]

            else: cleanedField = field
        else:
            cleanedField = field

        return cleanedField

    '''create a clean model specificaly for a usecase'''
    def createView(self, fields):
        self.sortFields(fields)

        header = 'Block Height|'
        toWrite = ''

        origin = self.filename.split('h', 1)
        origin = origin[-1].split('.', 1)

        if not fields == []:
            fileName = f'_eth{origin[0]}'
            for field in fields:
                header += field + '|'
                fileName += field.replace(' ', '')

            fileName += '.csv'
            header = header[:-1] + '\n'
            path = f'data/model/{fileName}'
            with open(path, 'w') as file:

                file.write(header)

                for key, value in self.sortedDataDict.items():
                    toWrite += f'{key}|'

                    for key0, value0 in value.items():
                        toWrite += f'{self.cleanField(key0, value0)}|'
                    toWrite = toWrite[:-1] + '\n'

                file.write(toWrite)

        else:
            print("Invalid: must have at least one filter to create a view.")

    '''show all models in model directory'''
    def visualizeViews(self):
        files = listdir('data/model')
        count = 1
        for file in files:
            print(count, ' : ' , file)
            count += 1
        return files

    '''allow to delete a view in model directory, with double confirmation'''
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