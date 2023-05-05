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
    max_len_command = 0
    for val in commands.values():
        max_len_command = max(max_len_command, len(val))
    dp = [[1] * (len(SYMBOLS) + 1) for _ in range(number)]

    for n in range(1, number):
        for s in range(len(SYMBOLS)):
            command = commands[SYMBOLS[s]]
            for i in range(len(command)):
                symb = command[i]
                index_symb = dict_w2i[symb]
                dp[n][s] = dp[n][s] + dp[n - 1][index_symb]
    count_move = dp[-1][dict_w2i[main_command]]
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


def main():
    # считываем входные данные
    main_command, number, commands = load_data(INPUT_FILE)
    # Космический мусорщик
    count_move = calc_space_scavenger(main_command, number, commands)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_move))


if __name__ == "__main__":
    main()
