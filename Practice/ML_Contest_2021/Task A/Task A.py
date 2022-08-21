from numpy.random import uniform
from math import cos, sin, pi
import numpy as np

GENERATE_ONE = 1
GENERATE_TWO = 2
PATH = ""
INPUT_DATA = PATH + "input.txt"
OUTPUT_DATA = PATH + "output.txt"


def generate(type_generate):
    if type_generate == GENERATE_ONE:
        return generate1()
    elif type_generate == GENERATE_TWO:
        return generate2()
    else: raise ValueError(f"type_generate not defined: {type_generate}")

def generate1():  
    a = uniform(0, 1)
    b = uniform(0, 1)
    return (a * cos(2 * pi * b), a * sin(2 * pi * b))
    
def generate2():  
    while True:  
        x = uniform(-1, 1)  
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:  
            continue  
        return (x, y)

COUNT_LINE_EVERY_GENERATOR = 20 # Кол-во сгенерированных данных для каждого алгоритма. При "COUNT_LINE_EVERY_GENERATOR = 10" для двух алгоритмов сгенерируется 20 строк
SIZE_LINE = 100 # Кол-во координат в строке. 1 координата = 2 значения x,y

def generete_data():
    targetes_lines_data = []
    xy_lines_data = []
    for generete_number in [GENERATE_ONE, GENERATE_TWO]:
        for line_number in range(COUNT_LINE_EVERY_GENERATOR):
            xy_data = []
            for i in range(SIZE_LINE):
                x,y = generate(generete_number)
                xy_data += [x,y] # формируем массив со всеми координатами для одной строки
            xy_lines_data.append(xy_data) # собираем все строки с координатами 
            targetes_lines_data.append(generete_number) # Массив целевых значений с номером алгоритма 
    xy_lines_data = np.array(xy_lines_data)
    return xy_lines_data, targetes_lines_data

def calc_model(xy_train, targetes_train):
    # расчет суммы всех параметров
    count_lines = xy_train.shape[0]
    count_values_in_line = xy_train.shape[1]
    # weights = np.ones(count_values_in_line) # Массив весов для всех пар x,y, по умолчанию равен 1
    
    sum_value_generator_1_abs = 0
    sum_value_generator_2_abs = 0
    # В обучающих данных могут быть различное количество данных сформированных 1м и 2м алгоритмом, поэтому для рассчета среднего надо считать кол-во
    count_line_generator_1 = 0
    count_line_generator_2 = 0

    for index_line in range(count_lines):
        target = targetes_train[index_line]
        xy_line = xy_train[index_line]
        abs_sum_xy_values = sum([abs(num) for num in xy_line ])
        if target == GENERATE_ONE:
            sum_value_generator_1_abs += abs_sum_xy_values
            count_line_generator_1 += 1
        elif target == GENERATE_TWO:
            sum_value_generator_2_abs += abs_sum_xy_values
            count_line_generator_2 += 1
        # else: raise ValueError(f"target not defined: {target}")
    return sum_value_generator_1_abs/(count_values_in_line*count_line_generator_1), sum_value_generator_2_abs/(count_values_in_line*count_line_generator_2)

def predict(avg_gen_1, avg_gen_2, avg_detect):
    if abs(avg_gen_1 - avg_detect) < abs(avg_gen_2 - avg_detect): # Если рассматриваемое значение ближе к 1му алгоритму тогда делаем вывод, что данные сгенерированы 1м алгоритмом, в противном случае 2м
        return GENERATE_ONE
    else:
        return GENERATE_TWO

def load_input_data(input_filename):
    input_data = []
    with open(input_filename, 'r') as file:
        for line in file:
            row = [float(n) for n in line.strip().split(" ")]
            input_data.append(row)
    return input_data

def main():
    xy_lines_data, targetes_lines_data = generete_data()
    # assert xy_lines_data.shape[0] == COUNT_LINE_EVERY_GENERATOR*2  and xy_lines_data.shape[1] == SIZE_LINE*2, "Ошибка в количестве рассчитанных данных"

    xy_lines_data.shape

    avg_genereator_1, avg_genereator_2 = calc_model(xy_lines_data, targetes_lines_data)


    # загружаем данные из input.txt
    input_data = load_input_data(INPUT_DATA)

    # Производим прогноз
    predicts_gen = []
    for row in input_data:
        avg_detect = sum(abs(num) for num in row)/len(row)
        predict_generator = predict(avg_genereator_1,avg_genereator_2, avg_detect)
        predicts_gen.append(predict_generator)

    # Записываем результат в output.txt
    with open(OUTPUT_DATA, "w") as file:
        file.write("\n".join(str(num) for num in predicts_gen))


if __name__ == '__main__':
    main()
