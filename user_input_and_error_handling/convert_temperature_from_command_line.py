from sys import argv, exit

def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * (5 / 9)

try:
    fahrenheit_temp = float(argv[1])
except IndexError:
    print('Error: No temperature provided. Please provide a valid temperature '
          'in Fahrenheit as a command-line argument.')
    exit(1)
except ValueError:
    print('Error: Invalid temperature provided. '
      'Please provide a valid temperature in Fahrenheit '
      'as a command-line argument.')
    exit(1)

celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)

print(f'{fahrenheit_temp}°F is equal to {celsius_temp}°C.')
