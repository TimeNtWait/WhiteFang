# https://contest.yandex.ru/contest/45469/problems/28/
# Дивизион A
# 28. Космический мусорщик
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

# Читаем данные из input.txt
def load_data(filename):
    commands = {}
    with open(filename, "r") as file:
        commands["N"] = file.readline().strip()
        commands["S"] = file.readline().strip()
        commands["W"] = file.readline().strip()
        commands["E"] = file.readline().strip()
        commands["U"] = file.readline().strip()
        commands["D"] = file.readline().strip()
        main_command, number = file.readline().split()
        main_command = main_command.strip()
        number = int(number)
    return main_command, number, commands


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Космический мусорщик
def calc_space_scavenger(main_command, number, commands):
    '''
    входные данные
    :main_command - основная комманда
    :number - числовое значение команды
    :commands -  правила для команд с направлением N, S, W, E, U и D соответственно

    выходные данные
    :count_move - количество перемещений
    '''
    print(commands)
    # assert False
    if number == 0:
        return 0
    count_move = do_commands_stack(main_command, number, commands)
    print(f"res: {count_move}")
    return count_move

# выполнение комманд
def do_commands_stack(command, number, commands):
    stack = [(command, number)]
    res = 0
    while len(stack) > 0:
        com, numb = stack.pop()
        res += 1
        numb -= 1
        if numb == 1:
            res += len(commands[com])
        elif numb > 1:
            for s in list(commands[com]):
                stack.append((s, numb))
    return res





# # выполнение комманд
# def do_commands_recursy(command, number, commands):
#     # print(command, number, commands[command])
#     if number == 4:
#         pre = 0
#         for s in commands[command]:
#             for s2 in commands[s]:
#             # print(f"s: {s}")
#                 pre += len(commands[s2]) + 1
#         return 1 + len(commands[command]) + pre
#     elif number == 3:
#         pre = 0
#         for s in commands[command]:
#             # print(f"s: {s}")
#             pre += len(commands[s])
#         return 1 + len(commands[command]) + pre
#     elif number == 2:
#         return 1 + len(commands[command])
#     elif number == 1:
#         return 1
#     move_programm = 1
#     for c in commands[command]:
#         move_programm += do_commands(c, number - 1, commands)
#     return move_programm
#

def main():
    # считываем входные данные
    main_command, number, commands = load_data(INPUT_FILE)
    # Космический мусорщик
    import time
    start_time = time.time()
    count_move = calc_space_scavenger(main_command, number, commands)
    print(time.time() - start_time)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_move))


if __name__ == "__main__":
    main()
