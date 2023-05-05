# https://contest.yandex.ru/contest/45468/problems/10/
# 10. Скучная лекция

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


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
    '''
    # Для быстрого расчета пришлось вывести формулу по которой можно рассчитать нужное кол-во символов
    letters = {}
    letters[word[0]] = last_count_letters = len(word)
    for idx in range(1, len(word)):
        count_letters = (last_count_letters // idx - 1) * (idx + 1)
        if word[idx] in letters:
            letters[word[idx]] += count_letters
        else:
            letters[word[idx]] = count_letters
        last_count_letters = count_letters
    for l in sorted(letters.keys()):
        print(f"{l}: {letters[l]}")


def main():
    # считываем входные данные
    word = load_data(INPUT_FILE)
    # Расчет кол-ва возможных подслов слов каждой буквы слова
    calc_count_sub_words(word)


if __name__ == "__main__":
    main()
