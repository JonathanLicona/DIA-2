numero_1 = int(input("ingrse  el primer numero="))
numero_2 = int(input("ingrse  el segundo numero="))
numero_3 = int(input("ingrse  el tercer numero="))

if numero_1 != numero_2 and numero_1 != numero_3 and numero_2 != numero_3:
    if numero_1 < numero_2:
        if numero_1 < numero_3:
            print("el numero menor", numero_1)
        else:
            print("el numero menor", numero_3)
    else:
        if numero_2 < numero_3:
            print("el numero menor ", numero_2)
        else:
            print("el numero menor ", numero_3)
else:
    print("ingrese tres numeros diferentes")
