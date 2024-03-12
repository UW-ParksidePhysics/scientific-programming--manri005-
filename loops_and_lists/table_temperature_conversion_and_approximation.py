def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

def approximate_celsius(fahrenheit):
  return (fahrenheit - 30) / 2

def main():
  print("°F\t°C\tApprox")
  fahrenheit = 0
  while fahrenheit <= 100:
      celsius = fahrenheit_to_celsius(fahrenheit)
      approx_celsius = approximate_celsius(fahrenheit)
      print(f"{fahrenheit}\t{celsius:.2f}\t{approx_celsius:.2f}")
      fahrenheit += 10

if __name__ == "__main__":
  main()