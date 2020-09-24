"""
TODO

 * Preface (what we won't cover) 
    * Fundamental particles 
    * Quantum effects 
    * Chemistry 
 * Our First Abstraction 
 * The Silicon Atom 
 * Lattice Structure 
    
"""
from manimlib.imports import *
from computer_architecture.utils.common_scenes import OpeningQuotation

class PrefaceIntroduction(Scene): 
    def construct(self): 
        opening_quotation = TextMobject("``", "A ", "really", " great quotation.''", 
                                        tex_to_color_map={'really': BLUE})
        author = TextMobject("A Pithy Author")
        author.next_to(opening_quotation, direction=DOWN)
        
        self.play(
            FadeInFrom(author, direction=DOWN), 
            Write(opening_quotation, run_time=4)
        )
        self.wait()


# class ChapterIntroduction(Scene): 
#     def construct(self): 
#         chapter_header = TextMobject("Chapter 1")
#         chapter_name = TextMobject("The Atom")
#         chapter_name.next_to(chapter_header, direction=DOWN) 
#         self.play(FadeIn(chapter_header), FadeInFrom(chapter_name, direction=DOWN))
#         self.wait() 





