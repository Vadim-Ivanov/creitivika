a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

start = 1, 1
end_ = 2, 5

m = []

def make_step(k):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
           m[i][j+1] = k + 1

k = 0

d = 0
sh = 0
b = False
time = 0
t = False
v = 1
def setup():
    global d,sh,k,m,start,end_,the_path
    size(800,800)
    d = width / 10
    sh = height / 10
    noStroke()
    y_start, x_start = start
    y_end, x_end = end_
    fill(255,0,0)
    rect((x_start * d) + 20, (y_start * sh) + 20,d - 40,sh - 40)
    fill(0,255,0)
    rect((x_end * d) + 20, (y_end * sh) + 20,d - 40,sh - 40)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                fill(0)
                rect(j * d,i * sh,d,sh)
    frameRate(25)
def draw():
    global d,sh,k,m,start,end_,the_path,b,time,t,v

    if mousePressed == True:
        b = True
    if b == True:
        for i in range(len(a)):
            m.append([])
            for j in range(len(a[i])):
                m[-1].append(0)
        i,j = start
        m[i][j] = 1
        
        while m[end_[0]][end_[1]] == 0:
            k += 1
            make_step(k)
        
        i, j = end_
        k = m[i][j]
        the_path = [(i,j)]
        while k > 1:
            if i > 0 and m[i - 1][j] == k-1:
                i, j = i-1, j
                the_path.append((i, j))
                k-=1
            elif j > 0 and m[i][j - 1] == k-1:
                i, j = i, j-1
                the_path.append((i, j))
                k-=1
            elif i < len(m) - 1 and m[i + 1][j] == k-1:
                i, j = i+1, j
                the_path.append((i, j))
                k-=1
            elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
                i, j = i, j+1
                the_path.append((i, j))
                k -= 1
        if len(the_path) - v >= 0:
            fill(0,116,255)
            ellipse((the_path[len(the_path)-v][1] * sh) + 40,(the_path[len(the_path)-v][0] * d) + 40,d - 60,sh - 60)
            v += 1
 
