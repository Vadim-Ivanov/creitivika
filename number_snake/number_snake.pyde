#объявляем переменные
list_prep = [] 
gran_left = 0
gran_right = 600
i = 1

X = 600
pX = 600
kof = 1.0 * pX / X

X_size = pX
Y_size = floor(800 * kof)

dict_int = {'score':0,'start':False,'shop':False,'snake_head_X':300,'snake_head_Y':500,'prep_Y':0,'palette':False,'esc':False,'boss':False,'invul':False,
            'iridescent colors':False}
dict_const = {'gran_left':0,'gran_right':600,'snake.scroll_tail_Y':3,'snake.move_to_palette_X':400,'snake.move_to_palette_Y':100,'gran_left_palette_line':50,'gran_right_palette_line':305,'palette_Y_line':50}
dict_const_fill = {'button_LEFT_RIGHT_palette':125,'text_LEFT_RIGHT_palette':0}
dict_const_stroke = {'line_palette1':125,'line_palette2':255,'button_collor_green_pallete':[0,255,0],'button_collor_red_pallete':[255,0,0],'button_palette':0,'RGB_palette':255}
dict_const_strokeWeight = {'line_palette':5,'button_palette':1}
dict_const_rect = {'button_collor_pallete':[50,200,50,50],'button_LEFT_palette':[50,400,25,50],'button_RIGHT_palette':[80,400,25,50],'list_fill':[50,480,55,55]}
dict_const_triangle = {'i':0}
dict_const_ellipse = {'i':0}
dict_const_text = {'RIGHT_paletter':[92.5,440],'LEFT_paletter':[62.5,440]}
dict_const_textSize = {'LEFT_RIGHT_palette':30,'RGB_palette':30}
upgrade_dict = {'cooldown':[15,500,1],'cartridges':[5,500,1],'bonus':[1,500,1],'punching':[1,500,1],'invulnerability':[1,500,1],
                'iridescent colors':[0,20000,1],'speed':[3,250,1],'speed cartridges':[3,500,1],'speed boss cartridges':[10,10000,1]}
#перезарядка,патроны,бонус,пробивание,патронов при выстреле,переливающиеся цвета,скорость,скорость стрельбы пушки
upgrade_list = ['cooldown','cartridges','bonus','punching','invulnerability','iridescent colors','speed','speed cartridges','speed boss cartridges']
upgrade_list_Russian = [u'перезарядка',u'патроны',u'бонус',u'пробивание',u'неуязвимость',u'переливающиеся \n цвета',u'скорость',u'скорость \n пуль',u'стрельба \n вражеской \n пушки']
upgrade = {}
#неуязвимость
class invulnerability:
    def __init__(self):
        self.invulnerability = upgrade_dict['invulnerability'][0]
        self.time = True
        self.time_invul = 0
    def draw_(self):
        global dict_int,immage
        #рисуем значок
        image(immage[5],500,700,60,60)
        text(self.invulnerability,490,690)
        if self.invulnerability > 0:
            #если нажимаем то используем
            if (mousePressed == True and self.time == True and mouseX > 500 * kof and mouseX < 560 * kof and mouseY > 700 * kof and mouseY < 760 * kof) or (self.time == True and keyPressed == True and key == 'q' or key == u'й'):
                self.time = False
                dict_int['invul'] = True
                self.time_invul = 1
                self.invulnerability -= 1
            if mousePressed == False and keyPressed == False: 
                self.time = True
        #отключение неуязввимости
        if self.time_invul > 0:
            self.time_invul += 1
            if self.time_invul % 1000 == 0 or dict_int['start'] == False:
                dict_int['invul'] = False
    def plus(self):
        if dict_int['start'] == False:
            self.invulnerability = upgrade_dict['invulnerability'][0]
#босс
class Boss:
    def __init__(self):
        self.l = 0
        self.b = 0
        self.time = 0
    def draw_(self):
        #определяем направление полёта
        if dict_int['esc'] == False:
            self.b = sqrt((snake.head_X() * kof - X_size / 2)**2 + (500 * kof)**2)
            self.l = asin((X_size / 2 - snake.head_X() * kof) / self.b) * 57.3
        #рисуем босса
        push()
        rectMode(CENTER)
        translate(300,0)
        rotate(radians(self.l))
        image(immage[2],-50,-36.5,100,73)
        pop()
        #каждые 30 кадров босс стреляем
        if self.time % 30 == 0:
            boss_cartridges.plus(self.l)
        self.time += 1
