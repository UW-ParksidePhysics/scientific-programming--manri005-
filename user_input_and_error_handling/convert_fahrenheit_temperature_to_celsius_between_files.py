def fahrenheit_to_celsius(temp_f):
  return (temp_f - 32) * (5 / 9)

file_path = 'user_input_and_error_handling/temperature.txt'

try:
  with open(file_path, 'r') as data_file:
      lines = data_file.readlines()

  third_line = lines[2].split()  # Split the third line into words
  temperature = float(third_line[2])  # Desired value is the third object in 'words', convert to float
except (IndexError, ValueError):
  print('Error: Temperature data is missing or not formatted correctly.')
else:
  temperature_celsius = fahrenheit_to_celsius(temperature)
  print(f'{temperature} degrees Fahrenheit is {temperature_celsius} degrees Celsius.')
