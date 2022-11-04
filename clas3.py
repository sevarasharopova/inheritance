class Odam:
    def __init__(self,ismi,familiyasi):
        self.ismi = ismi
        self.familiyasi = familiyasi
        

    def __str__(self):
        return f"{self.ismi},{self.familiyasi}"
    
   


class Shifokor(Odam):
    def __init__(self,ismi,familiyasi,maoshi):
        super(). __init__(ismi,familiyasi)
        self.maoshi = maoshi

    def textcha1(self):
        print(self.ismi,self.familiyasi,self.maoshi)

    def textcha2(self):
        print(self.ismi,self.familiyasi,"juda taniqli shifokor",self.maoshi)

shifokor1 = Shifokor("Aziza","Asadova","yaxshi")
shifokor2 = Shifokor("Dilsora","Mirzayeva","zo\'r")
shifokor3 = Shifokor("Nozima","Haydarova","o\'rtacha")

print(shifokor1.textcha1())
print(shifokor1.textcha2())

print(shifokor2.textcha1())
print(shifokor2.textcha2())

print(shifokor3.textcha1())
print(shifokor3.textcha2())
        
class Oqituvchi(Odam):
    def __init__(self,ismi,familiyasi,martabasi):
        super(). __init__(ismi,familiyasi)
        self.martabasi = martabasi
        
    def chiqarish1(self):
        print(self.ismi,self.familiyasi,self.martabasi)

    def chiqarish2(self):
        print("mening sevimli o\'qituvchim",self.ismi,self.familiyasi,self.martabasi)

oqituvchi3 = Oqituvchi("Xolida","Karimova","oliy")
oqituvchi4 = Oqituvchi("Shoxsanam","Mirzayeva","oliy")
oqituvchi5 = Oqituvchi("Ubaydullo","Jumayev","oliy")

print(oqituvchi3.chiqarish1())
print(oqituvchi3.chiqarish2())

print(oqituvchi4.chiqarish1())
print(oqituvchi4.chiqarish2())

print(oqituvchi5.chiqarish1())
print(oqituvchi5.chiqarish2())

class Shoira(Odam):
    def __init__(self,ismi,familiyasi,ijodi):
        super(). __init__(ismi,familiyasi)
        self.ijodi = ijodi
        
    def chiqarish4(self):
        print(self.ismi,self.familiyasi,self.ijodi)

    def chiqarish5(self):
        print("mening sevimli shoirim",self.ismi,self.familiyasi,self.ijodi,"she'rini yoqtiraman")

shoira4 = Shoira("Zulfiya","Isroilova","ona")
shoira5 = Shoira("nodira","ahadova","yurtim")
shoira6 = Shoira("Nargiza","Saidova","hayot")

print(shoira4.chiqarish4())
print(shoira4.chiqarish5())

print(shoira5.chiqarish4())
print(shoira5.chiqarish5())

print(shoira6.chiqarish4())
print(shoira6.chiqarish5())
        
        