f = [1, 2]

for i in range(2, 100):
    f.append(f[i-1] + f[i-2])

sum = 0
for j in range(0, 32):
    if f[j] % 2 == 0:
        sum += f[j]

print(sum)
