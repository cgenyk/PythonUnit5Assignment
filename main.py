import simpleguitk as simplegui
import random


# Timers
# Blinking Text


# This program is similar to the example "screensaver" shown
#	in the video. In this program, the user's text blinks
#	every time the timer handler is called. Try changing
#	the timer frequency to see what happens. Notice that if
#	the text is too long not all of it will be shown. For an
#	added challenge, can you come up with a way to solve
#	that issue?
## todo when will this update

# Global Variables

canvas_width = 800
canvas_height = 400
message = "No Input"
displayed = True
timer_interval = 1000  # In milliseconds (1000 ms = 1 s)


# Event Handlers

def input_handler(text):
    global message
    message = text


# Switches whether or not the text is visible
# Note that it does not have any parameters
def timer_handler():
    global displayed
    displayed = not displayed


def draw(canvas):
    if displayed:
        canvas.draw_circle((10, 50), 20, 12, 'Green')
        canvas.draw_circle([20, 30], 30, 12, 'Red')
        canvas.draw_circle((54, 55), 20, 5, 'Blue', 'White')
        canvas.draw_circle([70, 80], 30, 10, 'Yellow', 'Orange')
        canvas.draw_polygon([[30, 20], [40, 40], [50, 20], [10, 10]], 12, 'Red')
        canvas.draw_polygon([(50, 70), (80, 40), (30, 90)], 5, 'Blue', 'White')
        canvas.draw_text(message, [500, 65], 30, "Aqua")
        canvas.draw_line([500, 70], [610, 70],5, 'Blue')



# Frame

frame = simplegui.create_frame("Blinking Text", canvas_width, canvas_height)

# Register Event Handlers

frame.set_draw_handler(draw)
frame.add_input("Your message:", input_handler, 100)

# Creates a timer. Check the docs for more details.
timer = simplegui.create_timer(timer_interval, timer_handler)

# Remember to start the timer as well as the frame
frame.start()
timer.start()

