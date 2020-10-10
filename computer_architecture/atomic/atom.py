from manimlib.imports import *
from computer_architecture.atomic.utils import get_electron, get_proton, get_particle, JigglingSubmobjects

def get_grid_coordinates(n_rows : int = 5, n_cols : int = 5) -> list: 
    assert n_rows > 0 and n_cols > 0, "number of rows and number of columns must both be positive integers"

    origin = 2 * LEFT + 2 * UP 
    width_spacing, height_spacing = (2 * RIGHT - 2 * LEFT) / n_rows, (2 * UP - 2 * DOWN) / n_cols
    grid_coordinates = [] 

    for r in range(n_rows): 
        for c in range(n_cols): 
            grid_coordinates.append(origin + (RIGHT * width_spacing * r) + (DOWN * height_spacing * c))

    return grid_coordinates

def get_atom_nucleus(n_protons : int = 14, n_neutrons : int = 14): 
    protons = [get_proton() for _ in range(n_protons)]
    neutrons = [get_particle(color=LIGHT_GRAY, fill_opacity=0.3) for _ in range(n_neutrons)] # TODO: these look bad, maybe abstract these away immediately lol

    nucleus_mean = [0, 0, 0] 
    nucleus_std = 0.1
    dimension = 2

        
    for proton in protons: 
        destination = npr.randn(3) * nucleus_std + nucleus_mean
        if dimension is 2: destination[-1] = 0 
        proton.move_to(destination)

    for neutron in neutrons: 
        destination = npr.randn(3) * nucleus_std + nucleus_mean
        if dimension is 2: destination[-1] = 0 
        neutron.move_to(destination)
        
    nucleus = VGroup(*(protons + neutrons))

    return nucleus

def get_electrons(atomic_number : int, show_orbits : bool = False, nucleus_location : np.ndarray = np.array([0, 0, 0])) -> list:
    # electron orbitals (currently a sort of hacky impoverished Bohr model) TODO: update to quantum model 

    # TODO: this info can be put in constants somewhere 
    # orbital_names = ["1s", "2s", "2p", "3s", "3p"]
    orbital_capacities = [2, 2, 6, 2, 6]
    orbital_populations = [0] * 5  

    n_electrons = atomic_number 
    orbital_index = 0 

    while n_electrons > 0: 
        if n_electrons - orbital_capacities[orbital_index] >= 0: 
            orbital_populations[orbital_index] += orbital_capacities[orbital_index]
            n_electrons -= orbital_capacities[orbital_index]
            orbital_index += 1
        else: 
            orbital_populations[orbital_index] = n_electrons
            n_electrons = 0 

    electrons = [] 

    if show_orbits is True: 
        orbital_radii = [(0.55 * shell) for shell in range(1, 6)]
        for i, capacity in enumerate(orbital_populations): 
            position_angles = [i * ((2 * math.pi)/capacity) for i in list(range(capacity))]
            positions = [[orbital_radii[i] * math.cos(angle), orbital_radii[i] * math.sin(angle), 0] for angle in position_angles]
            for position in positions: 
                electron = get_electron() 
                electron.move_to(position) 
                electrons.append(electron)
        orbits = [] 
        for i, capacity in enumerate(orbital_populations): 
            orbital_path = Circle(radius=orbital_radii[i], stroke_width=1, color=WHITE)
            orbits.append(orbital_path)
    
        return electrons, orbits

    else: 
        nucleus_cov = np.eye(3) 
        positions = npr.multivariate_normal(nucleus_location, nucleus_cov, size=atomic_number)
        positions[:, 2] -= positions[:, 2]
        for position in positions: 
            electron = get_electron() 
            electron.move_to(position) 
            electrons.append(electron) 
    
    return electrons 

def get_bohr_atom(atomic_number : int = 14, dynamic : bool = False): 
    assert atomic_number == 14, "only silicon currently implemented"

    nucleus = get_atom_nucleus(atomic_number, atomic_number)
    electrons, orbits = get_electrons(atomic_number, show_orbits=True)

    if dynamic is True: 
        nucleus = JigglingSubmobjects(nucleus)
        electrons = JigglingSubmobjects(VGroup(*electrons))
    
    return VGroup(*[nucleus, *orbits, electrons])
       
class ChapterIntroduction(Scene): 
    def construct(self): 
        # chapter_header = TextMobject("Chapter 1")
        # chapter_name = TextMobject("The Atom")
        # chapter_name.next_to(chapter_header, direction=DOWN) 
        # self.play(FadeIn(chapter_header), FadeInFrom(chapter_name, direction=DOWN))
        # self.wait(2) 
        # self.play(FadeOut(chapter_header))
        # self.play(FadeOut(chapter_name))

        # show a single silicon atom
        self.show_single_atom() 
        self.wait(5)

    def show_single_atom(self): 
        atom = get_bohr_atom(14, True)
        self.add(atom) 
        
        