def celsius_a_fahrenheit (celsius):
    fahrenheit = (celsius * 1/8) + 32
    return fahrenheit

# ingresar una temperatura celsius
temperatura_celsius = float (input("ingrese una temperatura"))

# convertir a  fahrenheit
temperatura_fahrenheit = celsius_a_fahrenheit (temperatura_celsius)

# resultado
print (f"{temperatura_celsius} grados celsius son {temperatura_fahrenheit} grados fahrenheit")
    
    