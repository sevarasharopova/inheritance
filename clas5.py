class Shahar:
    def __init__(self,nomi,maydoni):
    
        self.nomi = nomi
        self.maydoni = maydoni
       

    def __str__(self):
        return f"{self.nomi},{self.maydoni}"
    

class Toshkent(Shahar):
    def __init__(self,nomi,maydoni,aholisi):
        super(). __init__(nomi,maydoni)
        self.aholisi= aholisi

    def chiqarish0(self):
        print(self.nomi,self.maydoni,self.aholisi)   

    def chiqarish1(self):
        print("sevimli shahrim Toshkent",self.nomi,self.maydoni,"aholisi eng ko\'p shahar",self.aholisi)
    
    def chiqarish3(self):
        print(self.nomi,"tumani",self.maydoni,"ming km.kv",self.aholisi,"ming kishi")
    
toshkent2 = Toshkent("non shahri",3348,2694400)
toshkent3 = Toshkent("Bektemir",1.83,29.9)
toshkent4 = Toshkent("Mirobod",1.71,123.8)

print(toshkent2.chiqarish0())
print(toshkent2.chiqarish1())

print(toshkent3.chiqarish0())
print(toshkent3.chiqarish3())

print(toshkent4.chiqarish0())
print(toshkent4.chiqarish3())




class Navoiy(Shahar):
    def __init__(self,nomi,maydoni,tumani):
        super().__init__(nomi,maydoni)
        self.tumani = tumani


    def chiqarish3(self):
        print(self.nomi,self.maydoni,self.tumani)

    def chiqarish4(self):
        print(self.nomi,"ismlariga atab qo'yilgan",self.maydoni,"ming km.kv ga yetadi",self.tumani,"ta  men qiziltepa tumanidanman")

    def chiqarish5(self):
        print(self.nomi,"tumani",self.maydoni,"ming km.kv",self.tumani,"ming kishi")

navoiy3 = Navoiy("Alisher Navoiy",111,8,)
navoiy4 = Navoiy("nurota",65,7)
navoiy5 = Navoiy("Qiziltepa",2.2,1,)

print(navoiy3.chiqarish3())
print(navoiy3.chiqarish4())

print(navoiy4.chiqarish3())
print(navoiy4.chiqarish5())

print(navoiy5.chiqarish3())
print(navoiy5.chiqarish5())



class Fargona(Shahar):
    def __init__(self, nomi,maydoni,balandligi):
        super().__init__(nomi,maydoni)
        self.balandligi = balandligi

    def textcha1(self):
       print(self.nomi,self.maydoni,self.balandligi) 

    def textcha2(self):
        print("eng go\'zal shahar",self.nomi,"deb yuritiladi",self.maydoni,"km.kv",self.balandligi,"metr")

    def textcha3(self):
        print(self.nomi,"tumani",self.maydoni,"ming km.kv",self.balandligi,"metr")

fargona5 = Fargona("gullar shahri",1.003,580)
fargona6 = Fargona("Beshariq",77,678)
fargona7 = Fargona("Buvayda",22,345)

print(fargona5.textcha1())
print(fargona5.textcha2())

print(fargona6.textcha1())
print(fargona6.textcha3())

print(fargona7.textcha1())
print(fargona7.textcha3())