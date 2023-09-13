"""
Module for printing out information for the module spaghetty.py
"""

def print_route(from_destination, to_destination):
    """
    Prints from and to destination
    """
    print("Going from " +
        from_destination +
        " to " +
        to_destination
    )

def print_distance(miles_to_destination, destination):
    """
    Prints distance in miles to destination
    """
    print(str(miles_to_destination) +
        " miles to " +
        destination
    )

def print_weather_at_destination(degrees, weather, destination):
    """
    Prints the temperature in Fahrenheit and weather at the destination
    """
    print(str(degrees) +
        " degrees and " +
        weather +
        " in " +
        destination
    )

def print_destination_info(
    from_destination, to_destination,
    miles_to_destination,
    degrees, weather):
    """
    Prints destination information
    """
    print_route(from_destination, to_destination)
    print_distance(miles_to_destination, to_destination)
    print_weather_at_destination(degrees, weather, to_destination)


if __name__ == "__main__":
    print_route("Karlskrona", "Osby")
    print_distance("84.5", "Osby")
    print_weather_at_destination("55.4", "Raining", "Osby")
    print_destination_info("Karlskrona", "Osby", "84.5", "55.4", "Raining")
