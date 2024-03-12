def generate_table(initial_velocity):
  g_cb = 14.12  # m/s^2
  g_cc = 12.94  # m/s^2

  times = []
  positions_cb = []
  positions_cc = []

  # Generate values for Gliese 667 Cb
  for i in range(10):
      t = i * 0.177
      y_cb = 0.5 * g_cb * t ** 2
      times.append(round(t, 3))
      positions_cb.append(round(y_cb, 3))

  # Generate values for Gliese 667 Cc
  for t in times:
      y_cc = 0.5 * g_cc * t ** 2
      positions_cc.append(round(y_cc, 3))

  print(f"For initial velocity of {initial_velocity:.2f} m/s:")
  print("-----------------------------------------------------")
  print("Gliese 667 Cb (g = 14.12 m/s^2)  Cc (g = 12.94 m/s^2)")
  print("-----------------------------------------------------")
  print("    t (s)         y (m)         t (s)         y (m)     ")
  print("    -----         -----         -----         -----     ")

  # Print out the table using zip to traverse the lists in parallel
  for t_cb, y_cb, t_cc, y_cc in zip(times, positions_cb, times, positions_cc):
      print(f"    {t_cb}         {y_cb}         {t_cc}         {y_cc}")

  print("-----------------------------------------------------")

def main():
  initial_velocity = 10.00
  generate_table(initial_velocity)

if __name__ == "__main__":
  main()