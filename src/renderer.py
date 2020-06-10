
from os import system, name
from time import sleep

#from chapterOBJ import *

#	Renderer class.
#	This is the class that handles the output.

class Renderer:
	
    def __init__(self):
        self.newStr = ""
        self.characterSpeed = 0.01
        self.lineSpeed = 1
        
    def ClearScreen(self):
        os = ""
        #	For windows:
        if name == "nt":
            os = system("cls")
        #	For mac etc
        else:
            os = system("clear")
            
    def DisplayFullChapter(self, lines, chapter):  
    
        story = ""
        
        #   For every line, execute display single line and then 
        #   wait and then add the line to total story. Then clear 
        #   the screen.
        for line in lines:
           
            r = chapter.chapterAssociatedEvent.registryInstance
            commonNameRegistry = r.commonNameRegistry
            if len(commonNameRegistry.commonNameObjectList) > -1:
                for commonName in commonNameRegistry.commonNameObjectList:
                    if line.find(commonName.associatedSymbol) >-1:
                        newline = line.replace(commonName.associatedSymbol, commonName.commonName)
                        line = newline
                        
            if line.find("@evt") >-1:
                chapter.ExecuteEvent()
            else:
                self.DisplaySinlgeLine(line, story, self.characterSpeed)
                sleep(self.lineSpeed)
                story += line
            self.ClearScreen() 

    #   Writes to the screen.
    def DisplaySinlgeLine(self, theString, story, characterSpeed):
    
        #   For each letter, 
        #   Clears the screen, then waits, then adds a letter to newStr and prints newStr
        for letter in theString:
            self.ClearScreen()
            sleep(characterSpeed)
            self.newStr += letter
            print(self.newStr)

	