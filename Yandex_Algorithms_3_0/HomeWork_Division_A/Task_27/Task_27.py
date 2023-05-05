# https://contest.yandex.ru/contest/45469/problems/27/
# Дивизион A
# 27. Расстояние по Левенштейну
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        word1 = file.readline().strip()
        word2 = file.readline().strip()
    return word1, word2


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет редакционного расстояние по Левенштейну
def compare_words(word1, word2):
    '''
    входные данные
    :word1 - первое слово для сравнения
    :word2 - второе слово для сравнения

    выходные данные
    :edits_length - редакционного расстояние по Левенштейну
    '''
    dp = [[(j + i if j == 0 or i == 0 else 0) for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    edits_length = dp[-1][-1]
    return edits_length


def main():
    # считываем входные данные
    word1, word2 = load_data(INPUT_FILE)
    # Расчет редакционного расстояние по Левенштейну
    edits_length = compare_words(word1, word2)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(edits_length))


if __name__ == "__main__":
    main()
