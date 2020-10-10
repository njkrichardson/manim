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

class ChapterTitle(Scene): 
    CONFIG = {
        'chapter_header': TextMobject("Chapter 00"), 
        'chapter_title': TextMobject("Chapter Title"), 
        'pause_duration': 3
    }
    def construct(self): 
        self.chapter_title.next_to(self.chapter_header, direction=DOWN) 
        self.play(FadeIn(self.chapter_header), FadeInFrom(self.chapter_title, direction=DOWN))
        self.wait(self.pause_duration) 
        self.play(FadeOut(VGroup(*[self.chapter_header, self.chapter_title])))

class PlanningScene(Scene): 
    CONFIG = {
        'topics': [f"Topic {i}" for i in range(4)], 
        'highlight_time': 2
    }
    def construct(self): 
        # header
        title = Title("The Plan")
        title.to_edge(edge=UP, buff=MED_SMALL_BUFF)
        h_line = Line(LEFT, RIGHT).scale(FRAME_X_RADIUS - 1)
        h_line.next_to(title, DOWN)

        # bulleted topics list 
        topics_list = BulletedList(*self.topics, buff=MED_SMALL_BUFF)
        topics_list.next_to(h_line, direction=DOWN, aligned_edge=LEFT, buff=LARGE_BUFF)
        self.add(topics_list)

        rect = ScreenRectangle()
        rect.set_width(FRAME_WIDTH - topics_list.get_width() - 2)
        rect.next_to(topics_list, direction=RIGHT, buff=MED_LARGE_BUFF)

        self.play(
            Write(title),
            ShowCreation(h_line),
            ShowCreation(rect),
            run_time = 2
        )
        
        for i in range(len(topics_list)):
            self.play(topics_list.fade_all_but, i)
            self.wait(self.highlight_time) 

        self.play(FadeOut(VGroup(title, h_line, topics_list, rect)))