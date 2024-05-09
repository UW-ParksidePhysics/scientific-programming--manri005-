"""
Demonstration of temperature conversion functions in the convert_temperature module.

Usage:
import convert_temperature

# Example usage
print(convert_temperature.celsius_to_fahrenheit(0))  # Should output 32.0
print(convert_temperature.fahrenheit_to_celsius(32))  # Should output 0.0
print(convert_temperature.celsius_to_kelvin(100))  # Should output 373.15
print(convert_temperature.kelvin_to_celsius(373.15))  # Should output 100.0
print(convert_temperature.fahrenheit_to_kelvin(32))  # Should output 273.15
print(convert_temperature.kelvin_to_fahrenheit(273.15))  # Should output 32.0

convert_temperature.test_conversion()  # Verify the implementation
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def test_conversion():
    celsius_input = 25.0
    fahrenheit_input = 77.0
    kelvin_input = 298.15

    assert abs(celsius_to_fahrenheit(fahrenheit_to_celsius(fahrenheit_input)) - fahrenheit_input) < 1e-6
    assert abs(kelvin_to_celsius(celsius_to_kelvin(celsius_input)) - celsius_input) < 1e-6
    assert abs(kelvin_to_fahrenheit(fahrenheit_to_kelvin(fahrenheit_input)) - fahrenheit_input) < 1e-6

if __name__ == "__main__":
    import sys

    def user_interface():
        if len(sys.argv) != 3:
            print("Usage: python convert_temperature.py <temperature> <scale>")
            print("Example: python convert_temperature.py 21.3 C")
            return

        temperature = float(sys.argv[1])
        scale = sys.argv[2].upper()

        if scale == 'C':
            celsius = temperature
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
        elif scale == 'F':
            fahrenheit = temperature
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = fahrenheit_to_kelvin(fahrenheit)
        elif scale == 'K':
            kelvin = temperature
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = kelvin_to_fahrenheit(kelvin)
        else:
            print("Invalid scale. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
            return

        print(f"{temperature} {scale} is {fahrenheit:.2f} F and {kelvin:.2f} K.")

    user_interface()
