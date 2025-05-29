#function for converting Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    user_input = input("Enter temperature in Celsius (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the temperature converter. Goodbye!")
        break

    if user_input.replace('.', '', 1).replace('-', '', 1).isdigit():
        temperature_celsius = float(user_input)
        temperature_fahrenheit = convert_celsius_to_fahrenheit(temperature_celsius)
        print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit}°F")
        if temperature_fahrenheit < 0:
            print("It's freezing cold!")
        elif temperature_fahrenheit <= 20:
            print("It's quite chilly.")
        else:
            print("It's warm.")
    else:
        print("Invalid input. Please enter a valid number for temperature in Celsius.")
