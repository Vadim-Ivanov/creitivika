import list
pole = list.pole()
pole1 = list.pole1()
my_pole_vr = list.my_pole_vr()
pole_vr = list.pole_vr()
my_pole = list.my_pole()
def rass(spis):
    napr = ["up","down","right","left"]
    for d in range(1,5):
        for i in range(5-d):
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
                    pr = add_ship(x-1,y-1,1,0,0,spis)
                else:
                    if spis == pole:
                        n = input("направление ")
                    else:
                        n = napr[random.randint(0,3)]
                    if n == "left":
                        pr = add_ship(x-1,y-1,d,-1,0,spis)
                    elif n == "right":
                        pr = add_ship(x-1,y-1,d,1,0,spis)
                    elif n == "up":
                        pr = add_ship(x-1,y-1,d,0,-1,spis)
                    elif n == "down":
                        pr = add_ship(x-1,y-1,d,0,1,spis)
            if spis == pole:
                p()
                
def p():
    for i in my_pole_vr:
        for j in i:
            print(j,end=" ")
        print()
    print("\n")
    for i in pole:
        for j in i:
            print(j,end=" ")
        print()
#     print("\n")
#     for i in pole_vr:
#         for j in i:
#             print(j,end=" ")
#         print()

        
        
        
def add_ship(x0,y0,d,px,py,spis):
    for i in range(d):
        x = x0 + i * px 
        y = y0 + i * py
        if (x < 0 or x > 9 or y < 0 or y > 9) and spis == pole:
            print("Ошибка: выход за границы поля")
            return False
        elif (x < 0 or x > 9 or y < 0 or y > 9) and spis != pole:
            return False
        for dy in range(-1,2):
            for dx in range(-1,2):
                if x + dx < 0 or x + dx > 9 or y + dy < 0 or y + dy > 9:
                    continue
                if spis[y + dy][x + dx] == "#":
                    if spis == pole:
                        print("Ошибка: нельзя ставить рядом с другими кораблями")
                        return False
                    else:
                        return False
    for i in range(d):
        x = x0 + i * px 
        y = y0 + i * py
        spis[y][x] = "#"
    return True

def potop(spis,x_s,y_s):
    napr_x = [1,-1,0,0]
    napr_y = [0,0,1,-1]
    for i in range(4):
        x = x_s + napr_x[i]
        y = y_s + napr_y[i]
        while x >= 0 and x <= 9 and y >= 0 and y <= 9 and spis[y][x] != "*" and spis[y][x] != "0":
            if spis[y][x] == "#":
                return False
            x = x_s + napr_x[i]
            y = y_s + napr_y[i]
    return True
        
        
def popal(x_snaryad,y_snaryad,storona,storona_sopernika):
    if x_snaryad < 0 or x_snaryad > 9 or y_snaryad < 0 or y_snaryad > 9:
        print("Ошибка: выход за границы поля")
        return False 
    if storona[y_snaryad][x_snaryad] == "#":
        storona[y_snaryad][x_snaryad] = "x"
        storona_sopernika[y_snaryad][x_snaryad] = "x"
        if potop(storona,x_snaryad,y_snaryad) == True:
            print("потопил")
        else:
            print("попал")
        return True
    elif storona[y_snaryad][x_snaryad] == "*":
        storona[y_snaryad][x_snaryad] = "0"
        storona_sopernika[y_snaryad][x_snaryad] = "0"
        print("промазал")
        return "m"
    else:
        print("Ошибка: повторное попадание в клетку")
        return False 
        
def pob(listing):
    pobed = 0
    for i in range(10):
        for j in range(10):
            if listing[i][j] == "#":
                pobed += 1
    if pobed > 0:
        return False
    elif pobed <= 0:
        return True