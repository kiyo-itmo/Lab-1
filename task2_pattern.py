"""
Задача 2: Узор d — вложенные прямоугольники
Вариант 4
"""


def draw_pattern_d(size=20):
    """
    Рисует вложенные прямоугольники.
    size — размер стороны внешнего квадрата (нечётное для симметрии).
    """
    # Матрица символов: 1 = закрашено, 0 = пусто
    grid = [[0] * size for _ in range(size)]

    # Рисуем рамки от внешней к внутренней
    for layer in range(0, size // 2, 2):  # шаг 2 — через слой
        for i in range(layer, size - layer):
            grid[layer][i] = 1           # верх
            grid[size - 1 - layer][i] = 1  # низ
        for i in range(layer, size - layer):
            grid[i][layer] = 1           # лево
            grid[i][size - 1 - layer] = 1  # право

    # Печатаем
    for row in grid:
        print("".join("█" if cell else " " for cell in row))


if __name__ == "__main__":
    draw_pattern_d(21)