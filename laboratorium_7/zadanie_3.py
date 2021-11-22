try:
    x, y, z = map(int, input("Podaj 3 cyfry: ").split())
    lista_x = []
    lista_y = []
    lista_z = []
    def list_maker(x, lista_unknown):
        string_x = str(x)
        i = 0
        while i < len(string_x):
            lista_unknown.append(int(string_x[i]))
            i += 1
        lista_unknown.sort()
    list_maker(x, lista_x)
    list_maker(y, lista_y)
    list_maker(z, lista_z)

    lista_x = list(dict.fromkeys(lista_x))
    lista_y = list(dict.fromkeys(lista_y))
    lista_z = list(dict.fromkeys(lista_z))

    if lista_x == lista_z == lista_y:
        print("Te liczby składają się z tych samych cyfr")
    else:
        def generator(lista_unknown):
            i = 1
            while i < 4:
                if i % 2 == 0:
                    print(i * str(lista_unknown[0]), end=" | ")
                elif i % 2 != 2 and len(lista_unknown) > 1:
                    print(i * str(lista_unknown[1]), end=" | ")
                else:
                    print(i * str(lista_unknown[0]), end=" | ")
                i += 1
        generator(lista_x)
        generator(lista_y)
        generator(lista_z)

except ValueError:
    print("Podaj liczby całkowite")