# https://contest.yandex.ru/contest/46304/problems/C/
# C. Доставка со склада
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

from collections import deque

import math


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        lost_times = []
        for _ in range(n):
            times = list(map(int, file.readline().split()))
            lost_times.append(times)
    return n, lost_times


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск ответа
def find_answer(n, lost_times):
    a = [0]*(n+1)
    b = [0]*(n+1)
    dp = [[(0,0)]*(n+1) for _ in range(n+1)]
    path_dp = [[((-1,-1),-1)]*(n+1) for _ in range(n+1)]
    for i, length in enumerate(lost_times):
        a[i+1], b[i+1] = length

    # for i in range(n+1):
    #     dp[i][0] = (a[i],0)
    #     dp[0][i] = (0,b[i])
    for i in range(1, n+1):
        dp[i][0] = (dp[i-1][0][0] + a[i],0)
        dp[0][i] = (0,dp[0][i-1][1] + b[i])


    print(a, b)
    for i in range(n+1):
        print(dp[i])
    # print()
    # for i in range(n+1):
    #     print(path_dp[i])
    for i in range(1,n+1):
        for j in range(1,n+1):
            i1 = dp[i-1][j-1]
            print(f"i1: {i1}")
            i1_a = (i1[0]+a[i],i1[1])
            i1_b = (i1[0], i1[1] + b[j])

            i2 = dp[i-1][j]
            print(f"i2: {i2}")
            i2_a = (i2[0]+a[i],i2[1])
            i2_b = (i2[0],i2[1] + b[j])


            i3 = dp[i][j-1]
            print(f"i3: {i3}")
            i3_a = (i3[0]+a[i],i3[1])
            i3_b = (i3[0],i3[1] + b[j])
            print(f"max(i1_a): {max(i1_a)}")
            print(f"max(i1_b): {max(i1_b)}")
            print(f"max(i2_a): {max(i2_a)}")
            print(f"max(i2_b): {max(i2_b)}")
            print(f"max(i3_a): {max(i3_a)}")
            print(f"max(i3_b): {max(i3_b)}")

            find_min = min(max(i1_a), max(i1_b), max(i2_a), max(i2_b), max(i3_a), max(i3_b))
            if max(i1_a) == find_min:
                dp[i][j] = i1_a
                path_dp[i][j] = ((i-1, j-1),1)
            elif max(i1_b) == find_min:
                dp[i][j] = i1_b
                path_dp[i][j] = ((i-1, j-1), 2)

            # if max(i2_a) == find_min:
            #     dp[i][j] = i2_a
            #     path_dp[i][j] = ((i-1, j), 1)
            # elif max(i2_b) == find_min:
            #     dp[i][j] = i2_b
            #     path_dp[i][j] = ((i-1, j), 2)
            # if max(i3_a) == find_min:
            #     dp[i][j] = i3_a
            #     path_dp[i][j] = ((i, j-1), 1)
            # elif max(i3_b) == find_min:
            #     dp[i][j] = i3_b
            #     path_dp[i][j] = ((i, j-1), 2)


            pass
    for i in range(n+1):
        print(dp[i])
    print()
    for i in range(n+1):
        print(path_dp[i])
    path = []
    step = path_dp[-1][-1]
    # path.append(step[1])
    print(f"step: {step}")
    while step[0] != (-1,-1):
        path.append(step[1])
        step = path_dp[step[0][0]][step[0][1]]
        print(f"step: {step}")
    print(path)
    path = path[:-1]
    path.reverse()

    print(path)
    return " ".join(map(str, path))


def main():
    # считываем входные данные
    n, lost_times = load_data(INPUT_FILE)
    # Поиск ответа
    answer = find_answer(n, lost_times)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(answer))


if __name__ == "__main__":
    main()
