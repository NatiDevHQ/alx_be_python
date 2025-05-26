# multiplication_table.py

try:
    # Prompt user for input
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate multiplication table using a for loop
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

except ValueError:
    print("Please enter a valid integer.")
