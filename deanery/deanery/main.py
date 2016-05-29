from symulate import *
from create import *


def info():
    #Początkowe informacje, menu
    print ("Symulator dziekanatu W4")
    print ("Autor: Wojciech Słowiński\n")
    print ("Menu:")
    print ("\t1. Przeprowadź symulację dla losowych pracowników")
    print ("\t2. Stwórz pracowników")
    print ("\t3. Wyjdź")

def main():
    #Czas na wybór użytkownika
    choice = input("\nCo chcesz zrobić?: ")
    if choice=="1":
        symulate()
        input()
    elif choice=="2":
        create()
        input()
    elif choice=="3":
        quit()
    else:
        print("\nNie ma takiej opcji!")
        main()
        
#W przeciwieństwie do C++, w Pythonie nic nie musi zaczynać się od main()
#Przy starcie programu to są jedyne komendy, które się wykonują (reszta to funkcje)
#Stąd wywołujemy to, co się dzieje na początku
if __name__ == "__main__":
    info()
    main()
