"""
Задача 4: Диаграмма процентного соотношения
Вариант 4: Среднее по модулю первых 125 и вторых 125 чисел
"""


def read_sequence(filename="sequence.txt"):
    """Читает числа из файла."""
    with open(filename, "r", encoding="utf-8") as f:
        numbers = []
        for line in f:
            line = line.strip()
            if line:
                numbers.append(float(line))
    return numbers


def calculate_averages(numbers):
    """Среднее по модулю первых 125 и вторых 125 чисел."""
    first_125 = numbers[:125]
    second_125 = numbers[125:250]

    avg_first = sum(abs(x) for x in first_125) / len(first_125)
    avg_second = sum(abs(x) for x in second_125) / len(second_125)

    return avg_first, avg_second


def draw_diagram(a, b, label_a="Первые 125", label_b="Вторые 125"):
    """Рисует диаграмму процентного соотношения."""
    total = a + b
    pct_a = a / total * 100
    pct_b = b / total * 100

    bar_length = 50
    bar_a = int(pct_a / 100 * bar_length)
    bar_b = int(pct_b / 100 * bar_length)

    print("=" * 60)
    print("Диаграмма процентного соотношения")
    print("=" * 60)
    print()
    print(f"{label_a}: avg|X| = {a:.4f}  →  {pct_a:.2f}%")
    print("█" * bar_a + "░" * (bar_length - bar_a))
    print()
    print(f"{label_b}: avg|X| = {b:.4f}  →  {pct_b:.2f}%")
    print("█" * bar_b + "░" * (bar_length - bar_b))
    print()
    print(f"Сумма процентов: {pct_a + pct_b:.2f}%")


if __name__ == "__main__":
    numbers = read_sequence("sequence.txt")
    print(f"Прочитано чисел: {len(numbers)}")
    a, b = calculate_averages(numbers)
    draw_diagram(a, b)