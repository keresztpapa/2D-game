class Person():
    def __init__(self,nev,kor):
        self.nev = nev
        self.kor = kor

    def getAge(self):
        return self.kor

    def beszol(self,age):
        print(age)

class Gyerek(Person):
    def __init__(self,nev,kor):
        super().__init__(nev,kor)
        self.nev = nev



p = Person("béla", 35)

p.beszol(p.getAge())

c = Gyerek("béla_fia",10)

c.beszol(c.getAge())

print(c.nev)
