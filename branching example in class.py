def convert_celsius_temperature_to fahrenheit(celcius_temperature):
  """Convert input temperature in Celsius to Fahrenheit"""
  return (9./5)*celsius_temperature + 32

def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
  """Convert input temperature in Fahrenheit to Celsius"""
  return (5./9)*(fahrenheit_temperature - 32)"

if __name__== "__main__":
  print(convert_celcius_temperature_to_fahrenheit(0))
  print(convert_fahrenheit_temperature_to_celsius(32))
  