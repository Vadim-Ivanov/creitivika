import list1
import potop
pole = list1.pole
pole1 = list1.pole1
my_pole_vr = list1.my_pole_vr
pole_vr = list1.pole_vr
my_pole = list1.my_pole

def popal(x_snaryad,y_snaryad,storona,storona_sopernika):
    if x_snaryad < 0 or x_snaryad > 9 or y_snaryad < 0 or y_snaryad > 9:
        print("Ошибка: выход за границы поля")
        return False 
    if storona[y_snaryad][x_snaryad] == "#":
        storona[y_snaryad][x_snaryad] = "x"
        storona_sopernika[y_snaryad][x_snaryad] = "x"
        if potop.potop(storona,x_snaryad,y_snaryad) == True:
            print("потопил")
            return True
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