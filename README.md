# python-text-adventure-framework
A python text adventure framework.

# To Use 

1. Copy/paste imports from demo version.
2. Create Common Name Registry and add relevant CommonNameOBJ instances.
3. Create a Registry instance.
4. Add instance of Common Name Registry to the Registry.
5. Create text files in chapters folder. This is the story of the adventure.
6. Create ChapterOBJs. These contain information about chapters.
7. Create ChapterEvents. Every chapter obj needs a chapter event, but it doesn't have to do anything.
8. Add instances of chapter events to the chapter objects.
9. Add chapters to the Registry.
10. Invoke registry.ExecuteCurrentIndex.

# How it works 

The registry loops through an array of chapter objects. It then opens the text files in chapters folder using the file path contained in the object. It then invokes a Renderer object that prints out each character and line as a typewriter effect. If there is an event attached to the chapter, it looks for the @evt symbol. If there is that symbol in the text file, it executes the associated event.

# Common variables in text files 

@evt = Event. This tells the registry to execute the associated event.
@name-x = A name. This is a common name.
