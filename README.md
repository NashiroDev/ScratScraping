# ScratScraping

Needed libraries for the script to work :
- selenium
- numpy
- pandas
- matplotlib
- matplotlib.pyplot

It is also needed to have an up to date chrome webdriver at the root of C:/WebDriver

For use :
The scrap section ask you to enter the starting block of the scrap, the last and the step.
You can put any number from 1 to ~17000000.
The scraped data will then be appened in a csv file on top of any previous data scraped with the entered step.

The handle section allow you to extract only the desired fields in another csv file. You can either create a model or delete it.

Finally the last section allow us to use the model previously generated, for now there is just a few function available. The letters at the end of the function name refer to the fields that must be present in the model selected.
As an exemple : a function ending with BHMB refer to the fields 'Block Height' and 'Mined by'. a function ending with BHFR refer to the fields 'Block Height' and 'Fee recipient'.
