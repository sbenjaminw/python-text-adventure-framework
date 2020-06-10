
#	GAME.PY
#	=======

#   Game stuff
from src.chapterOBJ import * 
from src.commonNameOBJ import * 
from src.commonNameRegistry import *

from registry import *

#   Import events 
from events.forestEvent import *

#   Create a common name.
bob = CommonNameOBJ("Bob", "@name-1")

#   The common name registry.
cnr = CommonNameRegistry()

#   Add the common name.
cnr.AddCommonName(bob)

#   Create the registry instance.
r = Registry()

#   Add the common name registry to the main registry
r.AddCommonNameRegistry(cnr)

#   Create the forest event with the registry instance.
fev = ForestEvt(r)

#   Create the chapter objects
intro = ChapterOBJ("intro", 0, "C:/Users/Sam/Desktop/pygames-textadventures/chapters/intro.txt", fev, "Bob")

forest = ChapterOBJ("forest", 1, "C:/Users/Sam/Desktop/pygames-textadventures/chapters/forest.txt", fev, "This is an event.")
forestLeft = ChapterOBJ("forestLeft", 2, "C:/Users/Sam/Desktop/pygames-textadventures/chapters/forestLeft.txt", fev, "Turn left from forest.")
forestRight = ChapterOBJ("forestRight", 3, "C:/Users/Sam/Desktop/pygames-textadventures/chapters/forestRight.txt", fev, "Turn right from forest.")
forestBack = ChapterOBJ("forestRight", 4, "C:/Users/Sam/Desktop/pygames-textadventures/chapters/forestBack.txt", fev, "Turn back from forest.")


#   Add the chapters to the main registry.
r.AddChapter(intro)

#   Forest chapters
r.AddChapter(forest)
r.AddChapter(forestLeft)
r.AddChapter(forestRight)
r.AddChapter(forestBack)

#   Execute the current index (which is 0.)
r.ExecuteCurrentIndex()

