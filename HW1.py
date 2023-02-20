n = int(input('Сколько всего монет? '))
resh = 0
orel = 0
for i in range(n):
    x = int(input())
    if x == 0:
        resh += 1
    else:
        orel += 1
if orel > resh:
    print(resh)
else:
    print(orel)
