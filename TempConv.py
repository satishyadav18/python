print("Temperaure Converter")
print("____________________")

choice = input("Choose conversion type (1 for Celcius to Fahrenheit, 2 for Farhenheit to Celcius): ")

if choice == '1':
    celcius = float(input("Enter temperature in celcius: "))
    fahrenheit = (celcius * 9/5) + 32 
    print(f"{celcius} Celcius is equal to {fahrenheit:.2f} Fahrenheit.")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fehrenheit: "))
    celcius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} Fahrenheit is equal to {celcius:.2f} Celcius.")
else:
    print("Invalid choice. Enter 1 0r 2.")

