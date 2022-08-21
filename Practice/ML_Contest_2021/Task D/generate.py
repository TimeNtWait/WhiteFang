import random

N = 100000
k = 100
res = f"{N} {k}\n"
for _ in range(N):
	a = random.randint(1,k*2)
	res += f"{a} "

with open("input_gen.txt", "w") as file:
	file.write(res)
