import list1
pole = list1.pole
pole1 = list1.pole1
my_pole_vr = list1.my_pole_vr
pole_vr = list1.pole_vr
my_pole = list1.my_pole

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