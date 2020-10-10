from manimlib.imports import *

def get_grid_coordinates(n_rows : int = 5, n_cols : int = 5, origin_coords : tuple = (2, 2), width : float = 2, height : float = 2) -> list: 
    assert n_rows > 0 and n_cols > 0, "number of rows and number of columns must both be positive integers"

    origin = origin_coords[0] * LEFT + origin_coords[1] * UP 
    width_spacing, height_spacing = (width * RIGHT - origin_coords[0] * LEFT) / n_rows, (origin_coords[1] * UP - height * DOWN) / n_cols
    grid_coordinates = [] 

    for r in range(n_rows): 
        for c in range(n_cols): 
            grid_coordinates.append(origin + (RIGHT * width_spacing * r) + (DOWN * height_spacing * c))

    return grid_coordinates