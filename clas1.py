


class Hayvon:
    def __init__(self,nomi,laqabi):
        self.nomi = nomi
        self.laqabi = laqabi
    def __str__(self):
        return f"{self.nomi},{self.laqabi}"
   


class Mushuk(Hayvon):
    def __init__(self,nomi,laqabi,rangi):
        super(). __init__(nomi,laqabi)
        self.rangi = rangi
    def chiqarish0(self):
        print(self.nomi,self.laqabi,self.rangi)

    def chiqarish1(self):
        print("uy hayvoni",self.nomi,self.laqabi,"yoqimli",self.rangi)

mushuk1 = Mushuk("farishtacha","momiqvoy","oq")
mushuk2 = Mushuk("yoqimtoy","yuvosh","sariq")
mushuk3 = Mushuk("mallavoy","domboqvoy","qora")

print(mushuk1.chiqarish0())
print(mushuk1.chiqarish1())

print(mushuk2.chiqarish0())
print(mushuk2.chiqarish1())

print(mushuk3.chiqarish0())
print(mushuk3.chiqarish1())





class It(Hayvon):
    def __init__(self,nomi,laqabi,ovozi):

        super(). __init__(nomi,laqabi)
        self.ovozi = ovozi

    def chiqarish2(self):
        print(self.nomi,self.laqabi,self.ovozi)

    def chiqarish3(self):
        print("sevimli multik qahramonim",self.nomi,self.laqabi,self.ovozi)

it1 = It("simba","laycha","yoqimtoy")
it2 = It("qoplon","qoravoy","jahldor")
it3 = It("olapar","mittivoy","shirincha")

print(it1.chiqarish2())
print(it1.chiqarish3())


print(it2.chiqarish2())
print(it2.chiqarish3())

print(it3.chiqarish2())
print(it3.chiqarish3())

class Ot(Hayvon):
    def __init__(self,nomi,laqabi,turi):
        super(). __init__(nomi,laqabi)
        self.turi = turi
    def chiqarish4(self):
        print(self.nomi,self.laqabi,self.turi)

    def chiqarish5(self):
        print("sevimli",self.nomi,"chaqqon",self.laqabi,"uy hayvoni emas",self.turi)

ot1 = Ot("ot","jiyron","yovvoyi")
ot2 = Ot("ot","voronko","yovvoyi")
ot3 = Ot("ot","chubar","yovvoyi")

print(ot1.chiqarish4())
print(ot1.chiqarish5())

print(ot2.chiqarish4())
print(ot2.chiqarish5())

print(ot3.chiqarish4())
print(ot3.chiqarish5())