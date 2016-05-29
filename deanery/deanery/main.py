from deanery_worker import *


def info():
    print ("Symulator dziekanatu W4")
    print ("Autor: Wojciech Słowiński\n")
    print ("Menu:")
    print ("\t1. Przeprowadź symulację dla losowych 10 pracowników")
    print ("\t2. Stwórz pracowników")
    print ("\t3. Wyjdź")

def main():
    info()
    choice = input("\nCo chcesz zrobić?: ")
    if choice=="1":
        symulate()
    elif choice=="2":
        create()
    elif choice=="3":
        quit()
    else:
        print("\nNie ma takiej opcji!")
        main()
    






if __name__ == "__main__":
    info()
    main()
