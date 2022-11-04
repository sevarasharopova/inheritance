class Taom:
    def __init__(self,turi,mazasi):
    
        self.turi = turi
        self.mazasi = mazasi
       

    def __str__(self):
        return f"{self.turi},{self.mazasi}"
    
    

class Osh(Taom):
    def __init__(self,turi,mazasi,hidi):
        super(). __init__(turi,mazasi)
        self.hidi = hidi

    def kiritish0(self):
        print(self.turi,self.mazasi,self.hidi)

    def kiritish1(self):
        print("eng yoqtirgan taomim",self.turi,self.mazasi,"mazali",self.hidi)


osh1 = Osh("osh","shirin","xushboy")
osh2 = Osh("xonim","juda zo\'r","yoqimli")
osh3 = Osh("sho\'rva","shirin","yoqimli")

print(osh1.kiritish0())
print(osh1.kiritish1())

print(osh2.kiritish0())
print(osh2.kiritish1())

print(osh3.kiritish0())
print(osh3.kiritish1())



class Kabob(Taom):
    def __init__(self,turi,mazasi,nomi):
        super(). __init__(turi,mazasi)
        self.nomi = nomi

    def kiritish3(self):
        print(self.turi,self.mazasi,self.nomi)

    def kiritish4(self):
        print(self.turi,"eng zo\'r taomim",self.mazasi,self.nomi,"mazasiga gap yo\'q")

kabob2 = Kabob("kabob","shirin","shashlik")
kabob3 = Kabob("kabob","mazali","tabaka")
kabob4 = Kabob("kabob","yoqimli","tandir")

print(kabob2.kiritish3())
print(kabob2.kiritish4())

print(kabob3.kiritish3())
print(kabob3.kiritish4())

print(kabob4.kiritish3())
print(kabob4.kiritish4())


class  Manti(Taom):
    def __init__(self,turi,mazasi,shakli):
        super(). __init__(turi,mazasi)
        self.shakli = shakli

    def kiritish6(self):
        print(self.turi,self.mazasi,self.shakli)

    def kiritish7(self):
        print("xamirli taom",self.turi,self.mazasi,"bukilishi ajoyib",self.shakli)

manti7 = Manti("manti","yoqimli","gullik")
manti8 = Manti("chuchvara","mazali","tugunchalik")
manti9 = Manti("somsa","shirin","tomchi")

print(manti7.kiritish6())
print(manti7.kiritish7())

print(manti8.kiritish6())
print(manti8.kiritish7())

print(manti9.kiritish6())
print(manti9.kiritish7())