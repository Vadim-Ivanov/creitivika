import random
import list1
import p
import popal
import pob
pole = list1.pole
pole1 = list1.pole1
my_pole_vr = list1.my_pole_vr
pole_vr = list1.pole_vr
my_pole = list1.my_pole

def n():
    sopernik = 0
    I = 0
    while I == sopernik:
        sopernik = random.randint(0,7)
        I = random.randint(0,7)
    while sopernik != I:
        if I > sopernik:
            print("вы начинаете")
            pop = ""
            while pop != "m":
                p.p()
                x = int(input("столбец куда стрелять "))
                y = int(input("строка куда стрелять "))
                pop = popal.popal(x-1,y-1,pole_vr,my_pole_vr)
                if pob.pob(pole_vr) == True:
                    print("победа")
                    I = sopernik
                    pop = "m"
                elif pob.pob(pole) == True:
                    print("проиграл")
                    I = sopernik
                    pop = "m"
            if I != sopernik:
                sopernik = 1
                I = 0
            
        elif I < sopernik:
            print("соперник начинает")
            pop = 0
            while pop != "m":
                x = random.randint(0,9)
                y = random.randint(0,9)
                pop = popal.popal(x,y,pole,my_pole)
                if pob.pob(pole_vr) == True:
                    print("победа")
                    I = sopernik
                    pop = "m"
                elif pob.pob(pole) == True:
                    print("проиграл")
                    I = sopernik
                    pop = "m"
            if I != sopernik:
                sopernik = 0
                I = 1

