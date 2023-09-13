"""
Disclaimer: Spaghetti code only written
for educational purposes.
Never do this at home.
"""

from conversions import km_to_miles
from conversions import cel_to_fahr
import destination_input
from output import print_destination_info

def handle_destination(
    from_destination, to_destination,
    distance_in_km,
    degrees_cel, weather):
    """
    Converts data for the destination and presents the result
    """
    miles_to_first_destination = km_to_miles(distance_in_km)
    degrees_fahrenheit_at_first_destination = cel_to_fahr(degrees_cel)

    print_destination_info(from_destination, to_destination,
        miles_to_first_destination, degrees_fahrenheit_at_first_destination, weather)

def main():
    """
    Main function for the module spaghetty.py
    """
    handle_destination(
        destination_input.starting_point,
        destination_input.first_destination,
        destination_input.km_to_first_destination,
        destination_input.degrees_celsius_at_first_destination,
        destination_input.weather_at_first_destination
    )

    print()

    handle_destination(
        destination_input.first_destination,
        destination_input.second_destination,
        destination_input.km_to_second_destination,
        destination_input.degrees_celsius_at_second_destination,
        destination_input.weather_at_second_destination
    )

if __name__ == "__main__":
    main()
    