import matplotlib.pyplot as plt

def parse_viscosity_data(filename):
    viscosity_data = {}
    with open(filename, 'r') as file:
        for line in file:
            # Skip comment lines and empty lines
            if line.startswith('#') or not line.strip():
                continue

            # Skip header lines
            if line.startswith('gas'):
                continue

            # Split the line by commas
            parts = line.strip().split(',')

            # Ensure the line contains the expected number of values
            if len(parts) == 4:
                name, C, T0, mu0 = parts
                viscosity_data[name.strip()] = {'C': float(C), 'T0': float(T0), 'mu0': float(mu0)}
            else:
                print(f"Warning: Skipping line '{line.strip()}' as it doesn't contain the expected number of values.")
    return viscosity_data


def calculate_viscosity(temperature, gas, viscosity_data):
    C = viscosity_data[gas]['C']
    T0 = viscosity_data[gas]['T0']
    mu0 = viscosity_data[gas]['mu0']
    viscosity = mu0 * (temperature / T0) ** C
    return viscosity


def plot_viscosity(gases, temperature, viscosity_data):
    temperatures = [temperature] * len(gases)
    viscosities = [calculate_viscosity(temperature, gas, viscosity_data) for gas in gases]

    plt.figure(figsize=(10, 6))
    plt.bar(gases, viscosities, color=['blue', 'green', 'red'])
    plt.xlabel('Gas')
    plt.ylabel('Viscosity (μ)')
    plt.title(f'Viscosity at {temperature} K')
    plt.show()


# Parse viscosity data from file
viscosity_data = parse_viscosity_data('viscosity_of_gases.dat')

# Plot viscosity for air, carbon dioxide, and hydrogen at 300 K
plot_viscosity(['air', 'carbon dioxide', 'hydrogen'], 300, viscosity_data)
