# https://contest.yandex.ru/contest/45469/problems/13/
# Дивизион A
# 13. Значение логического выражения
import re

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        task_string = file.readline().strip()
    return task_string


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Переаод из инфексного вида в постфиксный
def infix_to_postfix(task_string):
    priority = {"!": 1, "&": 2, "|": 3, "^": 3}
    # Разбить строку на операции и операнды
    if task_string[0] in ["&", "|", "^"]:
        return -1
    # Поиск ошибочных ситуаций
    bad_symbols = re.findall(r"[^01\s|&^!)(]", task_string)
    bad_symbols += re.findall(r"[01]\s+[01]", task_string)
    bad_symbols += re.findall(r"[|&^!]\s*[|&^]", task_string)
    bad_symbols += re.findall(r"[|&^!]\s*\)?\s*$", task_string)
    bad_symbols += re.findall(r"[|&^!]\s*\)", task_string)
    bad_symbols += re.findall(r"\(\s*?[|&^]", task_string)
    if len(bad_symbols) != 0:
        return -1
    task_string = re.split(r"([|&^!)(])", task_string)
    stack = []
    postfix_list = []
    cnt_tags = 0
    for s in task_string:
        if s.strip() == "":
            continue
        if s not in ("|", "&", "^", "!", "(", ")"):
            postfix_list.append(s)
        elif s in ("|", "&", "^", "!"):
            i = len(stack) - 1
            while i >= 0:
                if stack[i] == "(":
                    break
                if priority[s] >= priority[stack[i]]:
                    postfix_list.append(stack[i])
                    stack.pop()
                i -= 1
            stack.append(s)
        elif s == "(":
            cnt_tags += 1
            stack.append(s)
        elif s == ")":
            cnt_tags -= 1
            if cnt_tags < 0:
                return -1
            i = len(stack) - 1
            while stack[i] != "(":
                postfix_list.append(stack.pop())
                i -= 1
            stack.pop()
    if cnt_tags > 0:
        return -1
    for i in range(len(stack), 0, -1):
        postfix_list.append(stack.pop())
    return postfix_list


# Проверка на число
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Расчет постфиксной заиси уравнения
def calc_postfix(postfix):
    stack = []
    if len(postfix) == 2 and postfix[1] != "!":
        return "WRONG"
    for i in range(len(postfix)):
        if postfix[i].strip() == "":
            continue
        if is_number(postfix[i]):
            stack.append(int(postfix[i]))
        elif postfix[i] == "!":
            x = stack.pop()
            solution = int(not x)
            if i == len(postfix) - 1:
                return solution
            else:
                stack.append(solution)
        elif postfix[i] in "|&^":
            y = stack.pop()
            x = stack.pop()
            if postfix[i] == "|":
                solution = x | y
            elif postfix[i] == "&":
                solution = x & y
            elif postfix[i] == "^":
                solution = x ^ y
            # solution = eval(f"{x}{postfix[i]}{y}")
            if i == len(postfix) - 1:
                return solution
            else:
                stack.append(solution)
    if len(stack) == 1:
        return int(stack[0])


# Расчет уравнения
def calc_equation(task_string):
    '''
    входные данные
    :task_string — Строка с исходным уравнением

    выходные данные
    :result_check_transporters - Ответ уравнения
    '''
    postfix_list = infix_to_postfix(task_string)
    if postfix_list == -1:
        return "WRONG"
    for i in range(len(postfix_list)):
        postfix_list[i] = postfix_list[i].strip()
    answer = calc_postfix(postfix_list)
    return answer


def main():
    # считываем входные данные
    task_string = load_data(INPUT_FILE)
    # Расчет уравнения
    answer = calc_equation(task_string)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(answer))


if __name__ == "__main__":
    main()
