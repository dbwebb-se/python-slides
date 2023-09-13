"""
Module for converting units
"""

def km_to_miles(distance):
    """
    Returns a distance in miles converted from input in km
    """
    return distance * 0.621371

def cel_to_fahr(degrees):
    """
    Returns a temperature in Fahrenheit, converted from the input which is in Celsius
    """
    return degrees * (9/5) + 32

if __name__ == "__main__":
    print(km_to_miles(136))
    print(cel_to_fahr(13))
