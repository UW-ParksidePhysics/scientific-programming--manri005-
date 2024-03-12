def sum_integers(maximum_integer):
  total = 0
  for i in range(1, maximum_integer + 1):
      total += i
  return total

def main():
  maximum_integer = 100  # Define your maximum_integer here
  sum_for_loop = sum_integers(maximum_integer)
  sum_formula = maximum_integer * (maximum_integer + 1) // 2

  print(f"n = {maximum_integer}")
  print(f"sum(1, n) = {sum_for_loop}")
  print(f"n(n+1)/2 = {sum_formula}")

if __name__ == "__main__":
  main()