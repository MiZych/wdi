from math import sqrt
#Program rozwiązujący równanie x^2 -2 = 0 metodą bisekcji

#Znalezienie wartości x = a takiej że że f(a) < 0 np: x = 1
x_a = 1
#Znalezienie wartości x = b takiej że że f(b) > 0 np: x = 2
x_b = 2
#Znalezenie wartości funkcji f((a+b)/2)

def function(x_a, x_b):
    stop_punkt = ((x_a + x_b) / 2)
    print("Punkt stopu to: ", stop_punkt)

    # Obliczenie wartosci funkcji dla punktu stopu. Postać funkcji: f(x) = x^2 - 2

    function_stop = (stop_punkt ** 2) - 2
#Dokładność to 0.000002
    if function_stop > 0 and (stop_punkt - sqrt(2) > 0.000002):
        print("Rozwiązanie znajduje się w przedziale (", x_a, ",", stop_punkt, ")")
        function(x_a, stop_punkt)
    elif function_stop < 0 and (stop_punkt - sqrt(2) < 0.000002):
        print("Rozwiązanie znajduje się w przedziale (", stop_punkt, ",", x_b, ")")
        function(stop_punkt, x_b)

function(x_a, x_b)