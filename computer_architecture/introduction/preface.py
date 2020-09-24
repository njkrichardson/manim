"""
TODO

    * Atom Animation 
"""
from manimlib.imports import *
from computer_architecture.atomic.utils import get_proton, get_electron
from computer_architecture.production.quotations import IntroQuotation

class OpeningQuotation(IntroQuotation): 
    CONFIG={
        'author': TextMobject("Rijndael"), 
        'quotation': TextMobject("``", "A ", "really", " great quotation.''", 
        tex_to_color_map={'really': BLUE}), 
        'run_time': 2.5
    }

class Plan(Scene): 
    def construct(self): 
        self.list_our_topics() 
        self.clear() 
        self.list_lower_level_topics() 
        self.clear() 
        self.list_application_topics() 
        self.clear() 
        self.list_higher_level_topics() 
        self.clear() 
        self.list_macro_topics() 
        pass 

    def list_topics(self, title : str, topics : list): 
        # header
        title = Title(title)
        title.to_edge(edge=UP, buff=MED_SMALL_BUFF)
        h_line = Line(LEFT, RIGHT).scale(FRAME_X_RADIUS - 1)
        h_line.next_to(title, DOWN)
 
        # bulleted topics list 
        our_topics = BulletedList(*topics, buff=MED_SMALL_BUFF)
        our_topics.next_to(h_line, direction=DOWN, aligned_edge=LEFT, buff=LARGE_BUFF)
        # our_topics.to_edge(edge=LEFT, buff=LARGE_BUFF)
        self.add(our_topics)

        rect = ScreenRectangle()
        rect.set_width(FRAME_WIDTH - our_topics.get_width() - 2)
        rect.next_to(our_topics, direction=RIGHT, buff=MED_LARGE_BUFF)

        self.play(
            Write(title),
            ShowCreation(h_line),
            ShowCreation(rect),
            run_time = 2
        )
        
        for i in range(len(our_topics)):
            self.play(our_topics.fade_all_but, i)
            self.wait(2) 

        self.play(FadeOut(VGroup(title, h_line, our_topics, rect)))

    def list_our_topics(self): 
        our_topics = ["Atoms", "Diodes and Transistors", "Digital Circuits", "Logic", "Microarchitecture", "Architecture", "Operating Systems", "Application Software"]
        self.list_topics(title="The Path Ahead", topics=our_topics)

    def list_lower_level_topics(self): 
        ll_topics = ["Fundamental Particles", "Quantum Electrodynamics", "Electrochemistry"]
        self.list_topics(title="Less Abstract", topics=ll_topics)

    def list_higher_level_topics(self): 
        hl_topics = ["Software Engineering", "Computer Networking", "Security and Cryptography", "Scientific Computing", "Machine Learning", "Computational Mathematics"]
        self.list_topics(title="More Abstract", topics=hl_topics)
        
    def list_application_topics(self): 
        application_topics = ["Computational Neuroscience", "Statistical Genetics", "Robotics and Design", "Aerospace Engineering", "Quantitative Finance"]
        self.list_topics(title="Application areas", topics=application_topics)

    def list_macro_topics(self): 
        m_topics = ["Internet", "Economics", "Sociology", "Political Science", "Philosophy"]
        self.list_topics(title="And Beyond", topics=m_topics)

class JigglingSubmobjects(VGroup):
    CONFIG = {
        "amplitude": 0.05,
        "jiggles_per_second": 1,
    }

    def __init__(self, group, **kwargs):
        VGroup.__init__(self, **kwargs)
        for submob in group.submobjects:
            submob.jiggling_direction = rotate_vector(
                RIGHT, np.random.random() * TAU,
            )
            submob.jiggling_phase = np.random.random() * TAU
            self.add(submob)
        self.add_updater(lambda m, dt: m.update(dt))

    def update(self, dt):
        for submob in self.submobjects:
            submob.jiggling_phase += dt * self.jiggles_per_second * TAU
            submob.shift(
                self.amplitude *
                submob.jiggling_direction *
                np.sin(submob.jiggling_phase) * dt
            )

def get_atom_cartoon(n_protons : int = 1, n_electrons : int = 1, scale : float = 1., jiggle : bool = True) -> Mobject: 
    # protons = VGroup(*[get_proton() for _ in range(n_protons)]) 
    # electrons = [get_electron() for _ in range(n_electrons)]
    protons = VGroup(*[get_proton().move_to(rotate_vector(0.275 * n * RIGHT, angle))for n in range(2) for angle in np.arange(0, TAU, TAU / (6 * n) if n > 0 else TAU)])
    
    if jiggle is True: 
        return JigglingSubmobjects(protons) 
    return protons 

class SiliconAtom(Scene): 
    def construct(self): 
        atom = get_atom_cartoon(n_protons=4) 
        self.add(atom) 
        self.wait(5) 
        