import math

class Haromszog:
    def __init__(self, a, b, c):
        self.a = float (a)
        self.b = float (b)
        self.c = float (c)

    def Kerulet(self):
        return self.a + self.b + self.c
    
    def terulet(self):
        s = self.kerulet() / 2
        return(s * (s-self.a)* (s-self.b)*(c-self.c))**(1/2)
    def magassagA(self):
        return 2 * self.terulet() / self.a
    
    def magassagB(self):
        return 2 * self.terulet() / self.b
    
    def magassagC(self):
        return 2 * self.terulet() / self.c
    
    def Alfa(self):
        return math.degrees(math.acos((self.b**2 + self.c**2 - self.a2**2)/(2*self.b*2*self.c)))
    
     def Beta(self):
        return math.degrees(math.acos((self.a**2 + self.c**2 - self.b2**2)/(2*self.a*2*self.c)))
    
     def Gamma(self):
        return math.degrees(math.acos((self.a**2 + self.b**2 - self.c2**2)/(2*self.a*2*self.b)))
    

#0
print("háromszögek feldolgozása 'class' segitségével.")

#1
a = (input("a =").replace("," , "."))
b = (input("b =").replace("," , "."))
c = (input("c =").replace("," , "."))

har1 = Haromszog(a, b, c)
har2 = Haromszog(10, 20, 30)

adatsor = "10,5;12,6;13,4"
har3 = Haromszog(*(adatsor.replace(',', '.').split(';')))
#Először az adatsorba kijavitjuk a hibákat és részlekre osztjuk
#De ezek a részek a tupleba kerülnek vissza
#hogy a tuplet tovább bontjuk arra szólgál a * operátor


#3
print(f"K = {har1.Kerulet():.2f}")
print(f"K = {har2.Kerulet():.2f}")
print(f"K = {har3.Kerulet():.2f}")
print()
print(f"T = {har1.Terulet():.2f}")
print(f"ma = {har1.magassagA():.2f}")
print(f"mb = {har1.magassagB():.2f}")
print(f"mc = {har1.magassagc():.2f}")