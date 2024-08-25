from abc import ABC, abstractmethod


# Define an abstraction (interface)
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# Low-level module implementing the abstraction
class LightBulb(Switchable):
    def turn_on(self):
        print("Lightbulb is turned on")

    def turn_off(self):
        print("Lightbulb is turned off")


# High-level module depending on the abstraction
class Switch:
    def __init__(self, device: Switchable):
        self.device = device
        self.is_on = False

    def flip(self):
        if self.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()
        self.is_on = not self.is_on


# Usage
bulb = LightBulb()
switch = Switch(bulb)
switch.flip()  # Turns on the lightbulb
switch.flip()  # Turns off the lightbulb
