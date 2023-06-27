""" Follow the Light (light level detection).

This program will instruct the Ring:bit car to follow a light source by
performing light level detection using the light sensors natively integrated
with the LEDs on the front of the Micro:bit controller.
"""

__author__ = "Kendall Flanagan"
__license__ = "MIT"


# Initialise the wheels
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

# Perform custom instructions (indefinitely) - follow a light source
def on_forever():

    # Check the light level using a comparison operator.
    # If the light level is greater than 40 then move forwards otherwise brake.
    # Reference: https://makecode.microbit.org/reference/input/light-level
    if input.light_level() > 40:
        RingbitCar.forward()
    else:
        RingbitCar.brake()

# Run a given function body continuously in an event-based forever loop
# Reference: https://makecode.microbit.org/reference/basic/forever
basic.forever(on_forever)
