from symulate import *

def create():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Stwórz pracownika\n")
    print("Zakres cech:")
    print("\tWiek: 25-65")
    print("\tPłeć: Kobieta/Mężczyzna")
    print("\tZarobki: 1500-3500")
    print("\tDzieci: 0-3\n")
    print("\tTrudne dni: Tak/Nie\n")
    amount=int(input("Ilu pracowników chcesz stworzyć?"))
    if amount<=0:
        print("Podałeś złą ilość!")
        create()
    id = 1
    print("")
    workers=[]
    for i in range(amount):
        worker = DeaneryWorker()
        print("###Pracownik nr. %d###" % id)
        age=int(input("Podaj wiek: "))
        sex=input("Podaj płeć(K/M): ")
        earnings=float(input("Podaj zarobki: "))
        children=int(input("Podaj ilość dzieci: "))
        if sex.lower()=="k":
            days=input("Czy ma te dni?(T/N): ")
            if days.lower()=="t":
                days="Niestety"
            else:
                days="Nie"
            sex="Kobieta"
        else:
            days="Nie"
            sex="Mężczyzna"        
        worker.age=age
        worker.earnings=earnings
        worker.sex=sex
        worker.children=children
        worker.days=days
        workers.append(worker)
        id+=1
    symulate(workers,len(workers))
        
                
