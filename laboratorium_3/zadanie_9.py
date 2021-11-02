balance = 1000
pin = input("Ustaw swój 4 cyfrowy pin: ")

while len(pin) != 4:
    print("PIN nie jest 4 cyfrowy, proszę podać jeszcze raz")
    pin = input("Ustaw swój 4 cyfrowy pin: ")

pin = int(pin)

def check_pin():
    security = int(input("Wprowadź swój PIN: "))
    while security != pin:
        print("Zły numer pin")
        security = int(input("Wprowadź swój PIN: "))

while True:
    print("Witamy w Bankomacie/Wpłatomacie!")
    print("1. Wpłata \n2. Wypłata \n3. Sprawdź saldo" )

    operation = int(input("Co Chcesz zrobić (1,2,3)? "))

    if operation == 1:
        check_pin()
        deposit = int(input("Ile chcesz wpłacić: "))
        balance += deposit
    elif operation == 2:
        check_pin()
        withdraw = int(input("Ile chcesz wypłacić: "))
        if withdraw > balance:
            print("Nie masz tyle na koncie!!")
        else:
            balance -= withdraw
    elif operation == 3:
        check_pin()
        print(balance)

    what_to_do = int(input("Co chcesz zrobić w kolejnym kroku \n1. Rozpocząć od nowa \n2. Zakończyć program \n >"))
    if what_to_do == 2:
        break

