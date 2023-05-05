# https://contest.yandex.ru/contest/45469/problems/17/
# Дивизион А
# 17. Гоблины и шаманы
from collections import deque

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        commands = []
        for _ in range(n):
            commands.append(file.readline().strip())
    return n, commands


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет очереди гоблинов
def calc_queue_goblins(n, commands):
    '''
    входные данные
    :n — количество команд
    :commands — перечень команд

    выходные данные
    :goblins - список гобилнов зашедших к шаману
    '''
    goblins = []
    queue_goblins_1 = deque()
    queue_goblins_2 = deque()

    def balance_queue():
        while len(queue_goblins_1) > len(queue_goblins_2) + 1:
            queue_goblins_2.appendleft(queue_goblins_1.pop())

        while len(queue_goblins_2) > len(queue_goblins_1):
            item = queue_goblins_2.popleft()
            queue_goblins_1.append(item)

    # Для вставки в середину очереди будем использовать две очереди
    for command in commands:
        if command[0] == "+":
            num_goblin = int(command.split()[1])
            queue_goblins_2.append(num_goblin)
        elif command[0] == "*":
            num_goblin = int(command.split()[1])
            queue_goblins_1.append(num_goblin)
        elif command[0] == "-":
            goblins.append(queue_goblins_1.popleft())
        balance_queue()
    return goblins


def main():
    # считываем входные данные
    n, commands = load_data(INPUT_FILE)
    # Расчет очереди гоблинов
    goblins = calc_queue_goblins(n, commands)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(list(map(str, goblins))))


if __name__ == "__main__":
    main()
