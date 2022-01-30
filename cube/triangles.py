from turtle import left

import numpy as np
from stl import Mode, mesh

vertices = np.array(
    [
        [1, 0, 1],
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
        [1, 1, 1],
        [1, 0, 1],
    ]
)
faces = np.array(
    [
        [0, 1, 2],
        [3, 4, 5],
    ]
)


right_bc = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        right_bc.vectors[i][j] = vertices[f[j], :]

# Write the mesh to file "cube.stl"
right_bc.save("right_bc_python.stl", mode=Mode.ASCII)

right_bc.x -= 1
right_bc.save("left_bc_python.stl", mode=Mode.ASCII)
