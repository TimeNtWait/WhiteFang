# https://contest.yandex.ru/contest/27393/problems/B/
# B. Треугольник
PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        a = file.readline()
        b = file.readline()
        c = file.readline()
    return [int(a), int(b), int(c)]


# Записываем результат в output.txt
def save_output(filename, is_available):
    with open(filename, "w") as file:
        if is_available:
            file.write("YES")
        else:
            file.write("NO")


# Определяем возможность построения треугольника с заданными сторонами
def calc_available(edges):
    if min(edges) <= 0:
        return False
    is_available = (edges[0] < edges[1] + edges[2]) and (edges[1] < edges[0] + edges[2]) and (
            edges[2] < edges[0] + edges[1])
    return is_available


def main():
    # считываем входные данные
    edges = load_data(INPUT_FILE)
    # Определяем возможность построения треугольника с заданными сторонами
    is_available = calc_available(edges)
    # # Записываем результат в output.txt
    save_output(OUTPUT_FILE, is_available)


if __name__ == "__main__":
    main()
