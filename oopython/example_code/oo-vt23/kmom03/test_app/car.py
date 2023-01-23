#!/usr/bin/env python3
"""
Contains the Car class.
"""

class Car():
    """ Car class that handles cars with model and price. """
    wheels = 4

    def __init__(self, model, price):
        """ Constuctor """
        self.model = model
        self.price = price

    def present_car(self):
        """ Returns a string presenting the car """
        return "This car is of model {m} and costs {p}$.".format(
            m=self.model, p=self.price)

    def to_json(self):
        """  Returns a dict all the data of a Car """
        return {
            "model": self.model,
            "price": self.price,
        }

    # factory method
    @classmethod
    def from_json(cls, json):
        """ Creates a new instance of the class Car. """
        return cls(json["model"], json["price"])
