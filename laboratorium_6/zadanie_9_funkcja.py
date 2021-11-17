number = int(input("Podaj liczbę: "))
divisor = int(input("Przez jaką liczbę chcesz dzielić: "))

def check_zero(number):
    check_number = str(number)
    if check_number.count("0") != 0 or len(set(check_number)) != len(check_number):
        return False
    return True


if check_zero(number) == True:
    divisors = []
    def obojetne(x):
        check_number = str(x)
        if len(check_number) >= 2:
            for i in range(0, 10):
                check_number_second = str(check_number.replace(str(i), ""))
                if int(check_number_second) % divisor == 0:
                    divisors.append(check_number_second)

    for i in range(0, 10):
        string_number = str(number)
        essa = string_number.replace(str(i), "")
        obojetne(essa)

    print(set(divisors))



else:
    print("Wprowadź liczbę która nie ma zera zera i jej cyfry się nie powtarzają")