def umnoj_2(n):
    print("что бы умножить на 2,мы прибавляем к числу его же")
    print(f"{n} + {n} = {n*2}")

def umnoj_3(n):
    print("что бы умножить на 3, сначала умножаем на 5")
    umnoj_5(n)
    print("затем вычитаем это число один 2 раза")
    print(f"{n*10} - {n} - {n} = {n*3}")
    
def umnoj_4(n):
    print("что бы умножить на 4, сначала умножаем на 5")
    umnoj_5(n)
    print("затем вычитаем это число один раз")
    print(f"{n*10} - {n} = {n*4}")
    
def umnoj_5 (n):
    print("что бы умножить на 5, сначала умножаем на 10")
    umnoj_10(n)
    print("затем делим на 2")
    print(f"{n*10} / 2 = {n*5}")

def umnoj_6 (n):
    print("что бы умножить на 6, сначала умножаем на 5")
    umnoj_5(n)
    print("затем на прибавляем это число")
    print(f"затем складываем {n*5} + {n} = {n*6}")
          
def umnoj_7 (n):
    print("что бы умножить на 7, сначала умножаем на 5")
    umnoj_5(n)
    print("затем на 2")
    umnoj_3(n)
    print(f"затем складываем умножение на 5 и на 2, {n*5} + {n*3} = {n*6}")
          
def umnoj_8 (n):
    print("что бы умножить на 8, сначала умножаем на 5")
    
    umnoj_5(n)
    print("затем на 3")
    umnoj_3(n)
    print(f"затем складываем умножение на 5 и на 2, {n*5} + {n*3} = {n*8}")
          
def umnoj_9(n):
    print("что бы умножить на 9, сначала умножаем на 10")
    umnoj_10(n)
    print("затем отнимаем один раз это число")
    print(f"{n*10} - {n} = {n*9}")

def umnoj_10(n):
    print("что бы умножить на 10 к числу дописываем ноль")
    print(f"{n} * 10 = {n*10}")
def umnoj (n,k):
    if (k <= 10):
        if (k == 10):
            umnoj_10(n)    
            return
        if (k == 9):
            umnoj_9(n)
            return
        if (k == 8):
            umnoj_8(n)
            return
        if (k == 7):
            umnoj_7(n)
            return
        if (k == 6):
            umnoj_6(n)
            return
        if (k == 5):
            umnoj_5(n)
            return
        if (k == 4):
            umnoj_4(n)
            return
        if (k == 3):
            umnoj_3(n)
            return
        if (k == 2):
            umnoj_2(n)
            return




