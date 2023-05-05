from collections import Counter
from collections import Counter
from array import array 
PATH = ""
INPUT_DATA = PATH + "input.txt"
OUTPUT_DATA = PATH + "output.txt"


def load_input_data(input_filename):
    with open(input_filename, 'r') as file:
        # Считываем строки из входного файла
        rows = list(map(str.strip, file.readlines()))
        # Первая строка: общее кол-во сувениров и порядковый номер искомых
        number_souvenir = int(rows[0].split(" ")[1])
        # Общий перечень статуэток
        seq_souvenirs = [int(value) for value in rows[1].split(" ")]
    return number_souvenir, array("i", seq_souvenirs)


def main():
    # загружаем данные из input.txt
    number_souvenir, seq_souvenirs = load_input_data(INPUT_DATA)
    # По условию:"Гарантируется, что для всех тестовых данных ответ существует"
    # следовательно для N = 1 можно смело выдавать ответ 1
    sum_souvenirs = 0
    sum_finds_souvenirs = 0
    first_index = 0
    counter_souvenirs = Counter()
    if number_souvenir == 1:
        sum_souvenirs = 1
    else:
        finds_souvenirs = set()
        j = 0
        first_index = 0
        while j < len(seq_souvenirs):
            sum_finds_souvenirs += seq_souvenirs[j]
            counter_souvenirs[seq_souvenirs[j]] += 1
            if seq_souvenirs[j] <= number_souvenir:
                finds_souvenirs.add(seq_souvenirs[j])
                while len(finds_souvenirs) == number_souvenir:
                    if((sum_finds_souvenirs < sum_souvenirs) or
                            sum_souvenirs == 0):
                        # обновляем сумму
                        sum_souvenirs = sum_finds_souvenirs
                    # Удаляем первый "значимый" элемент
                    sum_finds_souvenirs -= seq_souvenirs[first_index]
                    counter_souvenirs[seq_souvenirs[first_index]] -= 1
                    if seq_souvenirs[first_index] in finds_souvenirs:
                        if counter_souvenirs[seq_souvenirs[first_index]] == 0:
                            finds_souvenirs.remove(seq_souvenirs[first_index])
                    first_index += 1

                    # Также удаляем первые "незначимые" элементы
                    # удаляем до тех пор пока не найдем "значимый"
                    while True:
                        if seq_souvenirs[first_index] > number_souvenir:
                            sum_finds_souvenirs -= seq_souvenirs[first_index]
                            counter_souvenirs[seq_souvenirs[first_index]] -= 1
                            if seq_souvenirs[first_index] in finds_souvenirs:
                                if counter_souvenirs[seq_souvenirs[first_index]] == 0:
                                    finds_souvenirs.remove(seq_souvenirs[first_index])
                            first_index += 1
                        # Найден значимый элемент
                        else:
                            if (sum_finds_souvenirs >= sum_souvenirs):
                                sum_finds_souvenirs -= seq_souvenirs[first_index]
                                counter_souvenirs[seq_souvenirs[first_index]] -= 1
                                if seq_souvenirs[first_index] in finds_souvenirs:
                                    if counter_souvenirs[seq_souvenirs[first_index]] == 0:
                                        finds_souvenirs.remove(seq_souvenirs[first_index])
                                first_index += 1
                            else:
                                break
            j += 1
            
    # Записываем результат в output.txt
    with open(OUTPUT_DATA, "w") as file:
        file.write(f"{sum_souvenirs}")


if __name__ == '__main__':
    main()
