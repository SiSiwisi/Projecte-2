negatiu = False

for i in range(10):
    num = int(input("Introdueix un nombre: "))

    if num < 0:
        negatiu = True

if negatiu == True:
    print("Hi havia almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")