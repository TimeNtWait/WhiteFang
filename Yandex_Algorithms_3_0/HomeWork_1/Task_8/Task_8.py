# https://contest.yandex.ru/contest/45468/problems/8/
# 8. Минимальный прямоугольник

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    coordinates = []
    with open(filename, "r") as file:
        k = int(file.readline())
        for _ in range(k):
            coordinates.append(list(map(int, file.readline().split())))
    return k, coordinates


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет координат прямоугольника
def calc_rectangle(k, coordinates):
    '''
    входные данные
    :k — количество клеток
    :coordinates - k координаты (x,y) закрашенных клеток
    выходные данные
    :rectangle - координат прямоугольника покрывающий все клетки
    '''
    min_x = max_x = coordinates[0][0]
    min_y = max_y = coordinates[0][1]
    for cell in coordinates:
        max_x = max(cell[0], max_x)
        min_x = min(cell[0], min_x)
        max_y = max(cell[1], max_y)
        min_y = min(cell[1], min_y)
    rectangle = [min_x, min_y, max_x, max_y]
    return rectangle


def main():
    # считываем входные данные
    k, coordinates = load_data(INPUT_FILE)
    # Расчет координат прямоугольника
    rectangle = calc_rectangle(k, coordinates)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, " ".join(map(str, rectangle)))

if __name__ == "__main__":
    main()
