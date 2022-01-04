from random import randint

number = int(input("Podaj liczbę hetmanów: "))

def chess_board():
    dane = []
    for i in range(1, 101):
        for k in range(1, 101):
            pomoc = [i, k]
            dane.append(pomoc)
    return dane

dane = chess_board()


def set_hetmans(number):
    hetmans = []
    for i in range(number):
        verse = randint(1, 100)
        column = randint(1, 100)
        hetmans.append([verse, column])
    return hetmans

hetmans = set_hetmans(number)
print("Ustawienie hetmanów", hetmans)

def tower_move(hetmans, number):
    all_tower_movements = []
    for m in range(number):
        verse_coordinate = hetmans[m][0]
        column_coordinate = hetmans[m][1]
        for i in range(1, 101):
            all_tower_movements.append([i, column_coordinate])
        for k in range(1, 101):
            all_tower_movements.append([verse_coordinate, k])
        all_tower_movements.append([0, 0])
    return all_tower_movements

all_tower_movements = tower_move(hetmans, number)
#print(all_tower_movements)


def laufer_move(hetmans, number):
    all_laufer_movements = []
    for m in range(number):
        x_cor = hetmans[m][0]
        y_cor = hetmans[m][1]
        i = 1
        while (x_cor + i) <= 100 and (y_cor + i) <= 100:
            all_laufer_movements.append([x_cor + i, y_cor + i])
            i += 1
        i = 1
        while (x_cor - i) >= 1 and (y_cor + i) <= 100:
            all_laufer_movements.append([x_cor - i, y_cor + i])
            i += 1
        i = 1
        while (x_cor - i) >= 1 and (y_cor - i) >= 1:
            all_laufer_movements.append([x_cor - i, y_cor - i])
            i += 1
        i = 1
        while (x_cor + i) <= 100 and (y_cor - i) >= 1:
            all_laufer_movements.append([x_cor + i, y_cor - i])
            i += 1
        all_laufer_movements.append([0, 0])

    return all_laufer_movements

all_laufer_movements = laufer_move(hetmans, number)
#print(all_laufer_movements)


#Indeksy gdzie kolejne hetmany kończą swoje manewry
result_tower = []
result_laufer = [0, ]
pos_tower = 0
pos_laufer = 0


while True:
    try:
        pos_tower = all_tower_movements.index([0, 0], pos_tower)
        pos_laufer = all_laufer_movements.index([0, 0], pos_laufer)
    except ValueError:
        break
    result_tower.append(pos_tower)
    result_laufer.append(pos_laufer)
    pos_tower += 1
    pos_laufer += 1

#print(result_tower)
#print(result_laufer)



def tower_and_laufer_moves(all_tower_movements, all_laufer_movements, result_tower, result_laufer, number):
    for k in range(number):
        first_tower = result_tower[k]
        for i in range(result_laufer[k], result_laufer[k + 1]):
            all_tower_movements.insert(first_tower + result_laufer[k], all_laufer_movements[i])
    return all_tower_movements

all_movements = tower_and_laufer_moves(all_tower_movements, all_laufer_movements, result_tower, result_laufer, number)
#print(all_movements)


def check_if_any_hitting(all_movements, hetmans, result_tower, result_laufer, number):
    for i in range(number):
        for k in range(i+1, number):
            previous_zero = result_tower[k - 1] + result_laufer[k]
            next_zero = result_tower[k] + result_laufer[k+1]
            for m in range(previous_zero, next_zero):
                if hetmans[i] == all_movements[m]:
                    print(hetmans[i], "Szachuje", hetmans[k])
                    print(hetmans[k], "Szachuje", hetmans[i])
            print(hetmans[i], "nie szachuje", hetmans[k])
            print(hetmans[k], "nie szachuje", hetmans[i])


check_if_any_hitting(all_movements, hetmans, result_tower, result_laufer, number)



def print_all(k, j):
    lista_gdzie_co_jest = []
    for args in dane[j:k]:
        for hetmans_sets in hetmans:
            if hetmans_sets == args:
                lista_gdzie_co_jest.append("|H|")
        lista_gdzie_co_jest.append("| |")
    if lista_gdzie_co_jest.count("|H|") != 0:
        lista_gdzie_co_jest.pop(-1)
    return lista_gdzie_co_jest


try:
    k = 10000
    j = 9900
    lista_gdzie_co_jest = []
    for i in range(100):
        lista_gdzie_co_jest.append(print_all(k, j))
        k -= 100
        j -= 100

    with open("output.txt", "w") as f:
        for k in range(100):
            print(lista_gdzie_co_jest[k], file=f)
except IndexError:
    pass




