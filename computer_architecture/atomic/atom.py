from manimlib.imports import *

class OpeningQuotation(Scene)
class ChapterIntroduction(Scene): 
    def construct(self): 
        chapter_header = TextMobject("Chapter 1")
        chapter_name = TextMobject("The Atom")
        chapter_name.next_to(chapter_header, direction=DOWN) 
        self.play(FadeIn(chapter_header), FadeInFrom(chapter_name, direction=DOWN))
        self.wait() 