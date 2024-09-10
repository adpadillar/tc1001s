"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector
import math

# Dibuja una línea, dados inicio o fin
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Dibuja un cuadrado, dados inicio o fin
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


# Dibuja un círculo, dados inicio o fin
def draw_circle(start, end):
    # Calcula el radio del círculo usando el teorema de Pitágoras
    radius = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
    
    up()
    goto(start.x, start.y - radius)  # Move to the bottom of the circle
    down()
    begin_fill()
    circle(radius)  # Draw the circle
    end_fill()

# Dibuja un rectángulo, dados su ancho y alto
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(2):
        forward(40)
        left(90)
        forward(60)
        left(90)
    end_fill()


# Dibuja un triángulo, dados inicio o fin
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):  # Un triángulo tiene 3 lados
        forward(50)         # Cambia el tamaño si lo necesitas
        left(120)           # El ángulo entre los lados de un triángulo equilátero es 120 grados
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('orange'), 'O')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()


