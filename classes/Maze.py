import numpy as np

class Maze():
    def __init__(self, x):
        self.n = x.shape[0] # Rows
        self.m = x.shape[1] # Columns

        self.maze = x

        # self.weight_mat = self.initialize_weight_mat()

    def initialize_weight_mat(self):
        weight_mat = np.zeros(shape=(self.n*self.m,self.n*self.m))
        print(weight_mat)
        for i in range(0, self.n):
            for j in range(0, self.m):
                idx_list = []
                # print(self.maze[i,j])
                try:
                    if (self.maze[i,j+1] == 1):
                        idx_list.append()
                except os as error:
                    pass
                    
    def coord2idx(self, x, y):
        value = (x * self.m + y)
        print(value)
        return value

    def update_weight(self):
        pass
