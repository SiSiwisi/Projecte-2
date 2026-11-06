nota = int(input("Introdueix una nota (-1 per acabar): "))
deu = False

while nota != -1:
    if nota == 10:
        deu = True

    nota = int(input("Introdueix una nota (-1 per acabar): "))

if deu == True:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")