#пуля босса
class Boss_cartridges:
    def __init__(self):
        self.cartridges = []
        self.l = 0
        self.time_cartridges = True
    def draw_(self):
        for i in range(len(self.cartridges) - 1):
            #рисуем все пули
            push()
            translate(self.cartridges[i]['x'],self.cartridges[i]['y'])
            rotate(radians(90 + self.cartridges[i]['l']))
            image(immage[3],-15 * kof,-7.5 * kof,30,15)
            pop()
            #двигаем пули
            self.cartridges[i]['y'] += self.cartridges[i]['speed_Y']
            self.cartridges[i]['x'] += self.cartridges[i]['speed_X']
        #если пуля улетела за границу экрана, то удаляем её
        if len(self.cartridges) > 0:
            if self.cartridges[0]['y'] >= Y_size:
                del self.cartridges[0]
                #если касается головы, то у змейки отнимается жизнь, а пуля удаляется
        for i in range(len(self.cartridges) - 1):
            if self.time_cartridges == True:
                if 500 / kof > self.cartridges[i]['y'] - 25 and 500 / kof < self.cartridges[i]['y'] + 25: 
                    if (self.cartridges[i]['x'] - (-15 * kof) - 25) <= snake.head_X() / kof: 
                        if (self.cartridges[i]['x'] - (-7.5 * kof) + 25) >= snake.head_X() / kof:
                            if dict_int['invul'] == False:
                                snake.dlina(-1)
                            del self.cartridges[i]
                            self.time_cartridges = False
        self.time_cartridges = True
    #создаём пулю
    def plus(self,l):
        self.l = l
        self.cartridges.append(dict(x = 300,y = 10,l = self.l,speed_Y = upgrade_dict['speed boss cartridges'][0] / kof,
                                    speed_X = (upgrade_dict['speed boss cartridges'][0] * (snake.head_X() - 300)) / (500 * kof))) 
    #удаляем все пули
    def minus(self):
        for i in range(len(self.cartridges)):
            del self.cartridges[0]
#пауза
class esc:
    def __init__(self):
        self.X = 550
        self.Y = 20
        self.time = True
        self.esc = 0
    def draw_(self):
        #если кнопка нажата, то ставим на паузу
        if keyPressed == True:
            if key == 'e' or key == u'у':
                dict_int['esc'] = True
        #рисуем экран паузы
        if dict_int['esc'] == True:
            if self.esc == 0:
                fill(0,0,0,230)
                rect(150,150,300,400)
                fill('#0E18C1')
                rect(200,250,200,80)
                rect(200,380,200,80)
                fill(255,255,0)
                textSize(30)
                text(u'пауза',300,200)
                text(u'продолжить',300,305)
                text(u'в меню',300,435)
            if mousePressed == True:
                #если нажата кнопка "продолжить", то продолжаем
                if mouseX / kof > 200 and mouseX / kof < 400 and mouseY / kof > 250 and mouseY / kof < 330 and self.time == True:
                    self.time = False
                    self.esc = 1
                #если нажата кнопка "в меню", то выходим в меню
                if mouseX / kof > 200 and mouseX / kof < 400 and mouseY / kof > 380 and mouseY / kof < 460 and self.esc == 0:
                    dict_int['esc'] = False
                    snake.dlina_to(0)
                if self.esc == 2:
                    dict_int['esc'] = False
                    self.esc = 0
            else:
                self.time = True
                if self.esc == 1:
                    self.esc = 2
class lava:
    def __init__(self):
        self.p = [dict(x = random(10,X_size),y = -15,num = floor(random(1,10)),gold = 0)]
    def draw_lava(self,head_X):
        for i in range(len(self.p)):
            #рисуем все кубики лавы
            strokeWeight(1)
            image(immage[1],self.p[i]['x'],self.p[i]['y'],30,30)
            textSize(12)
        #если кубик лавы выходит за края, то удаляем его
        if len(self.p) > 0:
            if self.p[0]['y'] >= Y_size / kof:
                del self.p[0]
        #если кубик лавы касается головы, то убиваем змейку и удаляем лаву
        for i in range(len(self.p)):
            if self.p[i]['y'] >= 462.5 and self.p[i]['y'] <= 537.5 and self.p[i]['x'] <= head_X and self.p[i]['x'] >= head_X - 37.5:
                if dict_int['invul'] == False:
                    snake.dlina_to(0)
                del self.p[i]
                return ' '
    #передвижение лавы
    def move(self):
        for i in range(len(self.p)):
            if prep.polog_Y() < 360 or prep.polog_Y() > 370:
                self.p[i]['y'] += upgrade_dict['speed'][0]
    #добавление кубика лавы
    def plus_lava(self):
        if prep.polog_Y() > 20 and prep.polog_Y() < 800 and dict_int['esc'] == False:
            self.p.append(dict(x = random(10,590),y = -15))
    #удаление всех кубиков лавы
    def lava_clear(self):
        for i in range(len(self.p)):
            del self.p[0]
#патроны змейки
class cartridges:
    def __init__(self):
        self.quantity = upgrade_dict['cartridges'][0]
        self.cartridges = []
        self.keyTime = True
        self.cartridge = self.quantity
        self.cart_time = 0
    def draw_(self):
        #рисуем значок
        fill(255)
        text(self.cartridge,80,710)
        image(immage[4],40,700,60,60)
        #если кнопка пробел нажата, то создаём пулю
        if keyPressed == True and key == " " and len(self.cartridges) <= self.quantity and self.keyTime == True and dict_int['esc'] == False and self.cartridge > 0:
            self.cartridges.append(dict(x = snake.head_X(),y = dict_int['snake_head_Y'],speed = upgrade_dict['speed cartridges'][0]))
            self.keyTime = False
            self.cartridge -= 1
        #добавляем патроны если их меньше чем нужно
        if self.cartridge != self.quantity:
            self.cart_time += 1
            if self.cart_time % (upgrade_dict['cooldown'][0] * 25) == 0:
                self.cartridge += 1
        if keyPressed == False:
            self.keyTime = True
        for i in range(len(self.cartridges)-1):
            #рисуем все пули
            push()
            translate(self.cartridges[i]['x']-4 * kof,self.cartridges[i]['y']-7.5 * kof)
            rotate(radians(-90))
            image(immage[3],0,0,30,15)
            pop()
            #передвигаем пули
            if dict_int['esc'] == False:
                cartridge.move(i)
            #если пуля долетела до края экрана, то удаляем её
            if self.cartridges[i]['y'] <= 0:
                del self.cartridges[i]
    #удаляем пулю
    def del_cart(self):
        del self.cartridges[0]
    #передвигаем пулю
    def move(self,i):
        self.cartridges[i]['y'] -= self.cartridges[i]['speed']
    #координаты пули по Y
    def Y_cartridges(self):
        if len(self.cartridges) > 0:
            return self.cartridges[0]['y']
    #координаты пули по X
    def X_cartridges(self):
        if len(self.cartridges) > 0:
            return self.cartridges[0]['x']
    #добавлдяем патроны
    def plus(self):
        self.cartridge = upgrade_dict['cartridges'][0]
    #удаляем летящие пули
    def minus(self):
        for i in range(len(self.cartridges)):
            del self.cartridges[0]
