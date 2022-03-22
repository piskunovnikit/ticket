kolvo = int(input("введите количество билетов "))
list = [int(input("введите возраст владельца билета ")) for i in range(kolvo)]

for i in range(kolvo):
    if list[i] <= 17:
        list[i] = 0
    elif list[i] >= 25:
        list[i] = 1390
    else:
        list[i] = 990
print(list)

cymma = sum(list)
print(cymma)
if kolvo > 3:
    procent = cymma * 0.1
    cymma = cymma - procent
print("сумма к оплате", cymma)