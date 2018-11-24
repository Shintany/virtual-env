import numpy as np
from .Robot import Robot

class Maze():
    def __init__(self, x, positive_lambda = 0.1, negative_lambda = 0.4, idx_beg_arr = [0,0]):

        # ------ MAZE SHAPE --------
        self.n = x.shape[0] # Rows
        self.m = x.shape[1] # Columns

        # ------ MAZE --------
        self.maze = x

        # ------ REWARD VALUES --------
        self.pos_lmbda = positive_lambda
        self.neg_lmbda = negative_lambda

        # ------ MAZE WEIGHT MATRIX --------
        self.weight_mat = self.initialize_weight_mat()

        # ------ MAZE EXIT --------
        self.arrival = idx_beg_arr[1]
 
        # ------ MAZE ROBOT --------
        self.robot = Robot(idx_beg_arr[0])

    def initialize_weight_mat(self):
        weight_mat = np.zeros(shape=(self.n*self.m,self.n*self.m))
        # print(weight_mat)
        for i in range(0, self.n):
            for j in range(0, self.m):
                idx_list = []
                try:
                    if(self.maze[i,j] == 1):
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
                        # print(idx_list)
                        for idx in idx_list:
                            weight_mat[self.coord2idx(i,j), idx] = 1/len(idx_list)
                except:
                    print('Error at : (' + str(i) + ',' + str(j) + ')')
                    quit()
        # print(weight_mat)
                    
    def coord2idx(self, x, y):
        # print('I received : (' + str(x) + ',' + str(y) + ')')
        value = (x * self.m + y)
        # print(value)
        return value

    def idx2coord(self, idx):
        return(int( idx/self.m ) , idx%self.m)

    def update_weight(self):
        pass
        
