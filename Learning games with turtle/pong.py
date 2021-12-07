import turtle

gra = turtle.Screen()  #Stworzenie okna
gra.title("Gra Pong :)") #Tytul okna
gra.bgcolor("black") #Kolor tła
gra.setup(width=800, height=800) #Rozmiar okna w którym się otworzy
gra.tracer(0) #Zatrzymuje aktualizacje okna, czyli musimy my aktualizować okno manualnie, pozwala na szybsze działanie gry


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Prędkość animacji
paddle_a.shape("square") #Kształt
paddle_a.color("white") #Kolor
paddle_a.shapesize(stretch_len=1, stretch_wid=5) #Rozszerzenie kształtu
paddle_a.penup()
paddle_a.goto(-350, 0) #Pozycja

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Prędkość animacji
paddle_b.shape("square") #Kształt
paddle_b.color("white") #Kolor
paddle_b.shapesize(stretch_len=1, stretch_wid=5) #Rozszerzenie kształtu
paddle_b.penup()
paddle_b.goto(350, 0) #Pozycja

#Ball
ball = turtle.Turtle()
ball.speed(0) #Prędkość animacji
ball.shape("square") # Kształt
ball.color("white") #Kolor
ball.penup()
ball.goto(0, 0) #Pozycja

#Przesuwanie sie
def paddle_a_up():
    y = paddle_a.ycor()#Przypisanie obecnych wspolrzednych Y
    y += 20
    paddle_a.sety(y) #Przypisanie wspolrzednej Y do paddle_a

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

gra.listen() #Nasluchiwanie z klawiatury
gra.onkeypress(paddle_a_up, "w")
gra.onkeypress(paddle_a_down, "s")
gra.onkeypress(paddle_b_up, "Up")
gra.onkeypress(paddle_b_down, "Down")


gra.listen() #
#Pętla całej gry
while True:
    gra.update() #Aktualizacja ekranu
