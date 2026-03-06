import matplotlib.pyplot as plt

# class Point():
#     def __init__(self, *args):
#         self.args = args
#     def draw(self):
#         x_seq = [item for item in self.args[::2]]+[self.args[0]]
#         y_seq = [item for item in self.args[1::2]]+[self.args[1]]
#         plt.scatter(x_seq, y_seq)
#         plt.plot(x_seq, y_seq)
#         plt.grid(True)
#         plt.xlabel("X")
#         plt.ylabel("Y")
#         plt.axhline(0)
#         plt.axvline(0)
#         plt.show()



# point = Point(2,1,2,4,4,4,4,2)
# point.draw()




SIZE = 20

grid = [['  ' for _ in range(SIZE)] for _ in range(SIZE)]

center = SIZE // 2

for i in range(SIZE):
    grid[center][i] = '--'
    grid[i][center] = '|'

grid[center][center] = '+'
# print(*[''.join(row) for row in grid], sep='\n')


class Point():
    def __init__(self, *args):
        self.args = args
    def draw(self):
        x_seq = [center + item for item in self.args[::2]]+[self.args[0]+center]
        y_seq = [center - item for item in self.args[1::2]]+[self.args[1]-center]
        for i in range(SIZE):
            for j in range(SIZE):
                if (j, i) in zip(x_seq, y_seq):
                    grid[i][j] = 'o'
        print(*[''.join(row) for row in grid], sep='\n')



point = Point(2,1,2,4,4,4,4,2)
point.draw()