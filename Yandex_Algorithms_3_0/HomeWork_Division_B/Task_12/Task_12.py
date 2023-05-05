# https://contest.yandex.ru/contest/45468/problems/12/
# Дивизион B
# 12. Правильная скобочная последовательность

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        tag_string = file.readline().strip()
    return tag_string


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)

# Проверка скобочной последовательности
def check_tags(tag_string):
    '''
    входные данные
    :tag_string — В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

    выходные данные
    :result_check - Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no
    '''
    stack = []
    for ch in tag_string:
        if ch not in "[](){}":
            continue
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
        elif ch == ")" and (len(stack) == 0 or stack.pop() != "("):
            return "no"
        elif ch == "]" and (len(stack) == 0 or stack.pop() != "[" ):
            return "no"
        elif ch == "}" and (len(stack) == 0 or stack.pop() != "{"):
            return "no"
    if len(stack) > 0:
        return "no"
    return "yes"


def main():
    # считываем входные данные
    tag_string = load_data(INPUT_FILE)
    # Проверка скобочной последовательности
    result_check = check_tags(tag_string)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(result_check))


if __name__ == "__main__":
    main()
