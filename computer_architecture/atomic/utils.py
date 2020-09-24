from manimlib.imports import *

def get_charged_particles(color, sign, radius=0.1):
    result = Circle(
        stroke_color=WHITE,
        stroke_width=0.5,
        fill_color=color,
        fill_opacity=0.8,
        radius=radius
    )
    sign = TexMobject(sign)
    sign.set_stroke(WHITE, 1)
    sign.set_width(0.5 * result.get_width())
    sign.move_to(result)
    result.add(sign)
    return result

def get_proton(radius=0.1):
    return get_charged_particles(RED, "+", radius)

def get_electron(radius=0.05):
    return get_charged_particles(BLUE, "-", radius)