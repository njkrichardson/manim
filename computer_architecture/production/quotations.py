from manimlib.imports import * 

class IntroQuotation(Scene): 
    CONFIG = {
        'author': TextMobject("Rijndael"), 
        'quotation': TextMobject("``Something pithy''"), 
        'run_time': 2, 
        'pause_duration': 1
    }
    def construct(self): 
        self.author.next_to(self.quotation, direction=DOWN)
        
        self.play(
            FadeInFrom(self.author, direction=DOWN), 
            Write(self.quotation, run_time=self.run_time) 
        )
        self.wait(self.pause_duration)
        self.play(FadeOut(VGroup(self.author, self.quotation)))
