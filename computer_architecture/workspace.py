from manimlib.imports import * 

class Movement(Scene): 
    def construct(self): 
        self.move_a_dot() 
        pass 

    def move_a_dot(self): 
        dot = Circle() 
        self.add(dot) 
        starting_position = [7, 0, 0]
        rotating_angle = np.pi/2
        # self.play(dot.move_to(rotate_vector(starting_position, rotating_angle)))
        self.wait(5)
