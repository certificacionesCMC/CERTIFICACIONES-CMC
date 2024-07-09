def masa_corporal (kg):
    peso = float (input("ingrese un peso en kilogramos: "))
    estatura  = float (input("ingrese su estatura: "))
    m = float (input("ingrese su estatura en metros: "))
    imc  = peso(kg) / [estatura(m)]
    print(f"su masa corporal (imc) es {imc: .2f}")
    
