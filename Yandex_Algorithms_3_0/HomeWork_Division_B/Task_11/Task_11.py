# https://contest.yandex.ru/contest/45468/problems/11/
# Дивизион B
# 11. Стек с защитой от ошибок

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        commands = file.readlines()
    return [c.strip() for c in commands]


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Имитация стека
def calc_stack(commands):
    '''
    входные данные
    :commands — команды управления стеком, по одной на строке

    Команды:
    push n - Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.
    pop - Удалить из стека последний элемент. Программа должна вывести его значение.
    back - Программа должна вывести значение последнего элемента, не удаляя его из стека.
    size - Программа должна вывести количество элементов в стеке.
    clear - Программа должна очистить стек и вывести ok.
    exit - Программа должна вывести bye и завершить работу.

    выходные данные
    :result - результат выполнения команд
    '''
    stack = []
    result = []
    for command in commands:
        if command[0:4] == "push":
            n = command.split()[1]
            stack.append(str(n))
            result.append("ok")
        elif command == "pop":
            if len(stack) == 0:
                result.append("error")
            else:
                result.append(stack.pop())
        elif command == "back":
            if len(stack) == 0:
                result.append("error")
            else:
                result.append(stack[-1])
        elif command == "size":
            result.append(str(len(stack)))
        elif command == "clear":
            stack = []
            result.append("ok")
        elif command == "exit":
            result.append("bye")
            return result
    return result


def main():
    # считываем входные данные
    commands = load_data(INPUT_FILE)
    # Имитация стека
    result_commands = calc_stack(commands)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(result_commands))


if __name__ == "__main__":
    main()
