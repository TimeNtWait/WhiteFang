# https://contest.yandex.ru/contest/45468/problems/13/
# Дивизион B
# 13. Постфиксная запись

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        postfix_string = file.readline().strip()
    return postfix_string


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Расчет постфиксной записи (или обратной польской записи)
def calc_polska_postfix(postfix):
    '''
    входные данные
    :postfix — постфиксная обратная (польская) запись

    выходные данные
    :solution - Результат решения обратной польской  записи
    '''
    stack = []
    if len(postfix) < 3:
        return None
    for i in range(len(postfix)):
        if is_number(postfix[i]):
            stack.append(int(postfix[i]))
        elif postfix[i] in "+-*":
            y = stack.pop()
            x = stack.pop()
            if postfix[i] == "+":
                solution = x + y
            elif postfix[i] == "-":
                solution = x - y
            elif postfix[i] == "*":
                solution = x * y
            # solution = eval(f"{x}{postfix[i]}{y}")
            if i == len(postfix) - 1:
                return solution
            else:
                stack.append(solution)
    return solution


def main():
    # считываем входные данные
    postfix_string = load_data(INPUT_FILE)
    # Расчет постфиксной записи (или обратной польской записи)
    solution = calc_polska_postfix(postfix_string)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(solution))


if __name__ == "__main__":
    main()
