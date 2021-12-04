import list1
pole = list1.pole
pole1 = list1.pole1
my_pole_vr = list1.my_pole_vr
pole_vr = list1.pole_vr
my_pole = list1.my_pole

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