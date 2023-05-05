# https://contest.yandex.ru/contest/45468/problems/16/
# Дивизион B
# 16. Очередь с защитой от ошибок
import queue

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


# Реализация очереди
def calc_queue(commands):
    '''
    входные данные
    :commands — команды управления стеком, по одной на строке

    Команды:
    push n - Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.
    pop - Удалить из очереди первый элемент. Программа должна вывести его значение.
    front - Программа должна вывести значение первого элемента, не удаляя его из очереди.
    size - Программа должна вывести количество элементов в очереди.
    clear - Программа должна очистить очередь и вывести ok.
    exit - Программа должна вывести bye и завершить работу.

    выходные данные
    :result - результат выполнения команд
    '''
    simple_queue = queue.Queue()
    result = []
    for command in commands:
        if command[0:4] == "push":
            n = command.split()[1]
            simple_queue.put(str(n))
            result.append("ok")
        elif command == "pop":
            if simple_queue.empty():
                result.append("error")
            else:
                result.append(simple_queue.get())
        elif command == "front":
            if simple_queue.empty():
                result.append("error")
            else:
                result.append(simple_queue.queue[0])
        elif command == "size":
            result.append(str(simple_queue.qsize()))
        elif command == "clear":
            simple_queue.queue.clear()
            result.append("ok")
        elif command == "exit":
            result.append("bye")
            return result
    return result


def main():
    # считываем входные данные
    commands = load_data(INPUT_FILE)
    # Реализация очереди
    result_commands = calc_queue(commands)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(result_commands))


if __name__ == "__main__":
    main()
