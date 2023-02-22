#charset: utf-8
import handle.scrapData as sd
import handle.extractData as ed

def multipleScrapAndSave(start=0, stop=5, step=1):
    try:
        for i in range(start, stop, step):
            block = sd.Block(i)
            block.scrapData()
            block.writeToCsv(step)
            percentage = float((i/stop)*100)
            print(f'Tasks : {i}/{stop}\n{percentage}% done.')
    except:
        print(f'Error: Failed to scrape and save block n°{i}')

def makeModel(modelPath, fields):
    try:
        model = ed.Model(modelPath)
        model.readFile()
        model.createView(fields)
    except:
        print(f'Error: Failed to create model from FILE with FILTER')

####### Prompt //~6250B/j moy //PoS : 15537393

s=14900000 #début scraping
e=16678211 #finishing
p=3125 #Step/Nom du fichier de save eth{}.csv
multipleScrapAndSave(s, e, p)

# makeModel('data/eth1.csv', ['Difficulty', 'Ether Price', 'Mined by'])

##Make : interface, 