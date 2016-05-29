#Tak będzie wyglądał nasz pracownik
import random

AGE_GAP = (25, 65)
SEX = ("Mężczyzna", "Kobieta")
EARNINGS_GAP = (1500.0, 3500.0)
CHILDREN = (0,1,2,3,4)


class DeaneryWorker:
    #Jeśli nie podamy żadnego parametru przy tworzeniu obiektu, to
    #będziemy sami musieli nadać mu cechy
    age=0
    sex=""
    earnings=0
    children=0
    def __init__(self, random=None):
        if random!=None:
            self.age=random.randrange(AGE_GAP[0],AGE_GAP[1])
            self.sex=random.choice(SEX)
            self.earnings=random.randrange(EARNINGS_GAP[0], EARNINGS_GAP[1])
            self.children=random.choice(CHILDREN)
        else:
            pass
    def print_features(self):
        print("Wiek: %d\nPłeć: %s\nZarobki: %d\nIlość dzieci: %d\n" %(self.age,self.sex,self.earnings,self.children))
    def features(self):
        return {"age":self.age,"sex":self.sex,"earnings":self.earnings,"children":self.children}
    
