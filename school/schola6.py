from calculator import umnoj
j=1 #количество действий
def I(new_pr, *args): #Функция, которая решает все примеры в массиве new_pr с определёнными знаками (их массив находится в *args)
    global j
    s=list(map(lambda x: pr.count(x),args)) #Количество знаков
    for y in range(sum(s)): 
        i=list(map(lambda x: new_pr.index(x),args)) #Список индексов знаков
        b=min(i) #Минимальный индекс знака
        if b==len(new_pr) or not(new_pr[b-1].isdigit()) or not(new_pr[b+1].isdigit()): #Если рядом со знаком не числа, либо он находится на последнем месте в массиве, то мы заканчиваем решение с этими знаками
            return
        chis1=new_pr[b-1] #Число, находящееся слева от знака
        chis2=new_pr[b+1] #Число, находящееся справа от знака
        if new_pr[b]=='**': #вычисляем возведение в степень
            v=int(chis1)**int(chis2)
        elif new_pr[b]=='*': #вычисляем умножение
            umnoj(int(chis1), int(chis2))
            v=int(chis1)*int(chis2)
        elif new_pr[b]=='//': #вычисляем деление
            v=int(chis1)//int(chis2)
        elif new_pr[b]=='+': #вычисляем сумму
            v=int(chis1)+int(chis2)
        else: #вычисляем вычитание
            v=int(chis1)-int(chis2)
        j+=1
        znak=new_pr[b] #Знак в виде строки
        new_pr.pop(b-1) #Убираем число, находящееся левее от знака 
        new_pr.pop(b) #Убираем число, находящееся правее от знака 
        new_pr[b-1]=str(v) #Заменяем знак на получившееся в результате решения число
        print(str(j)+') '+chis1+' '+znak+' '+chis2+' = '+str(v)) #Выводим алгоритм решения
vvod=input('Введите пример. Числа и все операции должны быть через пробел: ') #Строка, которую мы получаем на вход
print(str(j)+') '+vvod)
vvod=vvod.replace('(',' ( ') #Ставим пробелы перед и после скобки
vvod=vvod.replace(')',' ) ')
pr=vvod.split() #Превращаем строку в массив, разделённый пробелами
y=[] #массив с индексами скобочек
l=0
skob_pr=pr.copy()
for x in range(vvod.count('(')):
    y.append([skob_pr.index('(')+l,skob_pr.index(')')+l])
    skob_pr.remove('(')
    skob_pr.remove(')')
    l+=2
new_pr=pr.copy() 
new_pr.append('*') #делаем это, чтобы не выдавало ошибку на 5-ой строке
new_pr.append('//') 
new_pr.append('+') 
new_pr.append('-') 
new_pr.append('**') 
for h in y: 
    skob=pr[h[0]+1:h[1]] #действия внутри скобочек
    skob.append('*') #делаем это, чтобы не выдавало ошибку на 5-ой строке
    skob.append('//')
    skob.append('+')
    skob.append('-')
    skob.append('**')
    I(skob,'**') #Решаем примеры в скобочке
    I(skob,'*','//') 
    I(skob,'-','+')
    chis3=skob[0]
    new_pr[new_pr.index('('):new_pr.index(')')]='' #Убираем всё, что было в скобочках (кроме закрывающей скобочки) 
    new_pr[new_pr.index(')')]=chis3 #Заменяем закрывающую скобочку на число, получившееся внутри скобок
d=[]
chis=''
otv=''
I(new_pr,'**') #Решаем примеры с раскрытыми скобочками
I(new_pr,'*','//')
I(new_pr,'-','+')

