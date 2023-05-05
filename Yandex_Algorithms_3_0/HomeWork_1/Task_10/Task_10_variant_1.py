# https://contest.yandex.ru/contest/45468/problems/10/
# 10. Скучная лекция

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"

from collections import Counter


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        word = file.readline().strip()
    return word


# Расчет кол-ва возможных подслов слов каждой буквы слова
def calc_count_sub_words(word):
    '''
    входные данные
    :word — исходное слово

    выходные данные
    :count_sub_words - количество подслов которые подходят под условие задачи
    '''
    # Будем использовать префиксные ссумы для подсчета накопительного кол-ва символов
    # для подсчета символов будем использовать библиотеку Counter
    word_size = len(word)
    letters = [Counter()] * (word_size + 1)
    for i in range(1, word_size + 1):
        letters[i] = letters[i - 1] + Counter(word[i - 1])
    counter_letters = Counter()
    for i in range(word_size):
        for j in range(word_size, i - 1, -1):
            print(word[i:j])
            counter_letters += letters[j] - letters[i]
    for l in sorted(counter_letters.keys()):
        print(f"{l}: {counter_letters[l]}")


def main():
    # считываем входные данные
    word = load_data(INPUT_FILE)
    # Расчет кол-ва возможных подслов слов каждой буквы слова
    calc_count_sub_words(word)


if __name__ == "__main__":
    main()
