PATH = ""
INPUT_DATA = PATH + "input.txt"
OUTPUT_DATA = PATH + "output.txt"

def load_input_data(input_filename):
    with open(input_filename, 'r') as file:
        # Считываем строки из входного файла
        rows = list(map(str.strip, file.readlines()))
        # Первую строку разбиваем на значения сторон кубика
        dice_values = [int(value) for value in rows[0].split(" ")]
        # Вторая строка это кол-во подбрасываний
        count_N = int(rows[1])
    return dice_values, count_N

def main():

    # загружаем данные из input.txt
    dice_values, count_N = load_input_data(INPUT_DATA)
    uniq_dice_values = list(set(dice_values))
    
    # Суть: складываем вероятности выпадания каждой грани и умножаем на кол-во бросков и вычитаем вероятности возникновнеия дублей умноженную на кол-во бросков-1. Дубли могут возникать всего N-1 раз.
    # Общая формула выглядит так E(ai*pi)*N-E(ai*(pi**2)*(N-1)) - отнимаем ситуацию когда подряд одинаковые значиеня, т.е. дубли поэтому вероятность в квадрате

    p_plus = 0
    p_minus = 0
    for side_val in set(dice_values):
        p_side = dice_values.count(side_val)/6
        p_plus += side_val*p_side
        p_minus += side_val*(p_side**2)
    expected_value = p_plus*count_N - p_minus*(count_N-1)

    # Записываем результат в output.txt
    with open(OUTPUT_DATA, "w") as file:
        file.write(f"{expected_value}")

if __name__ == '__main__':
    main()