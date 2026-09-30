"""
Задача 1: Флаг Польши
Вариант 4
"""
import os

WHITE = "\033[47m"
RED = "\033[41m"
RESET = "\033[0m"


def draw_flag_poland(width=24, height=12):
    """Рисует флаг Польши: две горизонтальные полосы."""
    stripe_height = height // 2

    # Верхняя полоса — белая
    for _ in range(stripe_height):
        print(WHITE + " " * width + RESET)

    # Нижняя полоса — красная
    for _ in range(stripe_height):
        print(RED + " " * width + RESET)


if __name__ == "__main__":
    draw_flag_poland()