#палитра
class button_palette:
    def __init__(self):
        self.x = [175,175,175]
        self._fill_ = [{'R':255,'G':255,'B':255}]
        self.time = True
        self.mousePressed_time = True
        self.int_fill = 0
        self.RGB_ = ['R','G','B']
        self.time_iridescent_colors = 0
        self.rgb = 0
        self.iridescent_colors = 0
        self.timeT = True
        self.time_fill = True
    def palette(self):
        #рисуем змейку
        snake.draw_()
        snake.scroll_tail_Y(dict_const['snake.scroll_tail_Y'])
        #переносим голову змейки в верх экрана
        snake.move_to(dict_const['snake.move_to_palette_X'],dict_const['snake.move_to_palette_Y'])
        strokeWeight(dict_const_strokeWeight['line_palette'])
        stroke(dict_const_stroke['line_palette1'])
        #рисуем рычажки управления цветом
        for i in range(1,4):
            line(dict_const['gran_left_palette_line'],dict_const['gran_left_palette_line']*i,dict_const['gran_right_palette_line'],dict_const['gran_left_palette_line']*i)
            textSize(dict_const_textSize['RGB_palette'])
            fill(dict_const_stroke['RGB_palette'])
            text(self.RGB_[i-1],dict_const['gran_left_palette_line']-20,dict_const['gran_left_palette_line']*i+15)
        for i in range(1,4):
            stroke(dict_const_stroke['line_palette2'])
            line(self.x[i-1],(dict_const['palette_Y_line'] * i - 10),self.x[i-1],(dict_const['palette_Y_line'] * i + 10))
        if upgrade_dict['iridescent colors'][0] > 0:
            push()
            #если не включено "переливающиеся цвета", то рамка красная
            if self.iridescent_colors == 0:
                stroke(255,0,0)
                dict_int['iridescent colors'] = False
                snake._fill_(False)
            #иначе рамка зелёная
            else:
                stroke(0,255,0)
                dict_int['iridescent colors'] = True
                snake._fill_(self.rgb)
            if self.iridescent_colors > 1:
                self.iridescent_colors = 0
            #переводим цвет в формат HSB
            colorMode(HSB, 360, 100, 100)
            #рисуем переливающуюся кнопку
            strokeWeight(5)
            self.rgb += 1
            fill(self.rgb,100,100)
            self.time_iridescent_colors += 1
            rect(50,600,60,60)
            if self.rgb >= 360:
                self.rgb = 0
            #если нажали на кнопку, то включаем или выключаем переливание
            if mousePressed == True:
                if self.timeT == True:
                    if mouseX > 50 * kof and mouseX < 110 * kof and mouseY > 600 * kof and mouseY < 660 * kof:
                        self.iridescent_colors += 1
                        self.timeT = False
            else:
                self.timeT = True
            pop()
        if mousePressed == True:
            for i in range(1,4):
                #управляем рычажками мышкой
                if mouseX / kof >= dict_const['gran_left_palette_line'] and mouseX / kof <= dict_const['gran_right_palette_line'] and mouseY / kof > (i * (50 - 16) + i * 10) and mouseY / kof < (i * (50 + 16)):
                    self.x[i-1] = mouseX / kof
                if mouseX / kof < dict_const['gran_left_palette_line'] and mouseX / kof > dict_const['gran_left'] and mouseY / kof > (i * (50 - 16) + i * 10) and mouseY / kof < (i * (50 + 16)):
                    self.x[i-1] = dict_const['gran_left_palette_line']
                if mouseX / kof > dict_const['gran_right_palette_line'] and mouseX / kof < (dict_const['gran_right_palette_line'] + 45) and mouseY / kof > i * (50 - 16) + i * 10 and mouseY / kof < i * (50 + 16):
                    self.x[i-1] = dict_const['gran_right_palette_line']
                #если нажата левая кнопка то изменяем цвет на -1
                if mouseX / kof > dict_const_rect['button_LEFT_palette'][0]:
                    if mouseX / kof < (dict_const_rect['button_LEFT_palette'][0] + dict_const_rect['button_LEFT_palette'][2]):
                        if mouseY / kof > dict_const_rect['button_LEFT_palette'][1]:
                            if mouseY / kof < (dict_const_rect['button_LEFT_palette'][1] + dict_const_rect['button_LEFT_palette'][3]):
                                if self.int_fill > 0 and self.mousePressed_time == True:
                                    self.int_fill -= 1
                                    self.mousePressed_time = False
                #если нажата правая кнопка то изменяем цвет на +1
                if mouseX / kof > dict_const_rect['button_RIGHT_palette'][0]:
                    if mouseX / kof < (dict_const_rect['button_RIGHT_palette'][0] + dict_const_rect['button_RIGHT_palette'][2]):
                        if mouseY / kof > dict_const_rect['button_RIGHT_palette'][1]:
                            if mouseY / kof < (dict_const_rect['button_RIGHT_palette'][1] + dict_const_rect['button_RIGHT_palette'][3]):
                                if self.int_fill < len(self._fill_)-1 and self.mousePressed_time == True:
                                    self.int_fill += 1
                                    self.mousePressed_time = False
            #если нажата кнопка то добавляем цвет в список
            if mouseX / kof > 50 and mouseX / kof < 100 and mouseY / kof > 200 and mouseY / kof < 250 and dict_int['score'] >= 500:
                for i in range(len(self._fill_)):
                    if self._fill_[i]['R'] == self.x[0]-dict_const['gran_left_palette_line']:
                        if self._fill_[i]['G'] == self.x[1]-dict_const['gran_left_palette_line']:
                            if self._fill_[i]['B'] == self.x[2]-dict_const['gran_left_palette_line']:
                                self.mousePressed_time = False
                if self.mousePressed_time == True:
                    dict_int['score'] -= 500
                    self._fill_.append(dict(R = self.x[0]-dict_const['gran_left_palette_line'],G = self.x[1]-dict_const['gran_left_palette_line'],B = self.x[2]-dict_const['gran_left_palette_line']))
                    self.mousePressed_time = False
                    self.int_fill = len(self._fill_)-1
            #если нажимаем мышкой на кружок змейки то он меняет цвет
            snake.fill_(self._fill_[self.int_fill]['R'],self._fill_[self.int_fill]['G'],self._fill_[self.int_fill]['B'])
        else:
            self.mousePressed_time = True
        #определяем куплен цвет или нет и изменяем контур кнопки для покупки
        for i in range(len(self._fill_)):
            if self.time == True:
                if self._fill_[i]['R'] == self.x[0]-dict_const['gran_left_palette_line'] and self._fill_[i]['G'] == self.x[1]-dict_const['gran_left_palette_line'] and self._fill_[i]['B'] == self.x[2]-dict_const['gran_left_palette_line']:
                    stroke(dict_const_stroke['button_collor_green_pallete'][0],dict_const_stroke['button_collor_green_pallete'][1],dict_const_stroke['button_collor_green_pallete'][2])
                    self.time = False
                else:
                    stroke(dict_const_stroke['button_collor_red_pallete'][0],dict_const_stroke['button_collor_red_pallete'][1],dict_const_stroke['button_collor_red_pallete'][2])
        #удаляем повторяющиеся цвета
        for i in range(len(self._fill_)-1):
            for j in range(len(self._fill_)):
                if self._fill_[i] == self._fill_[j] and i != j:
                    del self._fill_[j]
                    self.int_fill -= 1
        #если в списке нет элементов то изменяем контур кнопки для покупки на красный
        if len(self._fill_) == 0:
            stroke(dict_const_stroke['button_collor_red_pallete'][0],dict_const_stroke['button_collor_red_pallete'][1],dict_const_stroke['button_collor_red_pallete'][2])
        self.time = True
        fill(self.x[0]-dict_const['gran_left_palette_line'],self.x[1]-dict_const['gran_left_palette_line'],self.x[2]-dict_const['gran_left_palette_line'])
        #рисуем кнопку покупки цветов
        strokeWeight(5)
        rect(dict_const_rect['button_collor_pallete'][0],dict_const_rect['button_collor_pallete'][1],dict_const_rect['button_collor_pallete'][2],dict_const_rect['button_collor_pallete'][3])
        stroke(dict_const_stroke['button_palette'])
        fill(dict_const_fill['button_LEFT_RIGHT_palette'])
        #рисуем кнопки вправо и влево
        strokeWeight(dict_const_strokeWeight['button_palette'])
        rect(dict_const_rect['button_LEFT_palette'][0],dict_const_rect['button_LEFT_palette'][1],dict_const_rect['button_LEFT_palette'][2],dict_const_rect['button_LEFT_palette'][3])
        rect(dict_const_rect['button_RIGHT_palette'][0],dict_const_rect['button_RIGHT_palette'][1],dict_const_rect['button_RIGHT_palette'][2],dict_const_rect['button_RIGHT_palette'][3])
        fill(dict_const_fill['text_LEFT_RIGHT_palette'])
        textSize(dict_const_textSize['LEFT_RIGHT_palette'])
        #рисуем на них значки
        text('>',dict_const_text['RIGHT_paletter'][0],dict_const_text['RIGHT_paletter'][1])
        text('<',dict_const_text['LEFT_paletter'][0],dict_const_text['LEFT_paletter'][1])
        fill(self._fill_[self.int_fill]['R'],self._fill_[self.int_fill]['G'],self._fill_[self.int_fill]['B'])
        #рисуем квадрат с купленными цветами
        rect(dict_const_rect['list_fill'][0],dict_const_rect['list_fill'][1],dict_const_rect['list_fill'][2],dict_const_rect['list_fill'][3])
