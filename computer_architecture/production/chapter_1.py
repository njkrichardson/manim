from manimlib.imports import * 
from computer_architecture.atomic.atom import get_bohr_atom, get_electron, get_proton
from computer_architecture.production.title_credits import IntroQuotation, ChapterTitle, PlanningScene

class Preface(IntroQuotation): 
    CONFIG={
    'author': TextMobject("Rijndael"), 
    'quotation': TextMobject("``", "A ", "really", " great quotation.''", 
    tex_to_color_map={'really': BLUE}), 
    'run_time': 2.5
    }

class TitleScene(ChapterTitle): 
    CONFIG = {
        'chapter_header': TextMobject("Chapter 1"), 
        'chapter_title': TextMobject("The Atom") 
    }

class Forecast(PlanningScene): 
    CONFIG = {
        'topics': ['Single Atoms', 'Valence Abstraction', 'Crystals', 'Doping', 'Semiconductors']
    }

class SingleAtom(Scene): 
    def construct(self): 
        self.show_single_atom()
        self.wait(5)

    def show_single_atom(self): 
        atom = get_bohr_atom(atomic_number=14, dynamic=True, show_orbits=True)
        self.add(atom)

class ValenceAbstraction(Scene): 
    def construct(self): 
        orbits, nucleus, electrons = get_bohr_atom(atomic_number=14, dynamic=True, show_orbits=True, return_list=True)
        orbits = VGroup(*orbits)

        self.add(orbits) 
        self.add(nucleus)
        self.add(electrons)
        self.wait(2)

        # show only valence electrons, remove orbital rings, remove protons
        valence_electrons = [get_electron(radius=0.15) for _ in range(4)]

        radius = 2
        for electron, position in zip(valence_electrons, [direction * radius for direction in [UP, RIGHT, DOWN, LEFT]]): 
            electron.move_to(position)

        valence_electrons = VGroup(*valence_electrons)
        collapsed_nucleus = get_proton(radius=0.2)

        self.play(FadeOut(orbits))
        self.play(Transform(electrons, valence_electrons))
        self.play(Transform(nucleus, collapsed_nucleus))

        self.wait(2)

