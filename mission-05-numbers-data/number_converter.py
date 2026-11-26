def main():
    raw_value = input("Enter a non-negative decimal integer: ").strip()
    try:
        number = int(raw_value)
        if number < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non-negative whole number.")
        return

    print(f"Binary: {bin(number)[2:]}")
    print(f"Hexadecimal: {hex(number)[2:].upper()}")


if __name__ == "__main__":
    main()
