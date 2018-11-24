
class Robot():
    def __init__(self, idx=0):
        self.idx = idx
        print('Robot initialized successfully at : ' + str(self.idx))

    def move(self, new_idx):
        print('Moving from : ' + str(self.idx) + ' to ' + str(new_idx) )
        self.idx = new_idx
        

