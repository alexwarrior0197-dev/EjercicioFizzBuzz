numero = 1
while numero <= 1000:
    if numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")   
    else:
        print(numero)   
    numero += 1