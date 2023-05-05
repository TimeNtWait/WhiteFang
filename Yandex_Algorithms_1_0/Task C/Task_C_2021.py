# https://contest.yandex.ru/contest/27393/problems/C/
# C. Телефонные номера
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


if __name__ == "__main__":
    main()
