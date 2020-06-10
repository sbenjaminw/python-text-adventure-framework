
from src.commonNameOBJ import *

#   A registry of common names.
class CommonNameRegistry:
    
    def __init__(self):
        self.commonNameObjectList = []
    
    #   Adds a common name to the list 
    def AddCommonName(self, cno):
        self.commonNameObjectList.append(cno)
    
    #   Gets a common name in the list by a name
    def GetCommonNameObjByName(self, name):
        wantedCommonNameOBJ = ""
        for commonNames in self.commonNameObjectList:
            if commonNames.commonName == name:
                wantedCommonNameOBJ = commonNames
        return wantedCommonNameOBJ
        
    #   Gets a common name in the list by a symbol
    def GetCommonNameObjBySymbol(self, symbol):
        wantedCommonNameOBJ = ""
        for commonNames in self.commonNameObjectList:
            if commonNames.associatedSymbol == symbol:
                wantedCommonNameOBJ = commonNames
        return wantedCommonNameOBJ
    