#магазин
class button_shop:
    def __init__(self):
        self.snake_X = 250
        self.snake_Y = 100
        self.speed_snake = 2
        self.str_ = 0
        self.mouseTime = True
    def draw_(self):
        upgrade = {'cooldown':[upgrade_dict['cooldown'][0]-1,upgrade_dict['cooldown'][1]*2,upgrade_dict['cooldown'][2]+1],
                   'cartridges':[upgrade_dict['cartridges'][0]+2,upgrade_dict['cartridges'][1]*2,upgrade_dict['cartridges'][2]+1],
                   'bonus':[upgrade_dict['bonus'][0]+1,upgrade_dict['bonus'][1]*2,upgrade_dict['bonus'][2]+1],
                   'punching':[upgrade_dict['punching'][0]*2,upgrade_dict['punching'][1]*2,upgrade_dict['punching'][2]+1],
                   'invulnerability':[upgrade_dict['invulnerability'][0]+1,upgrade_dict['invulnerability'][1]*2,upgrade_dict['invulnerability'][2]+1],
                   'iridescent colors':[upgrade_dict['iridescent colors'][0]+1,upgrade_dict['iridescent colors'][1]*2,upgrade_dict['iridescent colors'][2]+1],
                   'speed':[upgrade_dict['speed'][0]+1,upgrade_dict['speed'][1]*2,upgrade_dict['speed'][2]+1],
                   'speed cartridges':[upgrade_dict['speed cartridges'][0]+1,upgrade_dict['speed cartridges'][1]*2,upgrade_dict['speed cartridges'][2]+1],
                   'speed boss cartridges':[upgrade_dict['speed boss cartridges'][0]/1.5,upgrade_dict['speed boss cartridges'][1]*5,upgrade_dict['speed boss cartridges'][2]+1]}
        #рисуем змейку
        snake.draw_()
        snake.scroll_tail_Y(dict_const['snake.scroll_tail_Y'])
        #переносим голову змейки в верх экрана
        snake.move_to(self.snake_X,self.snake_Y)
        #управляем головой змейки
        if self.snake_X >= 350:
            self.speed_snake = -2
        if self.snake_X <= 250:
            self.speed_snake = 2
        self.snake_X += self.speed_snake
        for i in range(3):
            for j in range(3):
                #рисуем кнопки покупок
                fill(0,255,0,240)
                rect(100*i+175,100*j+400,90,90)
                fill(0)
                textSize(15)
                text(u'ур.',100*i+175+35,100*j+400+25)
                text(upgrade_dict[upgrade_list[i*3+j]][2],100*i+175+55,100*j+400+25)
                textSize(10)
                text(upgrade_list_Russian[i*3+j],100*i+175+45,100*j+400+70)
                text(upgrade_dict[upgrade_list[i*3+j]][1],100*i+175+45,100*j+400+90)
                #если нажали на кнопку покупки, то покупаем то, что написано на кнопке
                if mousePressed == True and self.mouseTime == True and dict_int['score'] >= upgrade_dict[upgrade_list[i*3+j]][1]:
                    if mouseX / kof > 100*i+175 and mouseX / kof < 100*i+175+90 and mouseY / kof > 100*j+400 and mouseY / kof < 100*j+400+90:
                        dict_int['score'] -= upgrade_dict[upgrade_list[i*3+j]][1]
                        upgrade_dict[upgrade_list[i*3+j]] = upgrade[upgrade_list[i*3+j]]
                        self.mouseTime = False
                if mousePressed == False:
                    self.mouseTime = True
