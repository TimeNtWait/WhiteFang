# https://contest.yandex.ru/contest/45469/problems/24/
# Дивизион А
# 24. Буратино
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    dinner_end = (14 - 9) * 60 * 60
    with open(filename, "r") as file:
        n = int(file.readline())
        events = []
        for _ in range(n):
            start_time, length = file.readline().split()
            start_time = start_time.strip().split(":")
            timestamp = (int(start_time[0]) - 9) * 60 * 60 + int(start_time[1]) * 60 + int(start_time[2])
            # Если после обеда пришел то дейсвтует мотивация по последней программе, т..е по сути событие после обеда
            # равно по вермени как 14 а по продолжительности как первая программ до этого
            if len(events) > 0 and (events[-1][0] < dinner_end < timestamp):
                events.append([dinner_end, events[-1][1]])
                n+=1
            events.append([timestamp, int(length.strip())])
    return n, events


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет ммаксимального количества гвоздиков
def calc_max_nails(n, events):
    '''
    входные данные
    :n — кол-во передач
    :events — передачи, отсортированные по времени начала с указанием продолжительности

    выходные данные
    :last_count - максимальное количество гвоздиков
    '''
    max_time  = 32400
    dp = [0] * (max_time + 1)
    events.append([max_time,10])
    full_events = [None] * (max_time + 1)
    for event in events:
        full_events[event[0]] = event
    last_length = full_events[0][1]
    for i in range(max_time):
        if full_events[i]:
            last_length = full_events[i][1]
        else:
            full_events[i] = [i, last_length]

    end_work_day = (18 - 9) * 60 * 60
    dinner_start = (13 - 9) * 60 * 60
    dinner_end = (14 - 9) * 60 * 60

    last_count = 0
    for event_id in range(0, len(full_events)):
        i, length = full_events[event_id]
        last_count = max(last_count, dp[i])
        if dinner_start <= i < dinner_end or (i < dinner_start and  i + length > dinner_start):
             continue

        if i + length > max_time :
            continue
        if i + length <= end_work_day and (i + length <= dinner_start or i + length > dinner_end):
            dp[i + length] = max(dp[i + length], last_count + 1)
            if i + length < end_work_day and i + length < full_events[event_id + 1][0]:
                last_count = max(last_count, dp[i + length])
        j = i + length
        j_length = length + 0
        while j + j_length < max_time and j + j_length <= full_events[event_id + 1][0]:
            if j < dinner_start and j + j_length >= dinner_end:
                break
            if (j + j_length <= dinner_start or j + j_length > dinner_end):
                dp[j + j_length] = max(dp[j + j_length], dp[j] + 1)
                last_count = max(last_count, dp[j + j_length])
            j += j_length
    return last_count


def main():
    # считываем входные данные
    n, events = load_data(INPUT_FILE)
    # Расчет ммаксимального количества гвоздиков
    max_nails = calc_max_nails(n, events)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(max_nails))


if __name__ == "__main__":
    main()
