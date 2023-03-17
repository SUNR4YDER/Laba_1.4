ticket = (input())
lenT = len(ticket)

#print(lenT)
sum1 = 0
sum2 = 0

if(lenT % 2 == 0):
    str1 = ticket[:lenT // 2]
    str2 = ticket[lenT // 2:]
    str11 = list(str1)
    str22 = list(str2)
    lenT = lenT // 2
    for i in range (lenT):
        sum1 = sum1 + int(str11[i])
    for i in range (lenT):
        sum2 = sum2 + int(str22[i])
    if(sum1 == sum2):
        print("Билетик - счастливый")
    else:
        print("Билетик - не счастливый")
else:
    print("Нечетное количество цифр")
