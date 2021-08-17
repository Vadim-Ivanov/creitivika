dlina_x = 1440
dlina_y = 820
class Pole:
    def __init__(self):
        self.r = 20
        self.pol = []
        for i in range(dlina_x / self.r):
            for j in range(dlina_y / self.r):
                self.pol.append(floor(random(0,7)) * 20)
        self.x = (20 * 10) - 10
        self.y = (20 * 10) - 10
        self.time = True
    def draw_(self):
        push()
        colorMode(HSB,360,100,100)
        for i in range(width / self.r):
            for j in range(height / self.r):
                fill(self.pol[i * (height / self.r) + j],100,100)
                rect(i * self.r,j * self.r,self.r,self.r)
                fill(0)
                text(self.pol[i * (height / self.r) + j] / 20,i * self.r + 10,j * self.r - 10)
                fill(0,0,255)
                ellipse(self.x,self.y,10,10)
                if keyPressed == True and self.time == True:
                    if keyCode == UP: 
                        if self.pol[(self.y - 30) / 20 + (self.x - 10) / 20] - self.pol[((self.y - 30) / 20 + (self.x - 10) / 20) - (width / self.r)] >= -20:
                            if self.pol[(self.y - 30) / 20 + (self.x - 10) / 20] - self.pol[((self.y - 30) / 20 + (self.x - 10) / 20) - (width / self.r)] <= 20:
                                self.y -= 20
                    if keyCode == DOWN:
                        self.y += 20
                    if keyCode == RIGHT:
                        self.x += 20
                    if keyCode == LEFT:
                        self.x -= 20
                    self.time = False
                if keyPressed == False:
                    self.time = True
        pop()

# class Player:
#     def __init__(self):
#         self.x = (20 * 10) - 10
#         self.y = (20 * 10) - 10
#         self.time = True
#     def draw_(self):
#         fill(0,0,255)
#         ellipse(self.x,self.y,10,10)
#         if keyPressed == True and self.time == True:
#             if keyCode == UP:
#                 self.y -= 20
#             if keyCode == DOWN:
#                 self.y += 20
#             if keyCode == RIGHT:
#                 self.x += 20
#             if keyCode == LEFT:
#                 self.x -= 20
#             self.time = False
#         if keyPressed == False:
#             self.time = True
pole = Pole()
#player = Player()
def setup():
    size(1440,820) 
    noStroke()
    textAlign(CENTER)
    textSize(10)
def draw():
    pole.draw_()
    #player.draw_()
