# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Fixed typo in variable name

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32  # Using corrected variable name

def main():
    """Main function handling user interaction"""
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get and validate unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit not in ('C', 'F'):
            print("Invalid unit. Please enter either 'C' or 'F'.")
            return
        
        # Convert and display
        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()