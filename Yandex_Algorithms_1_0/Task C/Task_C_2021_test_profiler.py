# https://contest.yandex.ru/contest/27393/problems/C/
# C. Телефонные номера
# import re
PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    phone_book = []
    with open(filename, "r") as file:
        new_number = file.readline().strip()
        for line in file:
            phone_book.append(line.strip())
    return new_number, phone_book


# Записываем результат в output.txt
def save_output(filename, result_check):
    with open(filename, "w") as file:
        file.write(result_check)


# Проверяем наличие номера в записной книжке
def check_numbers(new_number, phone_book):
    def normalization_phone_num(phone_num):
        phone_num = phone_num.replace("+7", "8").replace("-", "").replace("(", "").replace(")", "")
        # phone_num = re.sub(r"[^\d]", "", phone_num)
        if len(phone_num) == 7:
            phone_num = "8495" + phone_num
        return phone_num

    # нормализуем номера к единому виду
    new_number = normalization_phone_num(new_number)
    result_check = []
    for number_in_book in phone_book:
        if normalization_phone_num(number_in_book) == new_number:
            result_check.append("YES")
        else:
            result_check.append("NO")
    return "\n".join(result_check)


def main():
    # считываем входные данные
    new_number, phone_book = load_data(INPUT_FILE)
    # Проверяем наличие номера в записной книжке
    result_check = check_numbers(new_number, phone_book)
    # print(result_check)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, result_check)


import pytest


@pytest.mark.parametrize(
    "numbers, target_result_check",
    [

        (
                [
                    "8(495)430-23-97",
                    "+7-4-9-5-43-023-97",
                    "4-3-0-2-3-9-7",
                    "8-495-430",
                ],
                ["YES", "YES", "NO"],
        ),
        (
                ["86406361642",
                 "83341994118",
                 "86406361642",
                 "83341994118"],
                ["NO", "YES", "NO"],
        ),
        (
                [
                    "+78047952807",
                    "+78047952807",
                    "+76147514928",
                    "88047952807",
                ],
                ["YES", "NO", "YES"],
        ),
    ]
)
def test_check_numbers(numbers, target_result_check):
    new_number = numbers[0]
    phone_book = numbers[1:]
    result_check = check_numbers(new_number, phone_book)
    assert result_check == "\n".join(target_result_check)


if __name__ == "__main__":
    main()
    # pytest.main(args=[__file__])
    from line_profiler import LineProfiler

    lp = LineProfiler()
    lp_wrapper = lp(main)
    lp_wrapper()
    lp.print_stats()
