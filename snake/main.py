from turtle import *
from random import randrange, choice, sample
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
speed = 100  # Velocidad inicial (menor es mas rapido)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside_food(food):
    "Return True if head inside boundaries."
    return -200 < food.get("x") < 190 and -200 < food.get("y") < 190

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Colores para el snake y la comida, se calculan de manera aleatoria
# cada vez que se inicia el juego
colors = ["blue", "orange", "purple", "pink", "yellow"]
snakeColor, foodColor = sample(colors, 2)

def move():
    "Move snake forward one segment."
    global speed
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        speed = max(50, speed - 2) # al comer, la velocidad se aumenta (menor es mas rapido)
    else:
        newFood = {"x": -1000, "y": -1000}
        # mover la comida a una nueva posición aleatoria
        # a un espacio adyacente
        while not inside_food(newFood):
            newFoodX = food.x + choice([-1, 0, 1]) * 10
            newFoodY = food.y + choice([-1, 0, 1]) * 10
            newFood = {"x": newFoodX, "y": newFoodY}
        food.x = newFood.get("x")
        food.y = newFood.get("y")
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    update()
    ontimer(move, speed) # se llama a la función move cada speed milisegundos

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
