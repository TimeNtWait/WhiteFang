# https://contest.yandex.ru/contest/45468/problems/18/
# Дивизион B
# 18. Дек с защитой от ошибок
from collections import deque

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        commands = file.readlines()
    return [c.strip() for c in commands]


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Реализация двусторонней очереди
def calc_deque(commands):
    '''
    входные данные
    :commands — команды управления стеком, по одной на строке

    Команды:
    push_front n - Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.
    push_back n - Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.
    pop_front - Извлечь из дека первый элемент. Программа должна вывести его значение.
    pop_back - Извлечь из дека последний элемент. Программа должна вывести его значение.
    front - Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.
    back - Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.
    size - Вывести количество элементов в деке.
    clear - Очистить дек (удалить из него все элементы) и вывести ok.
    exit - Программа должна вывести bye и завершить работу.

    выходные данные
    :result - результат выполнения команд
    '''
    simple_deque = deque()
    result = []
    for command in commands:
        if command.split()[0] == "push_front":
            n = command.split()[1]
            simple_deque.appendleft(n)
            result.append("ok")
        elif command.split()[0] == "push_back":
            n = command.split()[1]
            simple_deque.append(n)
            result.append("ok")

        elif command == "pop_front":
            if len(simple_deque) == 0:
                result.append("error")
            else:
                result.append(simple_deque.popleft())
        elif command == "pop_back":
            if len(simple_deque) == 0:
                result.append("error")
            else:
                result.append(simple_deque.pop())
        elif command == "front":
            if len(simple_deque) == 0:
                result.append("error")
            else:
                result.append(simple_deque[0])
        elif command == "back":
            if len(simple_deque) == 0:
                result.append("error")
            else:
                result.append(simple_deque[-1])
        elif command == "size":
            result.append(str(len(simple_deque)))
        elif command == "clear":
            simple_deque.clear()
            result.append("ok")
        elif command == "exit":
            result.append("bye")
            return result
    return result


def main():
    # считываем входные данные
    commands = load_data(INPUT_FILE)
    # Реализация двусторонней очереди
    result_commands = calc_deque(commands)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(result_commands))


if __name__ == "__main__":
    main()
