PATH = ""
input_filename = PATH + "input.txt"
output_filename = PATH + "output.txt"

def load_input_data(input_filename):
    with open(input_filename, 'r') as file:
        # Считываем строки из входного файла
        rows = list(map(str.strip, file.readlines()))
        count_points = int(rows[0])
        points = []
        for i in range(count_points):
            points.append([int(n) for n in rows[i+1].split(" ")])
    return points

def main():
    # Загружаем входные данные
    points = load_input_data(input_filename)
    pre_point = [0,0]
    sum_length = 0
    # Соединяем все вершины 
    for point in points:
        # print(f"Pre Point: {pre_point}, Current point: {point}")
        sum_length += ((point[1]-pre_point[1])**2+(point[0]-pre_point[0])**2)**0.5
        pre_point = point
    # Ищем дополнительные вершины которые необходимо соединить по условию задачи
    len_points = len(points)
    for i in range(1,len_points - 1):
        height_pre = points[i-1][1]
        if points[i][1] < height_pre:
            min_height = points[i][1]
            for j in range(i+1, len_points):
                if points[j][1] >= height_pre:
                    sum_length += ((points[i-1][1]-points[j][1])**2+(points[i-1][0]-points[j][0])**2)**0.5
                    break
    with open(output_filename, "w") as file:
        file.write(f"{sum_length}")    

if __name__ == '__main__':
    main()
