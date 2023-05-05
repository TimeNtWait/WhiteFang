# https://contest.yandex.ru/contest/45469/problems/15/
# Дивизион A
# 15. Поврежденный XML
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        xml_string = file.readline().strip()
    return xml_string


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Корректировка XML
def correct_xml(xml_string):
    '''
    входные данные
    :xml_string — исходная XML строка которую надо скорректировать

    выходные данные
    :valid_xml — итоговая XML строка, с исправленными ошибками
    '''
    stack = []

    def addition_tag(start_pos, end_pos):
        if end_pos == len(xml_string) - 1:
            end_pos = len(xml_string)
        tag = xml_string[start_pos:end_pos]
        check_tag = True
        if tag[1] != "/":
            stack.append([tag, (start_pos, end_pos)])
            check_tag = True
        elif tag[1] == "/":
            if len(stack) == 0:
                # Эта ситуация как раз говорит о том что первый тэг стоит как закрывающий, но мы все-равно помечаем,
                # что все хорошо, чтобы произошло добалвение следующего тэга
                stack.append([tag, (start_pos, end_pos)])
                check_tag = True
            elif stack[-1][0] == tag.replace("/", ""):
                stack.pop()
                check_tag = True
            else:
                stack.append([tag, (start_pos, end_pos)])
                # Не всегда проблема может быть именно в последних двух бывает, что и у предпоследних двух, например
                # <l><it><wit></l>, поэтому требуется дополнительная проверка
                for item in stack:
                    if item[0] == tag.replace("/", ""):
                        stack.pop()
                        break
                check_tag = False
        if not check_tag and len(stack[-2][0]) != len(stack[-1][0]) - 1:
            stack.pop()
            return None
        return check_tag

    def find_change_symbol(open_tag_pos, close_tag_pos):
        open_tag = xml_string[open_tag_pos[0]: open_tag_pos[1]]
        close_tag = xml_string[close_tag_pos[0]: close_tag_pos[1]]
        if open_tag[0] != '<':
            return (open_tag_pos[0], open_tag_pos[0] + 1, "<")
        elif open_tag[-1] != '>':
            return (open_tag_pos[1] - 1, open_tag_pos[1], ">")
        elif close_tag[0] != '<':
            return (close_tag_pos[0], close_tag_pos[0] + 1, "<")
        elif close_tag[1] != '/':
            return (close_tag_pos[0] + 1, close_tag_pos[0] + 2, "/")
        elif close_tag[-1] != '>':
            return (close_tag_pos[1] - 1, close_tag_pos[1], ">")
        elif open_tag[1:-1] != close_tag[2:-1]:
            # Нужно выбрать какой именно тэг брать за основу, главное чтобы там были буквы, а не спецсимволы "</>"
            if close_tag[2:-1].isalpha():
                return (open_tag_pos[0] + 1, open_tag_pos[-1] - 1, close_tag[2:-1])
            else:
                return (close_tag_pos[0] + 2, close_tag_pos[-1] - 1, open_tag[1:-1])
    start_pos = end_pos = 0
    open_tag = True
    check_tag = True
    for idc in range(1, len(xml_string)):
        char = xml_string[idc]
        if char == "<" and not open_tag:
            start_pos = idc
            open_tag = True
        elif char == "<" and open_tag:
            if idc == len(xml_string) - 1:
                end_pos = idc
                open_tag = False
                check_tag = addition_tag(start_pos, end_pos)
            elif xml_string[idc - 1] == "<" or xml_string[idc - 1] == ">":
                pass
            elif xml_string[idc + 1] == "<":
                end_pos = idc + 1
                open_tag = False
                check_tag = addition_tag(start_pos, end_pos)
                if check_tag is not None:
                    start_pos = idc + 1
            elif xml_string[idc + 1] == ">":
                end_pos = idc + 2
                open_tag = False
                check_tag = addition_tag(start_pos, end_pos)
                if check_tag is not None:
                    start_pos = idc + 2
            elif xml_string[idc + 1] != "<":
                end_pos = idc
                open_tag = True
                check_tag = addition_tag(start_pos, end_pos)
                if check_tag is not None:
                    start_pos = idc
        elif char == ">" and check_tag is None:
            end_pos = idc + 1
            check_tag = addition_tag(start_pos, end_pos)
            start_pos = end_pos + 1
        elif char == ">" and not open_tag and xml_string[idc - 1] == ">":
            start_pos = idc
            open_tag = True
        elif char == ">" and open_tag and xml_string[idc - 1] != "<":
            end_pos = idc
            open_tag = False
            check_tag = addition_tag(start_pos, end_pos + 1)
            if check_tag is not None:
                start_pos = end_pos + 1

        elif idc == len(xml_string) - 1:
            check_tag = addition_tag(start_pos, idc + 1)
        if not check_tag and check_tag is not None:
            break
    if not check_tag or len(stack) != 0:
        open_tag_start = stack[-2][1][0]
        open_tag_end = stack[-2][1][1]
        close_tag_start = stack[-1][1][0]
        close_tag_end = stack[-1][1][1]

        open_tag = xml_string[open_tag_start: open_tag_end]
        close_tag = xml_string[close_tag_start:close_tag_end]

        change_char = find_change_symbol((open_tag_start, open_tag_end), (close_tag_start, close_tag_end))
        list_xml = list(xml_string)
        list_xml[change_char[0]: change_char[1]] = list(change_char[2])
        valid_xml = "".join(list_xml)
        return valid_xml

    return xml_string


def main():
    # считываем входные данные
    xml_string = load_data(INPUT_FILE)
    # Корректировка XML
    valid_xml = correct_xml(xml_string)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, valid_xml)


if __name__ == "__main__":
    main()
