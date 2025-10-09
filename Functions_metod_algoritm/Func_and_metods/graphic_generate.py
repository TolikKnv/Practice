import matplotlib.pyplot as plt


def line_intersection(a, b, c, d):
    """
Находит пересечение двух отрезков AB и CD.
Возвращает координаты точки пересечения или None, если пересечения нет.
    """
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x4, y4 = d

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None  # Параллельные или совпадающие линии

    # The expression `px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) /
    # denom` is calculating the x-coordinate of the intersection point of two line segments AB and CD.
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

    # Проверка, что точка лежит внутри обоих отрезков
    if (
        min(x1, x2) <= px <= max(x1, x2)
        and min(y1, y2) <= py <= max(y1, y2)
        and min(x3, x4) <= px <= max(x3, x4)
        and min(y3, y4) <= py <= max(y3, y4)
    ):
        return px, py

    return None


# Ввод координат
print("Введите координаты первого отрезка (x1 y1 x2 y2):")
# The line `x1, y1, x2, y2 = map(float, input().split())` is taking input from the user in the form of
# space-separated values and converting those values into floating-point numbers. Here's a breakdown
# of what each part does:
x1, y1, x2, y2 = map(float, input().split())

print("Введите координаты второго отрезка (x3 y3 x4 y4):")
x3, y3, x4, y4 = map(float, input().split())

# Точки отрезков
A, B = (x1, y1), (x2, y2)
C, D = (x3, y3), (x4, y4)

# Проверяем пересечение
point = line_intersection(A, B, C, D)

# Вывод результата
if point:
    print(f"Отрезки пересекаются в точке {point}")
else:
    print("Отрезки не пересекаются.")

# Построение графика
plt.plot([A[0], B[0]], [A[1], B[1]], "b-", linewidth=2, label="Отрезок AB")
plt.plot([C[0], D[0]], [C[1], D[1]], "g-", linewidth=2, label="Отрезок CD")

# Отметим точки
plt.scatter([A[0], B[0], C[0], D[0]], [A[1], B[1], C[1], D[1]], color="black", zorder=5)

# Если есть пересечение — выделим точку
if point:
    plt.scatter(*point, color="red", s=100, zorder=10, label=f"Пересечение {point}")
else:
    plt.text(
        (x1 + x2 + x3 + x4) / 4,
        (y1 + y2 + y3 + y4) / 4,
        "Нет пересечения",
        color="red",
        fontsize=12,
    )


# The code snippet you provided is responsible for plotting the two line segments (AB and CD)
# on a 2D plane and visualizing their intersection point if they intersect. Here's a
# breakdown of what each part of the code is doing:
plt.legend()


# `plt.grid(True)` in the provided code is a function call that enables the grid on the plot. When
# `plt.grid(True)` is called with the argument `True`, it turns on the grid lines on the plot. This
# helps in visually aligning data points and understanding the scale of the plot more effectively.
plt.grid(True)


# `plt.axis("equal")` in the provided code snippet is setting the aspect ratio of the plot to be equal
# along both the x-axis and y-axis. This means that the scaling of the plot will be such that one unit
# along the x-axis is equal to one unit along the y-axis, ensuring that the plot is displayed in a
# square aspect ratio.
plt.axis("equal")


# `plt.title("Пересечение двух отрезков на плоскости")` is setting the title of the plot to
# "Пересечение двух отрезков на плоскости" in Russian. This title provides a descriptive heading for
# the plot, indicating that it shows the intersection of two line segments on a plane. It helps
# viewers understand the context or purpose of the plot before analyzing the visual representation of
# the line segments and their intersection point.
plt.title("Пересечение двух отрезков на плоскости")


# `plt.xlabel("X")` is a function call in Matplotlib that sets the label for the x-axis of the plot.
# In this case, it sets the label to "X", indicating that the x-axis represents the values related to
# the variable X. This labeling helps in providing context to the plot by specifying what the x-axis
# represents in terms of the data being visualized.
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
