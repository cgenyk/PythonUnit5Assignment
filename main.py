import simpleguitk as simplegui
#commit
x = 50
y = 200


def draw_handler(canvas):
    global x
    global y
    color = "RGB(15, 150, 150)"
    x = x + 20

    if (x >= 1000):
        x = 50

    canvas.draw_circle((x, y), 50, 1, color, color)
    canvas.draw_circle((550, 120), 20, 12, 'Green')  # Green Boi
    canvas.draw_circle([432, 220], 30, 12, 'Red')  # Red Boi
    canvas.draw_circle((342, 320), 20, 5, 'Blue', 'White')  # Blue White Boi
    canvas.draw_circle([120, 80], 30, 10, 'Yellow', 'Orange')
    # TODO Add 3 more polygons
    canvas.draw_polygon([[150, 180], [160, 190], [40, 20], [10, 10]], 12, 'Red', 'Red')
    canvas.draw_polygon([(90, 100), (80, 40), (30, 90)], 5, 'Blue', 'White')
    # Todo add 3 more lines
    canvas.draw_line([500, 70], [610, 70], 5, 'Blue')
    frame.set_canvas_background('Black')


for x in (0, 100):
    for y in (0, 100):
        print("The program is running and the values in x or y were betwwen 0-100")
frame = simplegui.create_frame("Go", 1000, 400)
frame.set_draw_handler(draw_handler)
frame.start()