#старт
def button_start():
    global time_boss
    #переводим всё в первоначальное положение
    snake.dlina_to(20)
    prep.recovery_prep()
    ball.ball_clear()
    lava.lava_clear()
    dict_int['start'] = True
    time_boss = 0
    boss_cartridges.minus()
    cartridge.plus()
    cartridge.minus()
#кнопки
class Button():
    def __init__(self):
        self.X_start = 300
        self.Y_start = 400
        
        self.X_shop = 500
        self.Y_shop = 700
        
        self.X_palette = 25
        self.Y_palette = 700
    def draw_(self):
        fill(255,0,0)
        ellipse(self.X_start,self.Y_start,200,125)
        fill(255)
        triangle(self.X_start-20,self.Y_start-25,self.X_start-20,self.Y_start+25,self.X_start+30,self.Y_start)
        
        fill(0,255,0)
        rect(self.X_shop,self.Y_shop,75,75)
        fill(0,255,0)
        strokeWeight(3)
        ellipse(self.X_shop+37.5,self.Y_shop+30,20,20)
        strokeWeight(1)
        fill(255,0,0)
        rect(self.X_shop+20,self.Y_shop+30,35,35)
        
        fill(0,0,255)
        rect(self.X_palette,self.Y_palette,75,75)
        fill(0,255,0)
        ellipse(self.X_palette+37.5,self.Y_palette+37.5,70,70)
        push()
        noStroke()
        fill(0,0,255)
        ellipse(self.X_palette+37.5,self.Y_palette+37.5+20,15,15)
        pop()
        fill(255,0,0)
        ellipse(self.X_palette+15,self.Y_palette+37+10,15,15)
        fill(0,0,0)
        ellipse(self.X_palette+20,self.Y_palette+25,15,15)
        fill("#F2EB11")
        ellipse(self.X_palette+40,self.Y_palette+15,15,15)
        fill('#3DF2BD')
        ellipse(self.X_palette+55,self.Y_palette+32,15,15)
        fill(0,0,255)
        push()
        noStroke()
        translate(self.X_palette+62,self.Y_palette+57)
        rotate(radians(120))
        ellipse(0,0,30,25)
        pop()
        
        push()
        fill(0,0,255)
        noStroke()
        rect(0,0,100,60)
        pop()
        fill(255)
        textSize(24)
        text(u'деньги',50,42)
