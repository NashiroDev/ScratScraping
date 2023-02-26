#charset: utf-8
import handle.scrapData as sd
import handle.extractData as ed

def multipleScrapAndSave(start=0, stop=5, step=1):

    block = sd.Block(start)
    block.scrapData(stop, step)
    block.driver.quit()

def makeModel(modelPath, fields):

    model = ed.Model(modelPath)
    model.readFile()
    model.createView(fields)

####### Prompt //~6250B/j moy //PoS : 15537393

s=14000000 #début scraping
e=16699164 #finishing
# p=1 #Step/Nom du fichier de save eth{}.csv
multipleScrapAndSave(s, e, 1)

# makeModel('data/eth3125.csv', ['Mined by'])

##Make : interface, 