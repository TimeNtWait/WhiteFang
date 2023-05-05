# https://contest.yandex.ru/contest/45468/problems/15/
# Дивизион B
# 15. Великое Лайнландское переселение

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = file.readline().strip()
        cities = file.readline().strip().split()
        cities = list(map(int, cities))
    return n, cities


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет мест переселения
def calc_migration(n, cities):
    '''
    входные данные
    :n — кол-во городов из которых мигрируют
    :cities — Города из которых мигрируют

    выходные данные
    :migration — Города из которых мигрируют с указанием куда мигрировали
    '''
    migration_cities = [-2] * len(cities)
    stack = []
    for idx in range(len(cities)):
        city = cities[idx]
        if len(stack) > 0:
            i_stack = len(stack) - 1
            while i_stack >= 0:
                if city < stack[i_stack][0]:
                    migration_cities[stack[i_stack][1]] = idx
                    stack.pop()
                else:
                    break
                i_stack -= 1
        stack.append([city, idx])
    for stack_item in stack:
        migration_cities[stack_item[1]] = -1
    return migration_cities


def main():
    # считываем входные данные
    n, cities = load_data(INPUT_FILE)
    # Расчет мест переселения
    migration = calc_migration(n, cities)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, " ".join(map(str, migration)))


if __name__ == "__main__":
    main()
