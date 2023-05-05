# https://contest.yandex.ru/contest/46304/problems/A/
# A. Подземная доставка

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        commands = []
        for _ in range(n):
            commands.append(file.readline().split())
    return n, commands


# Поиск ответа
def find_answer(n, commands):
    products = {}
    train = []
    for command in commands:
        type = command[0].strip()
        if type == "delete":
            count_remove = int(command[1])
            while count_remove > 0:
                product_cnt, product_name = train.pop()
                count_remove -= product_cnt
                products[product_name] -= product_cnt
                if count_remove < 0:
                    products[product_name] += -count_remove
                    train.append([-count_remove, product_name])
        elif type == "add":
            cnt = int(command[1])
            name = command[2].strip()
            train.append([cnt, name])
            if name not in products:
                products[name] = cnt
            else:
                products[name] += cnt
        elif type == "get":
            name = command[1].strip()
            if name not in products:
                print(0)
            else:
                print(products[name])


def main():
    # считываем входные данные
    n, commands = load_data(INPUT_FILE)
    # Поиск ответа
    find_answer(n, commands)


if __name__ == "__main__":
    main()
