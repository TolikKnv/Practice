import inspect
import module

class Board:
    def __init__(self):
        self.pole = [[" " for j in range(3)] for i in range(3)]
        self.current = "X"

    def display(self):
        for i in self.pole:
            print(*i, sep="|")
            print("-" * 5)

    def win(self, pole):
        flag = 0
        for i in range(3):
            if pole[i][0] == pole[i][1] == pole[i][2] != ' ':
                print(f"{self.current} win")
                flag = 1
                break
        for i in range(3):
            if pole[0][i] == pole[1][i] == pole[2][i]!= ' ':
                print(f"{self.current} win")
                flag = 1
                break
        if pole[0][0] == pole[1][1] == pole[2][2]!= ' ':
            flag = 1
            print(f"{self.current} win")
        elif pole[0][2] == pole[1][1] == pole[2][0]!= ' ':
            flag = 1
            print(f"{self.current} win")
        return flag

    def make_move(self, i, j, znach):
        if znach != self.current:
            print(f"Ошибка! Сейчас ход игрока '{self.current}'")
            return
        if self.pole[i][j] != " ":
            print("Клетка уже занята!")
            return

        self.pole[i][j] = znach
        # print('Ход сделан!')
        self.display()
        print()
        if self.win(self.pole):
            exit()
        self.current = "O" if self.current == "X" else "X"


game = Board()
game.make_move(1, 1, "X")
game.make_move(1, 2, "O")
game.make_move(0, 0, "X")
game.make_move(0, 2, "O")
game.make_move(2, 2, "X")
print(inspect.getsource(module.Board))