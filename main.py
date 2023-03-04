# -*- coding: utf-8 -*-
import handle.scrapData as sd
import handle.extractData as ed
import handle.useData as ud
from os import listdir

def askInt(toAsk, incorrectMessage="Error: Invalid entry", possibleAnswear=False):
    while True:
        try:
            userInput = int(input(toAsk))
        except:
            print("Error, please retry.\n")
        else:
            if not possibleAnswear:
                return userInput
            elif userInput in possibleAnswear:
                return userInput
        print(incorrectMessage)
        
def askStr(toAsk, incorrectMessage="Error: Invalid entry.\n", possibleAnswear=False):
    while True:
        try:
            userInput = str(input(toAsk))
        except:
            print("Error, please retry.\n")
        else:
            if not possibleAnswear:
                return userInput
            elif userInput in possibleAnswear:
                return userInput
        print(incorrectMessage)
                

def multipleScrapAndSave(start=0, stop=5, step=1):

    block = sd.Block(start)
    block.scrapData(stop, step)
    block.driver.quit()

def makeModel(fields, dataPath='data/eth1.csv'):

    model = ed.Model(dataPath)
    model.readFile()
    model.createView(fields)

def deleteModel():

    model = ed.Model('data/eth1.csv')
    model.deleteView()

def useModel(dataPath, userChoice):
    
    data = ud.read_data(dataPath)

    if userChoice in [1,2]:
        limited = askInt("Please select the number of entity displayed (enter 1 to see the largest and the rest) : \n>>>")
    if userChoice == 1:
        ud.plot_data_BHMB(data, limited)
    elif userChoice == 2:
        ud.plot_data_BHFR(data, limited)


if __name__ == "__main__":
    loop = True
    
    while loop:

        userInput = askStr("Please enter the id of the action or !q :\nLaunch scrap -> 1\nHandle models -> 2\nUse models -> 3\nQuit -> !q\n>>>", "Error: Please enter !q or a number in the correct range.", ['1','2','3','!q'])
        
        if userInput == '!q':
            loop = False

        elif userInput == '1':
            startBlock = askInt("Please enter the number of the first block to scrap :\n>>>", "Error: entry must be an integer\n")
            endBlock = askInt("Please enter the number of the last block to scrap :\n>>>", "Error: entry must be an integer\n")
            stepBlock = askInt("What is the step between each scrapped block ?\n>>>", "Error: entry must be an integer\n")
            multipleScrapAndSave(startBlock, endBlock, stepBlock)

        elif userInput == '2':
            userInput = askStr("What do you want to do ? :\nCreate a model -> 1\nDelete a model -> 2\nGo home -> !h\n>>>", "Error: Please enter !h or a number in the correct range.\n", ['1','2','!h'])
            
            if userInput == '!h':
                pass
            
            elif userInput == '1':
                files = listdir('data')
                del files[-1]
                potentialFields = ['Timestamp', 'Proposed On', 'Transactions', 'Fee Recipient', 'Mined by', 'Block Reward', 
                                   'Total Difficulty', 'Size', 'Gas Used', 'Gas Limit', 'Base Fee Per Gas', 'Burnt Fees', 'Ether Price']
                explainFields = f"Select the fields that you want to use in your new Model among these (Block Height is used by default):\n{potentialFields}\nChoose at least one and at most three fields. Refer them by their id in the given list (start at 0), separated with a ';' in between.\nExemple : 0;2 or 6;-2;4\nNote that Fee Recipient and Mined by don't appear in every block.\n>>>"
                
                dataPath = askStr("Type the data file name to use (in /data) ?\n{}\n>>>".format(files), "Error: File does not exist in /data.\n", files)
                finalDataPath = f"data/{dataPath}"

                indicator = True
                while indicator:
                    indicator = False

                    toSortFields = askStr(explainFields)
                    toSortFields = toSortFields.split(';')
                    finalSortFields = []

                    if len(toSortFields) <= 3:
                        for id in toSortFields:
                            try:
                                potentialFields[int(id)]
                            except:
                                indicator = True
                                print("The prompt given wasn't correct.\n")
                            else:
                                finalSortFields.append(potentialFields[int(id)])
                
                makeModel(finalSortFields, finalDataPath)

            elif userInput == '2':
                deleteModel()

        elif userInput == '3':
            files = listdir('data/model')
            instructions = "Please select a function to run :\nud.plot_data_BHMD -> 1\nud.plot_data_BHFR -> 2\n>>>"

            userInput = askInt(instructions, "Error: index out of range.\n", [int(i) for i in range(1, 3)])
            dataPath = askStr("Type the model file name to use (in /data/model) ?\n{}\n>>>".format(files), "Error: File does not exist in /data/model.\n", files)
            definitivePath = f"data/model/{dataPath}"

            useModel(definitivePath, userInput)

####### Prompt //~6250B/j moy //PoS : 15537393
s=15567184 #début scraping
e=16711850 #finishing
p=1 #Step/Nom du fichier de save eth{}.csv
multipleScrapAndSave(s, e, p)