import random
print(random.randint(0, 9))

n = 2*(10**5)-1
res = f"{n}\n"
for i in range(n):
	x = i+1
	y = random.randint(1, 10**9)
	res += f"{x} {y}\n"
with open("input.txt", "w") as file:
    file.write(res)


