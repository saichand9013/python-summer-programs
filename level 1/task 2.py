#level1-T2
#Task: Temperature Conversion
#Create a Python program that convertstemperatures between Celsius and Fahrenheit.Prompt the user to enter a temperature value and the unit ofmeasurement, and then display theconverted temperature

value = float(input('Enter the temperature: ')) # Prompt the user for input
scale = input('Enter the temperature scale: ').upper()

if scale == 'C':   # Converting the temperature and print the converted result
    result = value * 1.8 + 32
    print(f'{value} C = {result} F')
elif scale == 'F':
    result = (value - 32) / 1.8
    print(f'{value} F = {result} C')
else:
    print('Invalid temperature scale')
