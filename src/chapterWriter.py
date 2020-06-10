
#   Import sleep from time and everything from clearscreeneffect
from time import sleep
from screenClear import *

#	Attempts a printer-like text effect.

#   theString is the sentance, the story so far, timeSeconds is the seconds between each character.
def ScreenWrite(theString, story, timeSeconds):

    newStr = ""
    
    sleepSpeed = 0.005
    
    for letter in theString:
        ClearScreen()
        sleep(sleepSpeed)
        newStr += letter
        print(story)
        print(newStr)
 


#   The best speed is 0.02
#ScreenWrite("Top of the Bore Da, boys!", writeSpeed)
#sleep(lineSpeed)
#ScreenWrite("My name is sambo.", writeSpeed)
#sleep(lineSpeed)