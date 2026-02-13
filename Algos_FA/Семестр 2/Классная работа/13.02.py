import matplotlib.pyplot as plt

class Figure():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        plt.scatter(self.x, self.y,)
        plt.grid(True)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()


point = Figure(100,100)
point.draw()