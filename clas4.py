class Gullar:
    def __init__(self,nomi,hidi):
        self.nomi = nomi
        self.hidi = hidi
    def __str__(self):
        return f"{self.nomi},{self.hidi}"

    

class Atirgul(Gullar):
    def __init__(self,nomi,hidi,rangi):
        super(). __init__(nomi,hidi)
        self.rangi = rangi

    def chiqarish1(self):
        print(self.nomi,self.hidi,self.rangi)
    
    def chiqarish2(self):
        print(self.nomi,"men sevadigan",self.hidi,"yoqimli",self.rangi,"gul")


atirgul2 = Atirgul("atirgul","xushboy","qizil")
atirgul3 = Atirgul("oq atirgul","xushboy","oppoq")
atirgul4 = Atirgul("atirgul","yoqimli","sariq")

print(atirgul2.chiqarish1())
print(atirgul2.chiqarish2())

print(atirgul3.chiqarish1())
print(atirgul3.chiqarish2())

print(atirgul4.chiqarish1())
print(atirgul4.chiqarish2())


class Lola(Gullar):
    def __init__(self,nomi,hidi,turi):
      super(). __init__(nomi,hidi)
      self.turi = turi

    def chiqar1(self):
        print(self.nomi,self.hidi,self.turi)

    def chiqar2(self):
        print(self.nomi,"ajoyib",self.hidi,"xushboy",self.turi)


lola1 = Lola("lola","yoqimli","qizg\'aldoq")
lola2 = Lola("lola","xushbo\'y","oq lola")
lola3 = Lola("lola","xushbo\'y","turkiston lolasi")

print(lola1.chiqar1())
print(lola1.chiqar2())

print(lola2.chiqar1())
print(lola2.chiqar2())

print(lola3.chiqar1())
print(lola3.chiqar2())


class Kaktus(Gullar):
    def __init__(self,nomi,hidi,tanasi):
     
        super(). __init__(nomi,hidi)
        self.tanasi = tanasi

    def textcha1(self):
        print(self.nomi,self.hidi,self.tanasi)
    def textcha2(self):
        print(self.nomi,"eng yomon",self.hidi,"hidsiz",self.tanasi,"tikanli gul")


kaktus0 = Kaktus("kaktus","yoq","tikanli")
kaktus1 = Kaktus("kaktus","yoqimsiz","o\'tli")
kaktus2 = Kaktus("kaktus","hidsiz","daraxtsimon")

print(kaktus0.textcha1())
print(kaktus0.textcha2())

print(kaktus1.textcha1())
print(kaktus1.textcha2())

print(kaktus2.textcha1())
print(kaktus2.textcha2())
