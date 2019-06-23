def sagslas(adet):
    for i in range(int(adet)):
        print("/",end="")

def solSlas(adet):
    for i in range(int(adet)):
        print("\\",end="")

def satirAtla(adet):
    for i in range(int(adet)):
        print()
        
def bosluk(adet):
    for i in range(int(adet)):
        print(" ",end="")

def üstKisim(cap):
    baslangicbosluk=cap/2-1
    for i in range(int(cap/2)):
        bosluk(baslangicbosluk-i)
        sagslas(1)
        bosluk(i*2)
        solSlas(1)
        satirAtla(1)

def altKisim(cap):
    baslangicbosluk=cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        solSlas(1)
        bosluk(baslangicbosluk-i*2)
        sagslas(1)
        satirAtla(1)

üstKisim(20)
altKisim(20)


