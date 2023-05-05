# https://contest.yandex.ru/contest/45468/problems/6/
# 6. Операционные системы lite

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        m = int(file.readline())
        n = int(file.readline())
        partition_pairs = []
        for _ in range(n):
            partition_pairs.append(list(map(int, file.readline().split())))
    return m, n, partition_pairs


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет кол-ва работающих ОС
def calc_count_OS(m, n, partition_pairs):
    '''
    входные данные
    :m — количество секторов на жестком диске
    :n — количество созданых разделов
    :partition_pairs - N пар чисел ai и bi, задающих номера начального и конечного секторов раздела

    выходные данные
    :count_OS - количество работающих операционных систем
    '''
    working_os = []
    for i in range(n):
        new_os = partition_pairs[i]
        deleted_os_list = []
        for idx_os in range(len(working_os)):
            os = working_os[idx_os]
            if new_os[0] <= os[0] <= new_os[1] or new_os[0] <= os[1] <= new_os[1] or os[0] <= new_os[0] <= os[1] or os[0] <= new_os[1] <= os[1]:
                deleted_os_list.append(os)
        working_os.append(new_os)
        deleted_os_list = sorted(deleted_os_list, reverse=True)
        for os in deleted_os_list:
            working_os.remove(os)
    count_os = len(working_os)
    return count_os


def main():
    # считываем входные данные
    m, n, partition_pairs = load_data(INPUT_FILE)
    # Расчет кол-ва работающих ОС
    count_os = calc_count_OS(m, n, partition_pairs)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_os))

if __name__ == "__main__":
    main()
