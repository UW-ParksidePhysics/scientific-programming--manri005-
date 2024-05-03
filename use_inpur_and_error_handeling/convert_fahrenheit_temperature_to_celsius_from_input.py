import numpy as np
import sys

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_fahrenheit_temperature_to_celsius_from_command_line.py <fahrenheit>")
        sys.exit(1)

    try:
        fahrenheit = float(sys.argv[1])
    except ValueError:
        print("Error: Please enter a valid number for Fahrenheit temperature.")
        sys.exit(1)

    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()
