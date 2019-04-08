# IMPORTANT:
# Please uncomment the correct import to run program
# - Thanks

# IMPORTS

# IMPORT FOR CODE SKULPTOR (UNCOMMENT LINE 9)
# import simplegui

# PYCHARM / OTHER USING TK (UNCOMMENT LINE 10)
# import simpleguitk as simplegui

# commit
x = 50
y = 200


def draw_handler(canvas):
    global x
    global y
    color = "RGB(15, 150, 150)"
    x = x + 20
    x2 = x + 20

    if (x >= 1000):
        x = 50
    y = 200
    ## Loading Dots
    canvas.draw_circle((x, y), 5, 1, color, color)
    canvas.draw_circle((x2, y), 5, 1, color, color)
    canvas.draw_circle((x2 + 20, y), 5, 1, color, color)
    canvas.draw_circle((x2 + 20, y), 5, 1, color, color)
    canvas.draw_circle((x2 + 40, y), 5, 1, color, color)
    canvas.draw_circle((x2 + 60, y), 5, 1, color, color)
    canvas.draw_circle((x2 + 80, y), 5, 1, color, color)

    # polygons
    canvas.draw_polygon([[0, 0], [1000, 0], [1000, 400], [0, 400]], 12, 'Black')
    canvas.draw_polygon([[5, 30], [1000, 30], [1000, 30], [5, 30]], 5, 'Black')
    canvas.draw_polygon([[300, 10], [700, 10], [700, 25], [300, 25]], .9, 'grey')
    canvas.draw_polygon([[8, 360], [1000, 360], [8, 360], [1000, 360]], .9, 'Blue')
    canvas.draw_polygon([[890, 10], [950, 10], [950, 25], [890, 25]], .9, 'grey')

    # Lines
    canvas.draw_line([420, 175], [580, 175], 5, 'Black')
    canvas.draw_line([420, 21], [550, 21], .9, 'Green')
    canvas.draw_line([900, 21], [906, 21], .9, 'Red')
    canvas.draw_line([910, 21], [916, 21], .9, 'Black')
    canvas.draw_line([916, 21], [925, 21], .9, 'Green')
    # Add Text
    canvas.draw_text('Loading', (420, 160), 48, 'Black', 'serif')
    canvas.draw_text('https://example.com/examplesite', (420, 21), 10, 'Green', 'serif')
    canvas.draw_text('E', (900, 21), 10, 'Red')
    canvas.draw_text('M', (908, 21), 10, 'Black')
    canvas.draw_text('F', (918, 21), 10, 'Green')
    canvas.draw_text('By Connor Genyk', (10, 380), 10, 'Green')

    frame.set_canvas_background('White')


for x in (0, 100):
    for y in (0, 100):
        print("Howdy")
frame = simplegui.create_frame("Go", 1000, 400)
frame.set_draw_handler(draw_handler)
frame.start()
