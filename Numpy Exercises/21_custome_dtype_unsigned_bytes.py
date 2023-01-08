# Create a custom dtype that describes a color as four unisgned bytes (RGBA)
import numpy as np

color = np.dtype([
    ("r", np.ubyte, 1),
    ("g", np.ubyte, 1),
    ("b", np.ubyte, 1),
    ("a", np.ubyte, 1)
])

print(f'{color =}')
