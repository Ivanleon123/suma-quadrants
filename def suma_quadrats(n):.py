def suma_quadrats(n):
    """Calcula la suma dels quadrats dels números separats per quatre posicions fins a n."""
    suma = 0
    for i in range(n, -1, -4):
        suma += i ** 2
    return suma

def main():
    # Demanar un número a l'usuari
    while True:
        numero = int(input("Introdueix un número menor de 100: "))
        if numero < 100:
            break
        else:
            print("Error: El número ha de ser menor de 100.")

    # Calcular la suma dels quadrats
    resultat = suma_quadrats(numero)

    # Mostrar el resultat
    print(f"La suma dels quadrats dels números separats per 4 posicions fins a {numero} és: {resultat}")

# Executar el programa
if __name__ == "__main__":
    main()