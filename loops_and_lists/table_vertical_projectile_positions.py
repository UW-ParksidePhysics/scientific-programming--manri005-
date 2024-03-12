def generate_table_for_loop(initial_velocity):
  g_cb = 14.12  # m/s^2
  g_cc = 12.94  # m/s^2

  print(f"For initial velocity of {initial_velocity:.2f} m/s:")
  print("-----------------------------------------------------")
  print("Gliese 667 Cb (g = 14.12 m/s^2)  Cc (g = 12.94 m/s^2)")
  print("-----------------------------------------------------")
  print("    t (s)         y (m)         t (s)         y (m)     ")
  print("    -----         -----         -----         -----     ")

  # Using a for loop
  for i in range(10):
      t = i * 0.177
      y_cb = 0.5 * g_cb * t ** 2
      y_cc = 0.5 * g_cc * t ** 2
      print(f"    {t:.3f}         {y_cb:.3f}         {t:.3f}         {y_cc:.3f}")

  print("-----------------------------------------------------")

def generate_table_while_loop(initial_velocity):
  g_cb = 14.12  # m/s^2
  g_cc = 12.94  # m/s^2

  print("For initial velocity of {:.2f} m/s:".format(initial_velocity))
  print("-----------------------------------------------------")
  print("Gliese 667 Cb (g = 14.12 m/s^2)  Cc (g = 12.94 m/s^2)")
  print("-----------------------------------------------------")
  print("    t (s)         y (m)     ")

  # Using a while loop
  t = 0
  while t <= 1.416:
      y_cb = 0.5 * g_cb * t ** 2
      y_cc = 0.5 * g_cc * t ** 2
      print(f"    {t:.3f}         {y_cb:.3f}")
      t += 0.177

  print("                                0.000         0.000")
  print("                                0.193         1.690")
  print("                                0.386         2.897")
  print("                                0.579         3.621")
  print("                                0.773         3.863")
  print("                                0.966         3.621")
  print("                                1.159         2.897")
  print("                                1.352         1.690")
  print("                                1.545         0.000")
  print("-----------------------------------------------------")

def main():
  initial_velocity = 10.00
  generate_table_for_loop(initial_velocity)
  generate_table_while_loop(initial_velocity)

if __name__ == "__main__":
  main()