#сферы силы
class Ball:
    def __init__(self):
        self.p = [dict(x = random(10,590),y = -15,num = floor(random(1,10)),gold = 0)]
    def draw_ball(self,head_X):
        for i in range(len(self.p)):
            strokeWeight(1)
            #меняем цвет
            if self.p[i]['gold'] == 0:
                if self.p[i]['num'] < 0:
                    fill(255,0,0)
                else:
                    fill(0,255,0)
            else:
                fill('#FFF827')
            #рисуем сферы силы
            ellipse(self.p[i]['x'],self.p[i]['y'],10,10)
            textSize(12)
            fill('#FFF827')
            text(self.p[i]['num'],self.p[i]['x'],self.p[i]['y']-5)
        #если сфера силы
        if len(self.p) > 0:
            if self.p[0]['y'] >= 800:
                del self.p[0]
        #если сфера силы касается головы змейки, то изменяем длину змейки
        for i in range(len(self.p)):
            if self.p[i]['y'] >= 460 and self.p[i]['y'] <= 540 and self.p[i]['x'] >= head_X - 40 and self.p[i]['x'] <= head_X + 40:
                snake.dlina(self.p[i]['num'])
                del self.p[i]
                return ' '
    #передвигаем сферу силы
    def move(self):
        for i in range(len(self.p)):
            if prep.polog_Y() < 360 or prep.polog_Y() > 370:
                self.p[i]['y'] += upgrade_dict['speed'][0]
    #добавляем сферу силы
    def plus_ball(self):
        if dict_int['esc'] == False:
            x = floor(random(0,1000))
            y = floor(random(0,7))
            if x == 1:
                self.p.append(dict(x = random(10,590),y = -15,num = floor(random(100,1000)),gold = 1))
            if x != 1 and y == 0:
                self.p.append(dict(x = random(10,590),y = -15,num = floor(random(-30,-5)),gold = 0))
            else:
                self.p.append(dict(x = random(10,590),y = -15,num = floor(random(1,10)),gold = 0))
    #удаляем сферы силы
    def ball_clear(self):
        for i in range(len(self.p)):
            del self.p[0]
#Змейка  
class Snake:
    def __init__(self,x_,y_,d,n):
        self.d = d
        self.n = n
        self.p = []
        self.rgb_ = False
        self.rgb_fill = 0
        for i in range(n):
            self.p.append(dict(x = x_,y = y_,R = 255,G = 255,B = 255,rgb = False))
    #установка цвета
    def fill_(self,r,g,b):
        for i in range(len(self.p)):
            if mousePressed == 1:
                if mouseX / kof >= 390 and mouseX / kof <= 410 and mouseY / kof > self.p[i]['y'] - 7 and mouseY / kof < self.p[i]['y'] + 7:
                    self.p[i]['R'] = r
                    self.p[i]['G'] = g
                    self.p[i]['B'] = b
    #установка цвета
    def _fill_(self,rgb):
        if rgb != False:
            for i in range(self.n):
                self.rgb_ = rgb + i
                self.p[i]['rgb'] = rgb + i
        else:
            self.rgb_ = False
            for i in range(self.n):
                self.p[i]['rgb'] = 255
    def draw_(self):
        global palette
        push()
        strokeWeight(1)
        if dict_int['iridescent colors'] == True:
            #делаем цвет переливающимся
            for i in range(self.n):
                self.p[i]['rgb'] = self.rgb_fill + i
            self.rgb_fill += 1
            if self.rgb_fill >= 360:
                self.rgb_fill = 0
            colorMode(HSB, 360, 100, 100)
            #рисуем змейку
            if self.n <= 40:
                for i in range(self.n):
                    fill(self.p[self.n-1-i]['rgb'], 100, 100)
                    circle(self.p[self.n-1-i]['x'],self.p[self.n-1-i]['y'],self.d)
            else:
                for i in range(40):
                    fill(self.p[40-1-i]['rgb'], 100, 100)
                    circle(self.p[40-1-i]['x'],self.p[40-1-i]['y'],self.d)
        else:
            colorMode(RGB, 255, 255, 255)
            #рисуем змейку
            if self.n <= 40:
                for i in range(self.n):
                    fill(self.p[self.n-1-i]['R'], self.p[self.n-1-i]['G'], self.p[self.n-1-i]['B'])
                    circle(self.p[self.n-1-i]['x'],self.p[self.n-1-i]['y'],self.d)
            else:
                for i in range(40):
                    fill(self.p[40-1-i]['R'], self.p[40-1-i]['G'], self.p[40-1-i]['B'])
                    circle(self.p[40-1-i]['x'],self.p[40-1-i]['y'],self.d)
        textSize(10)
        #пишем длинну змейки
        if dict_int['palette'] == False and dict_int['shop'] == False:
            text(self.n,self.p[0]['x'],self.p[0]['y']-10)
        pop()
    #передвижение
    def move_to(self,x,y):
        self.p[0]['x'] = x
        self.p[0]['y'] = y
        self.head_to_gran()
        self.move_tail()
    #передвижение
    def move(self,dx,dy):
        self.p[0]['x'] += dx
        self.p[0]['y'] += dy
        self.head_to_gran()
        self.move_tail()
    #голова от границы
    def head_to_gran(self):
        global gran_left,gran_right
        if self.p[0]['x'] <= gran_left + 7.5:
            self.p[0]['x'] = gran_left + 7.5
        if self.p[0]['x'] >= gran_right - 7.5:
            self.p[0]['x'] = gran_right - 7.5
    #увеличение/уменьшение длины
    def dlina(self,d):
        self.n += d
        if d > 0:
            for i in range(d):
                self.p.append(dict(x = 300,y = 1000,R = 255,G = 255,B = 255))
    #увеличение/уменьшение длины
    def dlina_to(self,d):
        self.n = d
    #передвижение тела
    def move_tail(self):
        #по формуле вычисляем куда сдвинуть тело змейки
        for i in range(1,self.n):
            dx = self.p[i]['x'] - self.p[i-1]['x']
            dy = self.p[i]['y'] - self.p[i-1]['y']
            d = sqrt(dx**2 + dy**2)
            if self.d < d:
                self.p[i]['x'] = (self.d / d) * (self.p[i]['x'] - self.p[i-1]['x']) + self.p[i-1]['x']
                self.p[i]['y'] = (self.d / d) * (self.p[i]['y'] - self.p[i-1]['y']) + self.p[i-1]['y']
    #движение змейки
    def scroll_tail_Y(self,dy):
        for i in range(1,self.n):
            self.p[i]['y'] += dy
    #длина змейки
    def get_n(self):
        return self.n
    #координаты головы X
    def head_X(self):
        return self.p[0]['x']

