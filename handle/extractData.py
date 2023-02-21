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

    def deleteView(self):
        pass
    #list .csv file in model then choose then confirm delete