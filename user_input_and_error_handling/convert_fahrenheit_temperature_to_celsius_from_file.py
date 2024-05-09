def fahrenheit_to_celsius(temp_f):
  return (temp_f - 32) * (5 / 9)

with open('user_input_and_error_handling/fahrenheit_temperature.txt', 'r') as data_file:
  lines = data_file.readlines()

words = lines[2].split()  # Split the third line into 'words'

try:
  temperature = float(words[2])  # Desired value is the third object in 'words', convert to float
except (IndexError, ValueError):
  print('Error: Temperature data is missing or not formatted correctly.')
  exit(1)

temperature_celsius = fahrenheit_to_celsius(temperature)

print(f'{temperature} degrees Fahrenheit is {temperature_celsius} degrees Celsius.')
