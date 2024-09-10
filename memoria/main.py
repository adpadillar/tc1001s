"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

# Define los posibles colores y formas posibles para los tiles
tile_shapes = ["triangle", "circle", "square", "star"]
tile_colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]

# Crea una lista de tiles con todas las combinaciones posibles de formas y colores
tiles = [(x, y) for x in tile_shapes for y in tile_colors] * 2
shuffle(tiles) # Mezcla los tiles para que no estén en orden

# Dibuja una estrella, dados inicio o fin y color
def draw_star(x, y, color):
    """Draw a star with the given color at (x, y)."""
    print("Drawing star at", x, y, "with color", color)
    up()
    goto(x, y + 30)
    down()
    fillcolor(color)
    begin_fill()
    for _ in range(5):
        forward(50)  # Reduced size to fit within the box
        right(144)
    end_fill()

# Dibuja un triángulo, dados inicio o fin y color
def draw_triangle(x, y, color):
    """Draw an equilateral triangle with the given color at (x, y)."""
    print("Drawing triangle at", x, y, "with color", color)
    up()
    goto(x, y)
    down()
    fillcolor(color)
    begin_fill()
    for _ in range(3):
        forward(50)
        left(120)
    end_fill()

# Dibuja un círculo, dados inicio o fin y color
def draw_circle(x, y, color):
    """Draw a circle with the given color at (x, y)."""
    print("Drawing circle at", x, y, "with color", color)
    up()
    goto(x + 25, y)
    down()
    fillcolor(color)
    begin_fill()
    circle(25)  # radius of 25 to match the size of other shapes
    end_fill()

# Dibuja un cuadrado, dados inicio o fin y color
def draw_square(x, y, color):
    """Draw a square with the given color at (x, y)."""
    print("Drawing square at", x, y, "with color", color)
    up()
    goto(x, y)
    down()
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()


car = path('car.gif')
state = {'mark': None, 'taps': 0}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)

        # Dibuja la forma en el tile dependiendo de la forma y color
        # generado inicialmente
        shape_name, shape_color = tiles[mark]
        if shape_name == 'circle':
            draw_circle(x, y, shape_color)
        elif shape_name == 'triangle':
            draw_triangle(x, y, shape_color)
        elif shape_name == 'square':
            draw_square(x, y, shape_color)
        elif shape_name == 'star':
            draw_star(x, y, shape_color)
    
    up()
    goto(-200, 200)

    # Escribe el número de taps en el tablero
    color('black')
    write(f"Taps: {state['taps']}", font=('Arial', 16, 'normal'))

    # Si el juego se ha ganado, muestra un mensaje con el número de taps
    if all(not h for h in hide):
        up()
        goto(0, 0)
        color('white')
        write(f"You won in {state['taps']} taps!", align='center', font=('Arial', 30, 'bold'))

    update()
    ontimer(draw, 100)


setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
