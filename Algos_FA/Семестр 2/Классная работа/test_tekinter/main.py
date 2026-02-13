# Тема 3.1. Знакомство с созданием графического интерфейса.

"""Задание 1. Создать программное окно размером 1200х650 и разместить его примерно по центру монитора.
Окно назвать "Первая программа на tkinter".
В данном окне создать плоскость для рисования размером 1100х650. Разместить на нем:
- текст с именем программы и разработчика;
- разбить плоскоть рисования на две части, имитируя песок и море. Для создания моря используйте метод
create_oval.
- разместить в небе квадратное и круглое солнце.
- создать изображение рыбки, расместить ее в море.
- сделать движение рыбки с помощью метода move.
- создать объект "пальма". Разместить несколько пальм рандомно на песке.
- при клике мышью круглое солнце должно переместиться ближе к морю ("уйти в закат"),НЕ используя
метод move. А квадратное солце должно переместиться к морю, используя метод move.
"""

import tkinter
import time
import random

def sun_kvadrat():
    kvadrat = c.create_rectangle(
        50, 50, 150, 150, outline="black", width="2", fill="#B63AAA"
    )
    return kvadrat


def sun_krug(x1, y1, x2, y2):
    c.create_oval(x1, y1, x2, y2, outline="black", width="2", fill="#FFB266")

def point(x, y):
    c.create_oval(x-5, y-5, x+5, y+5, fill="red", outline="red", width=5)

def sun_krug_disappear(x1, y1, x2, y2):
    c.create_oval(x1, y1, x2, y2, outline="yellow", width="2", fill="yellow")


window = (
    tkinter.Tk()
)  # Объект окна верхнего уровня window создается от класса Tk модуля tkinter
# Tk- Библиотека, которая содержит компоненты графического интерфейса
window.title("Первая программа на tkinter")
window.geometry(
    "1200x650+120-70"
)  # 1200на 650 -размер окна, а +120-70 это смещение окна,
# чтобы располагалось окно примерно по центру

c = tkinter.Canvas(window, width=1100, height=650, bg="yellow")

c.pack()  # упакопка (активация) области рисования "с" на окно window
c.create_text(
    150,
    10,
    font="Arial 14 bold italic",
    fill="blue",
    text="Программа....Разработчик ...",
)
c.create_oval(
    -100, 450, 1200, 800, fill="blue"
)  # х0,у0-левый верхний х1,у1-правый нижний угол

c.create_oval(300, 300, 400, 400, outline="black", width="2", fill="#F70606")


kv = sun_kvadrat()
sun_krug(900, 50, 1000, 150)

palma = []
for i in range(5):  # создаем 5 рандомно расположенных пальм
    random_x = random.randint(0, 1000)
    random_y = random.randint(100, 200)
    img = tkinter.PhotoImage("palma.png")
    palma.append(img)
    id_palma = c.create_image(random_x, random_y, anchor=tkinter.NW, image=palma[i])
    window.update()
    time.sleep(0.2)

# for i in range(1):
#     fish = tkinter.PhotoImage("fish.png")
#     id_fish = c.create_image(900, 500, anchor=tkinter.NW, image=fish)
#     for i in range(1, 400):
#         c.move(id_fish, -2, 0)
#         window.update()
#         time.sleep(0.02)

    fish = tkinter.PhotoImage("fish1.png")
    id_fish = c.create_image(100, 500, anchor=tkinter.NW, image=fish)
    for i in range(1, 400):
        c.move(id_fish, 2, 0)
        window.update()
        time.sleep(0.02)


def click_prog(event):
    print(dir(event))
    new_x = event.x
    new_y = event.y
    print(new_x, new_y)
    if 900 <= new_x <= 1000 and 50 <= new_y <= 150:
        sun_krug(600, 350, 700, 450)
        window.update()
        sun_krug_disappear(900, 50, 1000, 150)
    if 50 <= new_x <= 150 and 50 <= new_y <= 150:
        for i in range(1, 150):
            c.move(kv, 2, 2)
            window.update()
            time.sleep(0.02)


c.bind(
    "<Button-1>", click_prog
)  # метод bind связывает событие(нажатие на левую кнопку мыши) с функцией sun
window.mainloop()
