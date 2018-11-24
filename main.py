from classes.Maze import Maze
from classes.Robot import Robot
import numpy as np

# ----- MAZE DIMENSION -------
X_DIMENSION = 4
Y_DIMENSION = 4

# ----- REWARD VALUES -------
POSITIVE_LAMBDA = 0.1
NEGATIVE_LAMBDA = 0.4

# ----- OBSTACLES INDEX -------
IDX_OBSTACLES = [7, 9]

# ----- BEGIN & ARRIVAL INDEX -------
IDX_BEGIN_ARRIVAL = [3, 15]

if __name__ == '__main__':
    input_matrix = np.ones(shape=(X_DIMENSION, Y_DIMENSION))
    idx = 0
    for i in range(0, Y_DIMENSION):
        for j in range(0, X_DIMENSION):
            if idx in IDX_OBSTACLES:
                # print(str(i) + ',' + str(j))
                input_matrix[i,j] = 0.
            idx = idx + 1

    # print(input_matrix)
    maze = Maze(input_matrix, POSITIVE_LAMBDA, NEGATIVE_LAMBDA, IDX_BEGIN_ARRIVAL)

    print(foo)
