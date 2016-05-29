#Tak będzie wyglądał nasz pracownik
import random

AGE_GAP = (25, 65)
#Dlaczego tak? 3-krotnie zwiększam szansę na to, że to będzie kobieta
#odwzorowywując tym samym świat rzeczywisty
SEX = ("Mężczyzna", "Kobieta", "Kobieta", "Kobieta")
EARNINGS_GAP = (1500.0, 3500.0)
CHILDREN = (0,1,2,3)
THOSE_DAYS = ("Nie", "Niestety")


class DeaneryWorker:
    #Jeśli nie podamy żadnego parametru przy tworzeniu obiektu, to
    #będziemy sami musieli nadać mu cechy
    age=0
    sex=""
    earnings=0
    children=0
    #Najważniejszy parametr. Odpowiada on za to, jak zostaniemy potraktowani
    #Przy wejściu jest on maksymalny, a potem wszystko zaczyna spadać
    kindness=100.0
    def __init__(self, random=None):
        if random!=None:
            self.age=random.randrange(AGE_GAP[0],AGE_GAP[1])
            self.sex=random.choice(SEX)
            self.earnings=random.randrange(EARNINGS_GAP[0], EARNINGS_GAP[1])
            self.children=random.choice(CHILDREN)
            if self.sex=="Kobieta":
                self.days=random.choice(THOSE_DAYS)
            else:
                self.days=THOSE_DAYS[0]
        else:
            pass
    def print_features(self):
        print("Wiek: %d\nPłeć: %s\nZarobki: %d\nIlość dzieci: %d\nTe dni?: %s\nWspółczynnik dobroci: %.2f\n" %(self.age,self.sex,self.earnings,self.children,self.days,self.getKindness()))
    def features(self):
        return {"age":self.age,"sex":self.sex,"earnings":self.earnings,"children":self.children,"kindness":self.getKindness(),"days":self.days}
    def getKindness(self):
        if self.age==0:
            return 100.0
        #Dla wieku
        if self.age<30:
            pass
        elif self.age>=30 and self.age<40:
            self.kindness-=15.0
        elif self.age>=40 and self.age<50:
            self.kindness-=20.0
        elif self.age>=50 and self.age<60:
            self.kindness-=25.0
        elif self.age>=60:
            self.kindness-=30.0
        #Płeć
        if self.sex=="Mężczyzna":
            self.kindness-=random.choice((0.0,2.5,5.0))
        elif self.sex=="Kobieta":
            self.kindness-=random.choice((0.0,5.0,10.0))
        #Zarobki
        if self.earnings<=1800:
            self.kindness-=30.0
        elif self.earnings>1800 and self.earnings<=2500:
            self.kindness-=15.0
        elif self.earnings>2500 and self.earnings<=3000:
            self.kindness-=5.0
        else:
            pass
        #Potomstwo
        if self.children==0:
            pass
        elif self.children==1:
            self.kindness-=5.0
        elif self.children==2:
            self.kindness-=15.0
        elif self.children==3:
            self.kindness-=25.0
        #Trudne dni
        if self.days=="Niestety":
            self.kindness-=random.choice((5.0,10.0))
        else:
            pass
        return self.kindness
        
