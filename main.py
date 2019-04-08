import simpleguitk as simplegui

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

    # TODO Add 4 more polygons
    canvas.draw_polygon([[0, 0], [1000, 0], [1000, 400], [0, 400]], 12, 'Black')

    # Todo add 4 more lines
    canvas.draw_line([420, 175], [580, 175], 5, 'Black')

    # Add Text
    canvas.draw_text('Loading', (420, 160), 48, 'Black', 'serif')

    frame.set_canvas_background('White')


for x in (0, 100):
    for y in (0, 100):
        print("The program is running and the values in x or y were betwwen 0-100")
frame = simplegui.create_frame("Go", 1000, 400)
frame.set_draw_handler(draw_handler)
frame.start()
