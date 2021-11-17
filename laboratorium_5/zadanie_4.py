from math import sqrt
#Program rozwiązujący równanie x^2 -2 = 0 metodą bisekcji

#Znalezienie wartości x = a takiej że że f(a) < 0 np: x = 1
x_a = 1
#Znalezienie wartości x = b takiej że że f(b) > 0 np: x = 2
x_b = 2
#Znalezenie wartości funkcji f((a+b)/2)


stop_punkt = ((x_a + x_b) / 2)
print("Punkt stopu to: ", stop_punkt)

#Obliczenie wartosci funkcji dla punktu stopu. Postać funkcji: f(x) = x^2 - 2

function_stop = (stop_punkt ** 2) - 2

if function_stop > 0:
    print("Rozwiązanie znajduje się w przedziale (1, 1.5)")
else:
    print("Rozwiązanie znajduje się w przedziale (1.5, 2)")

stop_punkt_second = ((1+1.5)/2)
print("Punkt stopu to: ", stop_punkt_second)
function_stop_second = (stop_punkt_second ** 2) - 2

if function_stop_second > 0:
    print("Rozwiązanie znajduje się w przedziale (1, 1.25")
else:
    print("Rozwiązanie znajduje się w przedziale (1.25, 1.5)")

stop_punkt_third = ((1.25 + 1.5)/2)
print("Punkt stopu to: ", stop_punkt_third)
function_stop_third = (stop_punkt_third ** 2) - 2
if function_stop_third > 0:
    print("Rozwiązanie znajduje się w przedziale (1,", stop_punkt_third)
else:
    print("Rozwiązanie znajduje się w przedziale: (", stop_punkt_third, ", 1.5)")

stop_punkt_fourth = ((1.375 + 1.5)/2)
print("Punkt stopu to: ", stop_punkt_fourth)
function_stop_fourth = (stop_punkt_fourth ** 2) - 2
if function_stop_fourth > 0:
    print("Rozwiązanie znajduje się w przedziale (1.375,", stop_punkt_fourth, ")")
else:
    print("Rozwiązanie znajduje się w przedziale: (", stop_punkt_fourth, ", 1.5)")