import random
print("------------------------------------------")
print("--------------ADIVINA-NÚMERO--------------")
print("------------------------------------------")

ale=random.randint(0,10000)
n=int(input("Digite un número entre 0 y 10000: "))
i = 0
if n>=0 and n<=10000:
    while n != ale:
        if n > ale:
            print("INCORRECTO: Intente con un número menor")
        else:
            print("INCORRECTO: Intente con un número mayor")

        n=int(input("Digite otro número entre 0 y 10000: "))
        i = i + 1
    print("El numero es: "+str(n))   
    print("Para adivinar el número realizó " + str(i) + " intentos")
else: 
    print("El número que escribió no cumplió las características del programa")