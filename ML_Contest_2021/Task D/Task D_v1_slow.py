import time
PATH = ""
INPUT_DATA = PATH + "input_gen.txt"
# INPUT_DATA = PATH + "input.txt"
OUTPUT_DATA = PATH + "output.txt"

def load_input_data(input_filename):
    with open(input_filename, 'r') as file:
        # Считываем строки из входного файла
        rows = list(map(str.strip, file.readlines()))
        # Первая строка: общее кол-во сувениров и порядковый номер интересующих нас
        number_souvenir = int(rows[0].split(" ")[1])
        # Общий перечень статуэток 
        seq_souvenirs = [int(value) for value in rows[1].split(" ")]
    return number_souvenir, seq_souvenirs



def main():
    start_time = time.time()
    # загружаем данные из input.txt
    number_souvenir, seq_souvenirs = load_input_data(INPUT_DATA)

    # Перечень необходимых статуэток от 1 до N
    needs_souvenirs = list(range(1,number_souvenir+1))

    # Т.к. согласно условию: "Гарантируется, что для всех тестовых данных ответ существует." следовательно для N = 1 можно смело выдавать ответ 1, нет смысла даже искать в цикле
    sum_souvenirs = 0
    if number_souvenir == 1:
        sum_souvenirs = 1
    else: 
        for i in range(len(seq_souvenirs)):
            seq_souvenirs[i]
            i_item_svnr = seq_souvenirs[i]
            # Найдена подходящая статуэтка
            if i_item_svnr in needs_souvenirs:
                finds_souvenirs = [i_item_svnr]
                # начаинаем поиск последовательности
                for j in range(i+1,len(seq_souvenirs)):
                    j_item_svnr = seq_souvenirs[j]
                    finds_souvenirs.append(j_item_svnr)
                    if set(needs_souvenirs) <= set(finds_souvenirs):
                        # Посчитанную сумму учитываем в двух случаях: 1. либо сумма еще не подсчитана и равна нулю. 2. либо рассчитаная сумма меньше предыдущуей но при условии что сумма уже не нулевая
                        new_sum_souvenirs = sum(finds_souvenirs)
                        if sum_souvenirs == 0 or (new_sum_souvenirs < sum_souvenirs):
                            sum_souvenirs = new_sum_souvenirs
                        # print("Найдена стоимость: ", new_sum_souvenirs )
                        i = j
                        break
    print(time.time()-start_time)
    print(sum_souvenirs)
    
    # Записываем результат в output.txt
    with open(OUTPUT_DATA, "w") as file:
        file.write(f"{sum_souvenirs}")


if __name__ == '__main__':
    main()
