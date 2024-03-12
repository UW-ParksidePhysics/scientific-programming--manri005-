def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    print("°F\t\t°C")
    print("------------------")

    fahrenheit = 0
    while fahrenheit <= 100:
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}\t\t{celsius:.2f}")
        fahrenheit += 10

if __name__ == "__main__":
    main()