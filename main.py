n = int(input('Введитe число для Чисел Фибоначчи: '))
f1 = f2 = 1

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2)