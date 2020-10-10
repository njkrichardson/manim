from manimlib.imports import * 
from computer_architecture.atomic.atom import get_bohr_atom, get_electron, get_proton, get_abstract_atom, JigglingSubmobjects, get_atom_grid
from computer_architecture.production.title_credits import IntroQuotation, ChapterTitle, PlanningScene
from computer_architecture.atomic.utils import get_grid_coordinates

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


class MethodicalValenceAbstraction(Scene): 
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

        valence_electrons = JigglingSubmobjects(VGroup(*valence_electrons))
        collapsed_nucleus = JigglingSubmobjects(VGroup(get_proton(radius=0.2)))

        self.play(FadeOut(orbits))
        self.play(ReplacementTransform(electrons, valence_electrons))
        self.play(ReplacementTransform(nucleus, collapsed_nucleus))

        self.wait(2)

class SummaryValenceAbstraction(Scene): 
    def construct(self): 
        atom = get_bohr_atom(show_orbits=True, dynamic=True)
        self.add(atom)
        self.wait(2)

        abstract_atom = get_abstract_atom(dynamic=True) 
        self.add(abstract_atom)
        self.play(ReplacementTransform(atom, abstract_atom))
        self.wait(2)

class SiliconCrystal(Scene): 
    def construct(self): 
        small_crystal = get_atom_grid() 
        self.add(small_crystal)
        self.wait(1)

        large_crystal = get_atom_grid(origin_coords=(3.5, 3.5), n_rows=15, n_cols=15, width=4.5, height=4.5, scale=0.15, electron_radius=0.25)
        self.add(large_crystal)
        self.play(ReplacementTransform(small_crystal, large_crystal))
        self.wait(3)