#Препятствия
class Prep:
    def __init__(self):
        self.del_index = 5
        self.prep = []
        self.graniza = 0
    #регенерация препятствий
    def recovery_prep(self):
        global score
        self.del_index = 5
        self.prep = []
        for i in range(5):
            self.prep.append(dict(x = 120*i,y = -120,num = floor(random(3,40))))      
    #передвижение препятствий    
    def move_prep(self,get_n,head):
        global gran_left,gran_right,score
        #если змейка сломала препятствие, то создаём границы
        if self.prep[0]['y'] > 380 and self.prep[0]['y'] < 530 and self.del_index < 5:
            gran_left = self.prep[self.del_index]['x']
            gran_right = self.prep[self.del_index]['x'] + 120
        else:
            gran_left = 0
            gran_right = 600
        strokeWeight(10)
        dict_int['prep_Y'] = self.prep[0]['y'] + 120
        #если ничего не сломано
        if self.del_index == 5:
            for i in range(len(self.prep)):
                #если пуля змейки касается препятствия
                if self.prep[i]['y'] < 365:
                    if cartridge.Y_cartridges() <= self.prep[0]['y'] + 200:
                        if cartridge.Y_cartridges() <= self.prep[0]['y']:
                            if self.prep[i]['x'] <= cartridge.X_cartridges():
                                if self.prep[i]['x'] + 120 >= cartridge.X_cartridges():
                                    self.prep[i]['num'] -= upgrade_dict['punching'][0]
                                    dict_int['score'] += upgrade_dict['bonus'][0]
                                    cartridge.del_cart()
                #если голова змейки касается препятствия
                else:
                    if get_n > 0 and self.prep[i]['x'] <= head and self.prep[i]['x'] + 120 >= head:
                        self.prep[i]['num'] -= upgrade_dict['punching'][0]
                        dict_int['score'] += upgrade_dict['bonus'][0]
                        #если неуязвимость не включена
                        if dict_int['invul'] == False:
                            snake.dlina(-1)
                #рисуем препятствия
                if self.prep[i]['num'] > 0 and i != self.del_index:
                    fill("#34FFFD")
                    rect(self.prep[i]['x'],self.prep[i]['y'],120,120)
                    fill(0)
                    text(self.prep[i]['num'],self.prep[i]['x']+60,self.prep[i]['y']+60)
                else:
                    self.del_index = i
        else:
            #рисуем препятствия
            for i in range(len(self.prep)):
                if self.prep[i]['num'] > 0:
                    fill("#34FFFD")
                    rect(self.prep[i]['x'],self.prep[i]['y'],120,120)
                    fill(0)
                    text(self.prep[i]['num'],self.prep[i]['x']+60,self.prep[i]['y']+60)
            #удаляем препятствия если они вышли за пределы экрана
            if self.prep[0]['y'] >= 800 * kof:
                self.recovery_prep()
        if snake.get_n() <= 0:
            for i in range(len(self.prep)):
                self.del_index = i  
    #положение препятствий по Y
    def polog_Y(self):
        return self.prep[0]['y']
    #передвижение
    def move(self):
        for i in range(len(self.prep)):
            if self.del_index == 5:
                if self.prep[i]['y'] < 365:
                    self.prep[i]['y'] += upgrade_dict['speed'][0]
            else:
                self.prep[i]['y'] += upgrade_dict['speed'][0]
