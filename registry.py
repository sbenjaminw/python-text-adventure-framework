from src.chapterOBJ import *
from src.fileReader import *
from src.renderer import *

#	Registry
#	Stores instances of objects and events.
class Registry:
    
    def __init__(self):
        #   Continue running the story.
        self.runStory = True
        #   The current place in the story.
        self.currentIndex = 0
        #   Chapters are objects that represent the text files.
        self.chapters = []
        #   Associated events are classes that define a function for part of a chapter
        self.associatedEvents = []
    
    #   Adds the common name registry
    def AddCommonNameRegistry(self, commonNameRegistry):
        self.commonNameRegistry = commonNameRegistry
    
    #   Increments the story index.
    def IncrementIndex(self):
        self.currentIndex += 1
    
    #   Adds a chapter to the registry.
    def AddChapter(self, chapter):
        self.chapters.append(chapter)
        
    #   Executes a requsted index.
    def ExecuteSingleIndex(self, index, continueStory):
        lines = ""
        c = ""
        for chapter in self.chapters:
            c = chapter
            if chapter.chapterIndex == index:
                self.currentIndex = index
                c = chapter
                fReader = FileReader()
                lines = fReader.ExecuteReader(chapter.chapterFilePath)
                break 
        r = Renderer()
        r.DisplayFullChapter(lines, c)
        #   Check to see if the current index is less than the current number of 
        #   chapters in the registry.
        if self.currentIndex < len(self.chapters) and continueStory == True:
            #self.IncrementIndex()
            self.ExecuteCurrentIndex()
        else:
            self.runStory = False
            print("End")
    
    #   Plays the current index.
    def ExecuteCurrentIndex(self):
        lines = ""
        c = ""
        for chapter in self.chapters:
            if chapter.chapterIndex == self.currentIndex:
                c = chapter
                fReader = FileReader()
                lines = fReader.ExecuteReader(chapter.chapterFilePath)
                break 
        r = Renderer()
        r.DisplayFullChapter(lines, c)
        #   Check to see if the current index is less than the current number of 
        #   chapters in the registry.
        if self.currentIndex < len(self.chapters) and self.runStory == True:
            self.IncrementIndex()
            self.ExecuteCurrentIndex()
        else:
            print("End")
    
        