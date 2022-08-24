PATH = ""
input_filename = PATH + "input.txt"
output_filename = PATH + "output.txt"


def load_input_data(input_filename):
    with open(input_filename, 'r') as file:
        # Считываем строки из входного файла
        rows = list(map(str.strip, file.readlines()))
        count_employees = int(rows[0])
        is_covid_employees = [int(n) for n in rows[1].split(" ")]
        meetings_by_employees = []
        for i in range(count_employees):
            employe_meetings = [int(n) for n in rows[i+2].split(" ")][1:]
            meetings_by_employees.append(employe_meetings)
    return is_covid_employees, meetings_by_employees


def main():
    # Загружаем входные данные
    is_covid_employees, meetings_by_employees = load_input_data(input_filename)

    # Формируем словарь для учета встреч
    meetings_dict = {}
    for empl_index in range(len(is_covid_employees)):
        meetings = meetings_by_employees[empl_index]
        for meet in meetings:
            if meet in meetings_dict:
                meetings_dict[meet] += [empl_index]
            else:
                meetings_dict[meet] = [empl_index]
    # Определяем новый список зараженных (туда входят те кто уже заражен)
    new_is_covid_employees = is_covid_employees.copy()
    # Проход ведется по пордковым номерам встреч
    for num_meet in sorted(list(set(meetings_dict))):
        # определяем был ли кто на встрече с ковидом
        meeting_is_covid = False
        for empl_index in meetings_dict[num_meet]:
            if (new_is_covid_employees[empl_index] == 1):
                meeting_is_covid = True
                break
        # если встреча ковидная, то все её участники заражены
        if meeting_is_covid:
            for empl_index in meetings_dict[num_meet]:
                new_is_covid_employees[empl_index] = 1

    string_result_covid = " ".join(str(n) for n in new_is_covid_employees)
    # Записываем результат в output.txt
    with open(output_filename, "w") as file:
        file.write(string_result_covid)

if __name__ == '__main__':
    main()
