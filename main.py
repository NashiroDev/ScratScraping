#charset: utf-8
import handle.scrapData as sd
import handle.extractData as ed
import handle.useData as ud

def multipleScrapAndSave(start=0, stop=5, step=1):

    block = sd.Block(start)
    block.scrapData(stop, step)
    block.driver.quit()

def makeModel(modelPath, fields):

    model = ed.Model(modelPath)
    model.readFile()
    model.createView(fields)

def useModel(file_path):
    
     # Display instructions to the user
    instructions = "Please select a function (1-3 : \nud.plot_data_BHEP : 1\nud.plot_data_TEP : 2\nud.plot_data_BHMD : 3): "
    selection = str(input(instructions))

    # Use a while loop to keep prompting the user until they provide a valid input
    while selection not in ["1", "2", "3"]:
        print("Invalid input. Please try again.")
        selection = input(instructions)

    # Use a try-except block to catch any potential errors
    try:
        # Call the corresponding function based on user input
        if selection == "1":
            ud.plot_data_BHEP()
        elif selection == "2":
            ud.plot_data_TEP()
        else:
            ud.plot_data_BHMB()
    except:
        print("An error occurred while executing the selected function")
    
    
    
    
    # step, step2, ground, limite = 10, 5, 5, 5

    # file_path = './data/model/_eth3125EtherPrice.csv'
    # file_path_bis = './data/model/_eth3125TimestampEtherPrice.csv'
    # file_path_ter = './data/model/_eth3125Minedby.csv'

    # data = ud.read_data(file_path)
    # data_bis = ud.read_data(file_path_bis)
    # data_ter = ud.read_data(file_path_ter)

    # ud.plot_data_BHEP(data, step, ground)
    # ud.plot_data_TEP(data_bis, step2, ground)
    # ud.plot_data_BHMB(data_ter, limite)

####### Prompt //~6250B/j moy //PoS : 15537393

s=15542494 #début scraping
e=16711850 #finishing
# p=1 #Step/Nom du fichier de save eth{}.csv
multipleScrapAndSave(s, e, 1)

# makeModel('data/eth1.csv', ['Fee Recipient'])

# useModel('/data/model/_eth3125EtherPrice.csv', )




##Make : interface, 