# https://contest.yandex.ru/contest/45468/problems/17/
# Дивизион B
# 17. Игра в пьяницу
import queue

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        cards_1_player = file.readline().split()
        cards_2_player = file.readline().split()
    return [int(c) for c in cards_1_player], [int(c) for c in cards_2_player]


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Подсчет игры в пьяницу
def calc_alco_game(cards_1_player, cards_2_player):
    '''
    входные данные
    :cards_1_player — команды управления стеком, по одной на строке
    :cards_2_player — команды управления стеком, по одной на строке

    выходные данные
    :result - результат выполнения команд
    '''
    q_player_1 = queue.Queue()
    q_player_2 = queue.Queue()
    for i in range(len(cards_1_player)):
        q_player_1.put(cards_1_player[i])
        q_player_2.put(cards_2_player[i])
    i = 0
    while not q_player_1.empty() and not q_player_2.empty():
        card_p1 = q_player_1.get()
        card_p2 = q_player_2.get()
        if (card_p1 == 0 and card_p2 == 9):
            win_player = 1
        elif (card_p2 == 0 and card_p1 == 9):
            win_player = 2
        elif card_p1 > card_p2:
            win_player = 1
        elif card_p2 > card_p1:
            win_player = 2
        else:
            assert False
        if win_player == 1:
           q_player_1.put(card_p1)
           q_player_1.put(card_p2)
        elif win_player == 2:
            q_player_2.put(card_p1)
            q_player_2.put(card_p2)
        elif win_player == 0:
            assert False
        i += 1
        if i >= 10**6:
            return "botva"
    if q_player_2.empty():
        return f"first {i}"
    else:
        return f"second {i}"


def main():
    # считываем входные данные
    cards_1_player, cards_2_player = load_data(INPUT_FILE)
    # Подсчет игры в пьяницу
    game_score = calc_alco_game(cards_1_player, cards_2_player)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, game_score)


if __name__ == "__main__":
    main()
