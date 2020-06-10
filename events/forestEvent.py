
#	An event object.
class ForestEvt:
    #   Requires a registry instance in case I want a chapter Event 
    #   to do something to another object.
    def __init__(self, registry):
        self.registryInstance = registry
    
    def ExecuteEvent(self, args):
        
        result = input("What do you do, traveller? \n")
        
        if result == "LEFT":
            self.registryInstance.ExecuteSingleIndex(2, False)
        
        if result == "RIGHT":
            self.registryInstance.ExecuteSingleIndex(3, False)
        
        if result == "BACK":
            self.registryInstance.ExecuteSingleIndex(4, False)