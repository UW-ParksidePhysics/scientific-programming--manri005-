def compute_lists():
    g_cb = 14.12  # m/s^2
    g_cc = 12.94  # m/s^2

    times = []
    positions_cb = []
    positions_cc = []

    for i in range(10):
        t = round(i * 0.177, 2)
        y_cb = round(0.5 * g_cb * t ** 2, 2)
        y_cc = round(0.5 * g_cc * t ** 2, 2)
        times.append(t)
        positions_cb.append(y_cb)
        positions_cc.append(y_cc)

    return [times, positions_cb, positions_cc]

# Write out a table with t and y values in two columns
def write_table(times_positions):
    print("t (s)  \ty_cb (m)  \ty_cc (m)")
    print("------ \t-------- \t--------")
    for row in zip(*times_positions):
        print("{:.2f} \t{:.2f} \t{:.2f}".format(*row))

def main():
    times_positions = compute_lists()
    write_table(times_positions)

if __name__ == "__main__":
    main()
