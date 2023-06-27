""" Drive and Reverse.

This program will instruct the Ring:bit car to move forwards, reverse and brake
as a result of physically pressing the A, B and A+B buttons found on the front
of the Micro:bit controller.
"""

__author__ = "Kendall Flanagan"
__license__ = "MIT"


# Initialise the wheels
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

# Define a function that provides instructions to perform when the A button is pressed
def on_button_pressed_a():
    RingbitCar.forward()

# Define a function that provides instructions to perform when the B button is pressed
def on_button_pressed_b():
    RingbitCar.back()

# Define a function that provides instructions to perform when the A+B buttons are pressed
def on_button_pressed_ab():
    RingbitCar.brake()

# Bind the functions to the relevant input event handlers
# Reference: https://makecode.microbit.org/reference/input/on-button-pressed
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
