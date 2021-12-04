import list1
import random
import add_ship
import p 
pole = list1.pole
pole1 = list1.pole1
my_pole_vr = list1.my_pole_vr
pole_vr = list1.pole_vr
my_pole = list1.my_pole
ship_type = list1.ship_type

def rass(spis):
    napr = ["up","down","right","left"]
    for d in range(1,5):
        for i in range(5-d):
            if i != 10000:
                pr = False
                while pr != True:
                    if spis == pole:
                        print(ship_type[d-1])
                        x = int(input("столбец "))
                        y = int(input("строка "))
                    else:
                        x = random.randint(0,9) + 1
                        y = random.randint(0,9) + 1
                    if d == 1:
                        pr = add_ship.add_ship(x-1,y-1,1,0,0,spis)
                    else:
                        if spis == pole:
                            n = input("направление ")
                        else:
                            n = napr[random.randint(0,3)]
                        if n == "left":
                            pr = add_ship.add_ship(x-1,y-1,d,-1,0,spis)
                        elif n == "right":
                            pr = add_ship.add_ship(x-1,y-1,d,1,0,spis)
                        elif n == "up":
                            pr = add_ship.add_ship(x-1,y-1,d,0,-1,spis)
                        elif n == "down":
                            pr = add_ship.add_ship(x-1,y-1,d,0,1,spis)
                if spis == pole:
                    p.p()
