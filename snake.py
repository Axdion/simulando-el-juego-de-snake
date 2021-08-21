import turtle
import time
import random

#Variables
score = 0
high_score = 0
posponer = 0.1
#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer()


#Cabeza Serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Segmentos / Cuerpo
segmentos = []

#Texto/Puntuacion
texto = turtle.Turtle()
texto.speed(0)
texto.color("yellow")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0     High Score: 0", align = "center", font = ("Courier", 24, "normal"))

#Funciones

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def derecha():
    cabeza.direction = "right"

def izquierda():
    cabeza.direction = "left"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)

#Fin de partida
def fin_partida():
    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direction = "stop"
    #Limpiar Segmentos
    for segmento in segmentos:
        segmento.goto(500,500)
    segmentos.clear()

#Actualizar Puntuacion
def actualizar_puntuacion():
    texto.clear()
    texto.write("Score: {}     High Score: {}".format(score, high_score),
                align = "center", font = ("Courier", 24, "normal"))

#Teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(derecha,"Right")
wn.onkeypress(izquierda,"Left")


while True:

    wn.update()

    #Colision  Bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        fin_partida()
        score = 0
        actualizar_puntuacion()
    #Colision Cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            fin_partida()
            score = 0
            actualizar_puntuacion()



    #   Colision comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 10
        if score > high_score:
            high_score = score
        actualizar_puntuacion()




    #Mover Cuerpo
    #En un lapso de tiempo el trozo del cuerpo n, avanza a la posicion del trozo n
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)





    mov()
    time.sleep(0.1)
