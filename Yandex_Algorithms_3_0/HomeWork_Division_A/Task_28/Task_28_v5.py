# https://contest.yandex.ru/contest/45469/problems/28/
# Дивизион A
# 28. Космический мусорщик
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
SYMBOLS = 'NSWEUD'

# Читаем данные из input.txt
def load_data(filename):
    commands = {}
    with open(filename, "r") as file:
        for c in SYMBOLS:
            commands[c] = file.readline().strip()
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
    dict_w2i = {}
    for i, c in enumerate(SYMBOLS):
        dict_w2i[c] = i
    # dict_w2i = {'N': 1, 'S': 2, 'W': 3, 'E': 4, 'U': 5, 'D': 6}

    print(f"commands:{commands}")
    max_len_command = 0
    for val in commands.values():
        max_len_command = max(max_len_command, len(val))
    print(f"max_len_command:{max_len_command}")
    # dp = [[1]*(len(SYMBOLS)+1) for _ in range(max_len_command+1)]
    dp = [[1]*(len(SYMBOLS)+1) for _ in range(number)]

    print(dp)
    print(f"dp shape: {len(dp)}-{len(dp[0])}")
    for n in range(1, number):
        print(f"n: {n}")
        for s in range(len(SYMBOLS)):
            command = commands[SYMBOLS[s]]
            for i in range(len(command)):
                symb = command[i]
                index_symb = dict_w2i[symb]
                dp[n][s] = dp[n][s] + dp[n-1][index_symb]
                # print(dp)
                # assert False
                # pass
    print(dp)
    print(dp[-1][dict_w2i[main_command]])

            # print(f"s: {s}, SYMBOLS:{SYMBOLS[s]}")
            # for c in range(len(commands)):


    assert False
    def word_to_int(commands):
        int_commands = {}
        for key in commands:
            int_commands[dict_w2i[key]] = [dict_w2i[s] for s in commands[key]]
        return int_commands

    commands = word_to_int(commands)
    print(commands)
    # assert False
    if number == 0:
        return 0
    count_move = do_commands_stack(dict_w2i[main_command], number, commands)
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
            for s in commands[com]:
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
