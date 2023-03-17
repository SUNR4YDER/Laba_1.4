def divide100(number):
    OCheck = 0
    ValCheck = 0

    if(str(number).isdigit() != 1):
        ValCheck += 1
    else:
        if(number == 0):
            OCheck += 1
    if(OCheck == 0 and ValCheck == 0):
        print("100 / ", number, " = ", 100//number, " ост. ", 100%number)
    elif(OCheck != 0):
        print("На ноль делить нельзя")
    else:
        print("Вы ввели не число")

#divide100("srgsrfg")
#divide100(0)
#divide100(50)
#divide100(3)