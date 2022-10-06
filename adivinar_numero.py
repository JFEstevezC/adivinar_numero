import random
print("------------------------------------------")
print("--------------ADIVINA-NÚMERO--------------")
print("------------------------------------------")

i = 0
ale=random.randint(0,10000)
n=int(input("Digite un número entre 0 y 10000: "))

if n >= 0 and n <= 10000:
    while n != ale:
        if n > ale:
            print("Incorrecto, el número es menor")
        else:
            print("Incorrecto, el número es mayor")

        n=int(input("Digite otro número entre 0 y 10000: "))
        i = i + 1
    print("El numero es: "+str(n))   
    print("Para adivinar el número realizó " + str(i) + " intentos")
else: 
    print("El número que escribió no cumplió las características del programa")