#создаём объекты всех классов
snake = Snake(300,600,15,40)
prep = Prep()
background_ = [0,0,0]
ball = Ball()
lava = lava()
Button_palette = button_palette()
shop = button_shop()
cartridge = cartridges()
esc = esc()
button = Button()
boss = Boss()
boss_cartridges = Boss_cartridges()
time_boss = 0
invul = invulnerability()
#начало
def setup():
    global immage,kof
    #загружаем все картинки
    immage = [loadImage("fon.png"),loadImage("fire.jpg"),loadImage("boss.png"),loadImage("pulya1.png"),loadImage("magazin.png"),loadImage("shield.png")]
    #устанавливаем размер экрана
    size(X_size,Y_size)
    background(255)
    textSize(20)
    #делаем, чтобы текст отображался по середине кнопки
    textAlign(CENTER, BOTTOM)
    #устанавливаем колличество кадров в секунду 100
    frameRate(100)
#основная часть
def draw():
    global start,immage,background_,i,palette,m,time_boss
    background(background_[0],background_[1],background_[2])
    #рисуем фон
    image(immage[0],0,0,600,800)
    scale(kof)
    fill(255)
    textSize(25)
    if dict_int['boss'] == False:
        text('money:',300,25)
        text(dict_int['score'],300,50)
    dict_int['snake_head_X'] = mouseX / kof
    invul.plus()
    #передвижение
    if dict_int['start'] == True and dict_int['esc'] == False:
        lava.move()
        ball.move()
        prep.move()
    #действия
    if dict_int['start'] == True:
        invul.draw_()
        ball.draw_ball(snake.head_X())
        lava.draw_lava(snake.head_X())
        snake.draw_()
        snake.scroll_tail_Y(upgrade_dict['speed'][0])
        if mousePressed == True and dict_int['esc'] == False:
            snake.move_to(mouseX / kof,500)
        else:
            snake.move_tail()
        textSize(20)
        prep.move_prep(snake.get_n(),snake.head_X())
        strokeWeight(1)
        cartridge.draw_()
        fill(255-background_[0],255-background_[1],255-background_[2])
        #лава и сферы силы
        if i % (90 / upgrade_dict['speed'][0]) == 0:
            ball.plus_ball()
            lava.plus_lava()
        #босс
        if time_boss >= 1000 and time_boss <= 5000:
            boss.draw_()
            boss_cartridges.draw_()
            dict_int['boss'] = True
        else:
            dict_int['boss'] = False
        if time_boss >= 5000:
            time_boss = 0
        time_boss += 1
        esc.draw_()
        i += 1
    else:
        i = 1
        dict_int['boss'] = False
    #если длина змейки 0, то завершаем игру
    if snake.get_n() <= 0:
        dict_int['start'] = False
    #рисуем кнопки
    if dict_int['start'] == False and dict_int['palette'] == False and dict_int['shop'] == False:
        button.draw_()
    #рисуем кнопку выхода из магазина или палитры
    if dict_int['palette'] == True or dict_int['shop'] == True:
        fill(255,0,0)
        strokeWeight(1)
        rect(500,0,100,60)
        fill(0)
        textSize(20)
        text('BACK',550,40)
        if dict_int['palette'] == True:
            Button_palette.palette()
        else:
            shop.draw_()
    #рисуем кнопку получения денег 
    if mousePressed == True:
        if dict_int['start'] == False and mouseX > 0 and mouseX < 100 * kof and mouseY > 0 and mouseY < 60 * kof and dict_int['palette'] == False and dict_int['shop'] == False:
            dict_int['score'] += 10000000
#функция на проверку нажатия мышки
def mousePressed():
    global start,palette
    #если нажата кнопка выйти из магазина, то выходим из магазина
    if dict_int['start'] == False and mouseX > 500 * kof and mouseX < 600 * kof and mouseY > 0 and mouseY < 60 * kof and dict_int['shop'] == True:
        snake.dlina_to(40)
        dict_int['shop'] = False
    #если нажата кнопка магазин, то заходим в магазин
    if dict_int['start'] == False and mouseX > 500 * kof and mouseX < 575 * kof and mouseY > 700 * kof and mouseY < 775 * kof and dict_int['shop'] == False:
        dict_int['shop'] = True
        shop.draw_()
        snake.dlina_to(20)
    #если нажата кнопка палитра, то заходим в палитру
    if dict_int['start'] == False and mouseX > 25 * kof and mouseX < 100 * kof and mouseY > 700 * kof and mouseY < 775 * kof:
        dict_int['palette'] = True
        snake.dlina_to(40)
    #если нажата кнопка выйти из палитры, то выходим из палитры
    if dict_int['start'] == False and mouseX > 500 * kof and mouseX < 600 * kof and mouseY > 0 and mouseY < 60 * kof and dict_int['palette'] == True:
        dict_int['palette'] = False
        snake.dlina_to(40)
    #если нажата кнопка старт, то начинаем игру
    if dict_int['start'] == False and mouseX > 200 * kof and mouseX < 400 * kof and mouseY > (400 - 62.5) * kof and mouseY < (400 + 62.5) * kof and dict_int['palette'] == False and dict_int['shop'] == False:
        button_start()
