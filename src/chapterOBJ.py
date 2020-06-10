
#	The Chapter object.
class ChapterOBJ:
    #   The chapter name is a given string name of chapter 
    #   The chapter index, an integer, the position where the chapter is at 
    #   The file path of the text file 
    #   The associated event object 
    #   The associeted event arguments.
    def __init__(self, chapterName, chapterIndex, chapterFilePath, chapterAssociatedEvent, chapterAssociatedEventArgs):
        self.chapterName = chapterName
        self.chapterIndex = chapterIndex
        self.chapterFilePath = chapterFilePath
        self.chapterAssociatedEvent = chapterAssociatedEvent
        self.chapterAssociatedEventArgs = chapterAssociatedEventArgs
    
    #   Executes the associated event object.
    def ExecuteEvent(self):
        self.chapterAssociatedEvent.ExecuteEvent(self.chapterAssociatedEventArgs)