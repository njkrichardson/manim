from manimlib.imports import *

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