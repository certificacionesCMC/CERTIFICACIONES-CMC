notas =  []
for i in(1, 5):
    
    nota = float (input("ingrese la nota {i}: "))
    notas.append (nota)
    
promedio = sum(notas) / len(notas)

print(f"El promedio de las notas en ingles es: {promedio: .5f}")
        