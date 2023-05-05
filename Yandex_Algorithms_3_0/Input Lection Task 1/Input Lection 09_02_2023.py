# https://contest.yandex.ru/contest/46276/problems/B/
# Академия Яндекса Начальная Лекция 09.02.2023


PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    logs = []
    with open(filename, "r") as file:
        log_size = file.readline()
        for line in file:
            logs.append(line.split())
    return logs


# # Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет
def calc_task(logs):
    '''
    входные данные
    выходные данные
    '''
    rockets = {}
    rockets_total_time = {}
    for log in logs:
        rocket_id = int(log[3])
        if rocket_id not in rockets:
            rockets[rocket_id] = {}
        timestamp = int(log[2]) + int(log[1]) * 60 + int(log[0]) * 24 * 60
        rockets[rocket_id][timestamp] = log[4]
    result = []
    for rocket_id in sorted(rockets.keys()):
        sort_times = sorted(rockets[rocket_id].keys())
        total_time = 0
        start_time = -1
        for timestamp in sort_times:
            action = rockets[rocket_id][timestamp]
            if action == "A":
                start_time = timestamp
            elif action in ["C", "S"] and start_time != -1:
                total_time += timestamp - start_time

        rockets_total_time[rocket_id] = total_time
        result.append(total_time)
    return result


def main():
    # считываем входные данные
    logs = load_data(INPUT_FILE)
    # Расчет
    result = calc_task(logs)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, " ".join(map(str,result)))

if __name__ == "__main__":
    main()
