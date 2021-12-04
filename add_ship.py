import list1
pole = list1.pole
pole1 = list1.pole1
my_pole_vr = list1.my_pole_vr
pole_vr = list1.pole_vr
my_pole = list1.my_pole

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