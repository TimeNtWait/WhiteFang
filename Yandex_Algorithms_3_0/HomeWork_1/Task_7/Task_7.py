# https://contest.yandex.ru/contest/45468/problems/7/
# 7. SNTP
from datetime import datetime, timedelta

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# По условию надо округлять математически, но питон 0.5 округляет как 0, избавляемся от этого
def my_round(n):
    return int(n + 0.5)


# Читаем данные из input.txt
def load_data(filename):
    format = '%H:%M:%S'
    with open(filename, "r") as file:
        a = datetime.strptime(file.readline().strip(), format)
        b = datetime.strptime(file.readline().strip(), format)
        c = datetime.strptime(file.readline().strip(), format)
    return a, b, c


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет времени посылки между клиентом и сервером
def calc_time(a, b, c):
    '''
    входные данные
    :a — время отправления Клиентом (по клиентскому времени)
    :b — время получения Сервером (по точному серверному времени)
    :c - время получения Клиентом ответа от Сервера (по клиентскому времени)

    выходные данные
    :res_time - точное время полученное от сервера
    '''
    # Определяем разницу между отправкой и получением данных и делим на 2
    delta_seconds = (c - a).seconds / 2
    # Округляем по правилам матеамтики и переводим в таймдельту
    delta_seconds = timedelta(seconds=my_round(delta_seconds))
    res_time = b + delta_seconds
    return res_time


def main():
    # считываем входные данные
    a, b, c = load_data(INPUT_FILE)
    # Расчет времени посылки между клиентом и сервером
    res_time = calc_time(a, b, c)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, res_time.strftime("%H:%M:%S"))


if __name__ == "__main__":
    main()
