import tkinter as tk

root = tk.Tk()

WIDTH = 600
HEIGHT = 600

c = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
c.pack()

cx = WIDTH // 2
cy = HEIGHT // 2

# ось X
c.create_line(0, cy, WIDTH, cy, width=2)

# ось Y
c.create_line(cx, 0, cx, HEIGHT, width=2)

# def to_canvas(x, y):
#     canvas_x = cx + x
#     canvas_y = cy - y
#     return canvas_x, canvas_y

# def draw_point(x, y, r=3, color="red"):
#     px, py = to_canvas(x, y)

#     c.create_oval(
#         px-r, py-r,
#         px+r, py+r,
#         fill=color,
#         outline=color
#     )

# draw_point(2, 2)
# draw_point(-120, 80)


class Figure():
    def __init__(self, canvas, cx, cy, x, y):
        self.canvas = canvas
        self.cx = cx
        self.cy = cy
        self.x = x
        self.y = y
    def to_canvas(self):
        return (
            self.cx + self.x * 10,
            self.cy - self.y * 10
        )

    def draw_point(self, r=3, color="red"):
        px, py = self.to_canvas()

        self.canvas.create_oval(
            (px-r), (py-r),
            (px+r), (py+r),
            fill=color,
            outline=color
        )


point = Figure(c, cx, cy, 2, 2)
# point.to_canvas()
point.draw_point()

root.mainloop()