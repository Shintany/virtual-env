import numpy as np

class Maze():
    def __init__(self, x):
        self.n = x.shape[0] # Rows
        self.m = x.shape[1] # Columns

        self.maze = x

        print(self.maze)
        self.weight_mat = self.initialize_weight_mat()

    def initialize_weight_mat(self):
        weight_mat = np.zeros(shape=(self.n*self.m,self.n*self.m))
        # print(weight_mat)
        for i in range(0, self.n):
            for j in range(0, self.m):
                idx_list = []
                try:
                    if (j + 1 != self.m):
                        if (self.maze[i,j+1] == 1): # Check right
                            idx_list.append(self.coord2idx(i,j+1))
                    if(j - 1 >= 0):
                        if (self.maze[i, j-1] == 1): # Check left
                            idx_list.append(self.coord2idx(i,j-1))
                    if(i + 1 != self.n):
                        if (self.maze[i+1, j] == 1): # Check bottom
                            idx_list.append(self.coord2idx(i+1,j))
                    if(i - 1 >= 0):
                        if (self.maze[i-1, j] == 1): # Check above
                            idx_list.append(self.coord2idx(i-1,j))
                    print(idx_list)
                except:
                    print('Error at : (' + str(x) + ',' + str(y) + ')')
                    quit()
                    
    def coord2idx(self, x, y):
        # print('I received : (' + str(x) + ',' + str(y) + ')')
        value = (x * self.m + y)
        # print(value)
        return value

    def update_weight(self):
        pass
