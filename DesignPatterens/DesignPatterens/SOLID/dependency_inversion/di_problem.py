"""

Dependency Inversion Principle (DIP)
The Dependency Inversion Principle is one of the SOLID principles of object-oriented design. It states:

High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.


In simpler terms, this principle suggests that you should rely on abstractions (interfaces or abstract classes) rather than concrete implementations.
This allows for more flexible and maintainable code.
"""


class LightBulb:
    def turn_on(self):
        print("Lightbulb is turned on")

    def turn_off(self):
        print("Lightbulb is turned off")


class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def flip(self):
        # This method assumes the bulb has a turn_on and turn_off method
        if self.is_on:
            self.bulb.turn_off()
        else:
            self.bulb.turn_on()
        self.is_on = not self.is_on


# Usage
bulb = LightBulb()
switch = Switch(bulb)
switch.flip()  # Turns on the lightbulb
switch.flip()  # Turns off the lightbulb


"""
Issues with the Above Code
Tight Coupling: Switch directly depends on LightBulb. If you want to use a different type of light source, you have to modify the Switch class.
No Abstraction: The Switch class relies on the specific implementation of LightBulb.
"""