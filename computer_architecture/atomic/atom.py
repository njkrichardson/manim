from manimlib.imports import *
from computer_architecture.atomic.utils import get_grid_coordinates

def get_particle(color : str, charge : str = None, radius : float = 0.1, **kwargs):
    result = Circle(
        stroke_color=WHITE,
        stroke_width=0.5,
        fill_color=color,
        fill_opacity=kwargs.pop("fill_opacity", 0.8),
        radius=radius
    )
    if charge is not None: 
        sign = TexMobject(charge) 
        sign.set_stroke(WHITE, 1)
        sign.set_width(0.5 * result.get_width())
        sign.move_to(result)
        result.add(sign)
    return result

def get_proton(radius : float = 0.1):
    return get_particle(RED, "+", radius)

def get_electron(radius : float = 0.05):
    return get_particle(BLUE, "-", radius)

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

    def update(self, dt : float, recursive : bool = True):
        for submob in self.submobjects:
            submob.jiggling_phase += dt * self.jiggles_per_second * TAU
            submob.shift(
                self.amplitude *
                submob.jiggling_direction *
                np.sin(submob.jiggling_phase) * dt
            )

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

    orbital_radii = [(0.55 * shell) for shell in range(1, 6)]
    for i, capacity in enumerate(orbital_populations): 
        position_angles = [i * ((2 * math.pi)/capacity) for i in list(range(capacity))]
        positions = [[orbital_radii[i] * math.cos(angle), orbital_radii[i] * math.sin(angle), 0] for angle in position_angles]
        for position in positions: 
            electron = get_electron() 
            electron.move_to(position) 
            electrons.append(electron)

    if show_orbits is True: 
        orbits = [] 
        for i, capacity in enumerate(orbital_populations): 
            orbital_path = Circle(radius=orbital_radii[i], stroke_width=1, color=WHITE)
            orbits.append(orbital_path)
    
        return electrons, orbits

    return electrons 

def get_bohr_atom(atomic_number : int = 14, dynamic : bool = False, show_orbits : bool = False, return_list : bool = False): 
    assert atomic_number == 14, "only silicon currently implemented"

    atom = [] 

    nucleus = get_atom_nucleus(atomic_number, atomic_number)

    if show_orbits is True:  
        electrons, orbits = get_electrons(atomic_number, show_orbits=show_orbits)
        if return_list is True: 
            atom.append(orbits)
        else: 
            atom.extend(orbits)
    
    else: 
        electrons = get_electrons(atomic_number)

    if dynamic is True: 
        nucleus = JigglingSubmobjects(nucleus)
        electrons = JigglingSubmobjects(VGroup(*electrons))

    atom.append(nucleus)

    if return_list is True:  
        atom.append(electrons)
        return atom 

    else: 
        atom.extend(electrons)
        return VGroup(*atom)
       
def get_abstract_atom(scale : float = 1, electron_radius : float = 1, dynamic : bool = True, n_valence : int = 4): 
    nucleus = get_proton(radius=0.2*scale)
    
    electrons = [] 
    for i in range(n_valence): 
        angle = (2 * math.pi / n_valence) * i 
        electron = get_electron(radius = 0.1 * scale).move_to([electron_radius * math.cos(angle), electron_radius * math.sin(angle), 0])
        electrons.append(electron)
    
    if dynamic is True: 
        nucleus = JigglingSubmobjects(VGroup(nucleus))
        electrons = JigglingSubmobjects(VGroup(*electrons))

    atom = VGroup(nucleus, electrons)
    return atom 
        
def get_atom_grid(origin_coords : tuple = (2, 2), n_rows : int = 5, n_cols : int = 5, width : float = 4, height : float = 4, scale : float = 0.5, electron_radius : float = 0.5): 
    atom_locs = get_grid_coordinates(origin_coords=origin_coords, n_rows=n_rows, n_cols=n_cols, width=width, height=height)
    atoms = [] 
    for loc in atom_locs: 
        atom = get_abstract_atom(dynamic=True, scale=scale, electron_radius=electron_radius).move_to(loc)
        atoms.append(atom)
    return VGroup(*atoms)
