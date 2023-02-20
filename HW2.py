X = int(input('Введите первое число: '))
Y = int(input('Введите второе число: '))
for i in range(X):
    for j in range(Y):
        if X == i + j and Y == i * j:
            print(i, j)