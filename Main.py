# from Rubic_Cube import Rubic_Cube
# from SolCorners import is_corner_solved
from SolCorners import ExtendRubic_Cube
import copy

cube = ExtendRubic_Cube()
cube.shuffle(6)
test = copy.deepcopy(cube.cube)
cube.display()
print(cube.Brute_force(test))
print(cube.count)

