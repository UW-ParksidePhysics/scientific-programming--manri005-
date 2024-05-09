from sys import (argv, exit)

def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * (5 / 9)

try:
    user_temp = float(argv[1])
except IndexError:
    print('Please input a temperature as a command-line argument.')  # Print message if no command-line argument is provided
    exit(1)  # Exit the program

temp_celsius = fahrenheit_to_celsius(user_temp)

print(f'{user_temp}°F equals {temp_celsius}°C.')  # Print the converted temperature

