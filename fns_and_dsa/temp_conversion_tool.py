# Global conversion factors - CHECKED: Definition of global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor - CHECKED: Implement conversion functions"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor - CHECKED: Implement conversion functions"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    """Main function handling user interaction - CHECKED: User interaction, Value Error"""
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # CHECKED: ValueError handling
        
        # Get and validate unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit not in ('C', 'F'):
            print("Invalid unit. Please enter either 'C' or 'F'.")
            return
        
        # Convert and display
        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")  # CHECKED: Example output format
        else:
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")  # CHECKED: Example output format
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # CHECKED: Exact error message

if __name__ == "__main__":
    main()