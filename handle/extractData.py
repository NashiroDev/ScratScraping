class Model:
    def __init__(self, filename):
        self.filename = filename
        self.dataDict = dict()
        self.sortedDataDict = dict()
    
    def read_file(self):
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
    
    def sort_fields(self, fields=[]):
        self.sortedDataDict = dict()

        for key, value in self.dataDict.items():

            self.sortedDataDict[key] = {}
            for key0, value0 in value.items():
                if key0 in fields:
                    self.sortedDataDict[key][key0] = value0

        return fields
    
    def create_view(self, fields):
        self.sort_fields(fields)

        if not fields == []:
            fileName = '_eth'
            for field in fields:
                fileName += field.replace(' ', '')

            fileName += '.csv'
            path = f'./data/{fileName}'
            with open(path, 'w') as file:

                for key, value in self.sortedDataDict.items():
                    toWrite = f'Block Height:{key}\n'

                    for key0, value0 in value.items():
                        toWrite += f'{key0}:{value0}\n'

                    file.write(toWrite)

        else:
            print("Invalid: must have at least one filter to create a view.")

# test = Model('./data/eth1.csv')
# test.read_file()
# test.create_view(['Difficulty'])