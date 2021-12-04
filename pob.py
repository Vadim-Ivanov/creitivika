import list1
pole = list1.pole
pole1 = list1.pole1
my_pole_vr = list1.my_pole_vr
pole_vr = list1.pole_vr
my_pole = list1.my_pole

def pob(listing):
    pobed = 0
    for i in range(10):
        for j in range(10):
            if listing[i][j] == "#":
                pobed += 1
    if pobed > 0:
        return False
    else:
        return True