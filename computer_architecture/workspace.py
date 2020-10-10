### How to move to coordinates? 

from manimlib.imports import * 
from computer_architecture.atomic.utils import get_electron, get_proton, get_particle, JigglingSubmobjects

class Movement(Scene): 
    def construct(self): 
        # self.show_lattice() 
        # self.get_abstract_atom()
        self.atom_grid() 
        # self.show_atom() 
        # self.get_atom()
        pass 

    def move_a_dot(self): 
        dot = Dot() 
        dot.move_to(UR)
        self.add(dot)
        self.play(dot.shift, UR)
        self.wait(5)

    def show_atom(self): 
        atom = self.get_atom(atomic_number=14)
        self.add(*atom)
        self.play(atom.shift, UR)
        self.wait(5)

    def get_grid_coordinates(self, n_rows : int = 5, n_cols : int = 5, dynamic : bool = False) -> list: 
        assert n_rows > 0 and n_cols > 0, "number of rows and number of columns must both be positive integers"

        origin = 2 * LEFT + 2 * UP 
        width_spacing, height_spacing = (2 * RIGHT - 2 * LEFT) / n_rows, (2 * UP - 2 * DOWN) / n_cols
        grid_coordinates = [] 

        for r in range(n_rows): 
            for c in range(n_cols): 
                grid_coordinates.append(origin + (RIGHT * width_spacing * r) + (DOWN * height_spacing * c))

        return grid_coordinates

    
    def get_abstract_atom(self, atomic_number : int = 14): 
        assert atomic_number == 14, "nothing implemented but silicon"
        nucleus = get_proton() 
        valence_electrons = [get_electron() for _ in range(4)]
        valence_electrons[0].move_to(UP)
        valence_electrons[1].move_to(LEFT)
        valence_electrons[2].move_to(RIGHT)
        valence_electrons[3].move_to(DOWN)

        atom = VGroup(*[*valence_electrons, nucleus])
        self.add(atom)
        self.wait(2) 
        self.play(atom.shift, UR)
        self.wait(5)

    def get_atom(self, atomic_number : int = 14): 
        assert atomic_number <= 14, "need to update electron orbitals to exceed an atomic number of 14"

        protons = [get_proton() for _ in range(atomic_number)]
        neutrons = [get_particle(color=LIGHT_GRAY, fill_opacity=0.3) for _ in range(atomic_number)] # TODO: these look bad, maybe abstract these away immediately lol
        electrons = [get_electron() for _ in range(atomic_number)]

        # nucleus TODO: modularize this
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

        # electron orbitals (currently a sort of hacky impoverished Bohr model) TODO: update to quantum model 
        # let's also just immediately abstract this into the valence shell 

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

        orbital_radii = [(0.55 * shell) for shell in range(1, 6)]
        orbits = [] 
        electrons = [] 

        for i, capacity in enumerate(orbital_populations): 
            orbital_path = Circle(radius=orbital_radii[i], stroke_width=1, color=WHITE)
            position_angles = [i * ((2 * math.pi)/capacity) for i in list(range(capacity))]
            positions = [[orbital_radii[i] * math.cos(angle), orbital_radii[i] * math.sin(angle), 0] for angle in position_angles]
            for position in positions: 
                electron = get_electron() 
                electron.move_to(position) 
                electrons.append(electron)
            orbits.append(orbital_path)

        nucleus = JigglingSubmobjects(nucleus)
        orbitals = VGroup(*orbits)
        electrons = JigglingSubmobjects(VGroup(*electrons))
        
        return VGroup(*[nucleus, orbitals, electrons])
        
        # self.add(nucleus)
        # self.add(orbitals)
        # self.add(electrons)
        # self.wait(5)

    def show_lattice(self): 
        n_x_coords, n_y_coords = 5, 5 
        delta_x = (UR[0] - UL[0])/n_x_coords 
        delta_y = (UR[1] - DR[1])/n_y_coords 
        coords = [] 
        for i in range(n_x_coords): 
            for j in range(n_y_coords): 
                coords.append(UL + [i*delta_x, j*delta_y, 0])

        # corners 
        dot = Dot(color=RED)
        dot.move_to(TOP + LEFT_SIDE + (DR * SMALL_BUFF)) 
        self.add(dot)

        dot = Dot(color=RED)
        dot.move_to(UR) 
        self.add(dot)

        dot = Dot(color=RED)
        dot.move_to(DR) 
        self.add(dot)

        dot = Dot(color=RED)
        dot.move_to(DL) 
        self.add(dot)

        # for coord in coords: 
        #     dot = Dot() 
        #     dot.move_to(coord) 
        #     self.add(dot) 

        self.wait(5) 

        # self.add(plane) 
        # self.wait(5) 

            

