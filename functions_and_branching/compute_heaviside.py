def compute_heaviside(position):
  if position < 0:
      return 0
  elif position >= 0:
      return 1

def test_heaviside():
  tests = [-10, -10 - 15, 0, 10 - 15, 10]
  for position in tests:
      result = compute_heaviside(position)
      print(f"H({position}) = {result}")

if __name__ == "__main__":
  test_heaviside()
