def generate_coordinates_for_loop(a, b, num_intervals):
  interval_length = (b - a) / num_intervals
  coordinates = []
  for i in range(num_intervals + 1):
      x = a + i * interval_length
      coordinates.append(round(x, 2))
  return coordinates

def generate_coordinates_list_comprehension(a, b, num_intervals):
  interval_length = (b - a) / num_intervals
  return [round(a + i * interval_length, 2) for i in range(num_intervals + 1)]

def main():
  a = 1
  b = 2
  num_intervals = 20

  interval_length = (b - a) / num_intervals

  print(f"For x in [{a}, {b}] with {num_intervals} intervals, the interval length is h = {interval_length:.3f}, and")
  print("Using a for loop:")
  coordinates_for_loop = generate_coordinates_for_loop(a, b, num_intervals)
  print(f"x = {coordinates_for_loop}")

  print("Using list comprehension:")
  coordinates_list_comprehension = generate_coordinates_list_comprehension(a, b, num_intervals)
  print(f"x = {coordinates_list_comprehension}")

if __name__ == "__main__":
  main()