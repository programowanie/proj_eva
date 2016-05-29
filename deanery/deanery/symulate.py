from deanery_worker import *
import matplotlib.pyplot as plt
import math, os
#Symulacja - losowa, bądź dla stworzonych pracowników
def symulate(list_of_workers=[],number_of_workers=100):
    #Tworzymy listę 100 pracowników z losowymi cechami
    #Dlaczego 100? W tej symulacji nie chodzi o wybieranie konkretnego okienka
    #lecz próba przewidzenia sytuacji, jaka nas tam spotka
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nParametry dla takiej symulacji to:")
    print("\tWiek: 25-65")
    print("\tPłeć: 3 razy więcej kobiet, niż mężczyzn")
    print("\tZarobki: 1500-3500")
    print("\tDzieci: 0-3\n")
    print("\tTrudne dni: Tak/Nie\n")
    print("\nOd razu powiedzieć trzeba, że symulacja dla danych losowych nie będzie najlepsza, gdyż")
    print("niestety świat nie jest idealny :(\n")
    
    workers=list_of_workers
    amount = number_of_workers
    if len(workers)==0:
        for i in range(amount):
            workers.append(DeaneryWorker(random))        
    #Zakładamy, że możemy podejść z dowolną sprawą, więc trzeba by ich było
    #jakoś uśrednić
    average_worker = DeaneryWorker() #"Uśredniony" pracownik
    average_age=0
    #Licznik mężczyzn/kobiet
    males=0
    females=0
    #Licznik pracowników z "tymi dniam" i bez nich
    those_days=0
    not_those_days=0
    average_earnings=0
    average_children=0
    for worker in workers:
        average_age+=worker.age
        #Zliczamy płcie
        if worker.sex=="Mężczyzna":
            males+=1
        else:
            females+=1

        #Zliczamy pracowników z "tymi dniami"    
        if worker.sex=="Kobieta":                
            if worker.days=="Niestety":
                those_days+=1
            else:
                not_those_days+=1
        average_earnings+=worker.earnings
        average_children+=worker.children
        
    average_worker.age=math.ceil(average_age/amount)
    average_worker.earnings=math.ceil(average_earnings/amount)
    average_worker.children=math.ceil(average_children/amount)
    #Szukamy najbardziej prawdopodobnej płci:
    if males>females:
        average_worker.sex="Mężczyzna"
    elif females>males:
        average_worker.sex="Kobieta"
    else:
        average_worker.sex="Kobieta"
    #I wystąpienia "tych dni"
    if those_days>not_those_days:
        average_worker.days="Niestety"
    elif those_days<not_those_days:
        average_worker.days="Nie"
    else:
        average_worker.days="Niestety"
        
    print("W dziekanacie najprawdopodobniej natrafisz na osobę o podanych cechach:\n")
    average_worker.print_features() #Tu już się dokonuje obliczenie wsp. dobroci
    
    #Co się o dziwo okazuje? Średnio pracownikiem jest ok. 45 letnia kobieta
    #Zarabiająca 2500 na rękę z dwójką dzieci. Nie mam danych co do zarobków
    #w dziekanacie, można tym trochę pomanipulować, ale efekt jest ciekawy

    #Czas na odchylenie standardowe:
    sum=0
    standard_deviation=None
    points=[]
    values=[]
    for worker in workers:
        sum+=(worker.getKindness()-average_worker.kindness)**2
        points.append(worker.kindness)
    standard_deviation=math.sqrt((1/(amount-1))*sum)
    #A tutaj krzywa gęstości prawdopodobieństwa (rozkład Gaussa):
    points=sorted(points)
    for point in points:
        a=standard_deviation*math.sqrt(2*math.pi)
        b=(point-average_worker.kindness)**2
        c=-2*(standard_deviation)**2
        values.append(1/a*math.pow(math.e,(b/c)))
    plt.plot(points, values)
    plt.title("Gestosc prawdopodobienstwa")
    plt.xlabel("Współczynnik dobroci")
    plt.show()
    #Mógłbym tutaj wyliczać prawdopodobieństwo wystąpienia dla danego przedziału
    #ale jest to funkcja dyskretna, nie ciągła. Co do całkowania funkcji dyskretnych
    #, to nawet słynny mgr. Pietraszko mówił, że jakby ktoś na kolokwium próbował
    #to zaprasza do C11 na specjalny egzamin, który umie napisać 100 osób w Polsce
    index = values.index(max(values))
    
    #Najbardziej prawdopodobny współczynnik dobroci:
    average_kindness=points[index]

    if average_kindness<=20.0:
        print("\n* No nikt Cię nie wyrzuci, ale spotkasz się z absolutnym brakiem sympatii")
        print("* Przysłowiowa Pani Jadzia będzie się na Ciebie patrzeć, jakbyś zabił jej dziecko")
        print("* Lub skasował jej ulubiony serial paradokumentalny z dekodera")
        print("* Będziesz obserwowany ze wszystkich stron, a każdy, choćby najmniejszy niewłaściwy ruch")
        print("spowoduje, że wezmą Cię za oszusta, złodzieja i pewnie jeszcze pijaka")
    if average_kindness>20.0 and average_kindness<=40.0:
        print("\n* Sytuacja nie jest najgorsza, lecz wciąż jesteś tylko studentem - debilem, znaczy się")
        print("* Każdy wie, że wczoraj upiłeś się do nieprzytomności, a w dodatku jesteś czcicielem szatana")
        print("* Chcesz podbić legitymację? Po czekaniu 40 minut w kolejce dowiesz się, że przyszedłeś za wcześnie/za późno")
        print("* A tak w ogóle, to czemu nie na galowo?")
    if average_kindness>40.0 and average_kindness<=60.0:
        print("\n* Coraz lepiej. Pracownikom nie przeszkadza już to, że nie znasz wszystkich procedur obowiązujących w ich gabinecie")
        print("* Co prawda mógłbyś przyjść w garniturze z bukietem róż i czekoladek dla Pani Krysi, no ale cóż, taka ta dzisiejsza młodzież")
        print("* Większość spraw uda Ci się załatwić, jeśli będziesz miły i we wszystkim zgodzisz się z Panią siedzącą po drugiej stronie biurka")
    if average_kindness>60.0:
        print("\n* Nie oszukujmy się, sytuacja jest praktycznie niemożliwa")
        print("* Pracownicy aż wzdychają do Ciebie, gdy przychodzisz z papierkiem o zmianę wydziału")
        print("* Podbijanie legitymacji to sama przyjemność, niemalże dostajesz pieczątki na cały stopień studiów")
        print("* Innymi słowy utopia - jak u Karola Marksa")
