#inf = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
city = [[float('inf'), 20, 18, 12, 8],
        [5, float('inf'), 14, 7, 11],
        [12, 18, float('inf'), 6, 11],
        [11, 17, 11, float('inf'), 12],
        [5, 5, 5, 5, float('inf')]]
city_col = []
# for i in range(len(city[0])):
#     city_col.append([])
#     for j in range(len(city)):
#         city_col[i].append(city[j][i])
column = []
stroka = []
def city_col_app():
    for i in range(len(city[0])):
        city_col.append([])
        for j in range(len(city)):
            city_col[i].append(city[j][i])
    
def str_const():
    global column, stroka
    stroka = []
    for i in range(len(city)):
        stroka.append(min(city[i]))
        
def col_const():
    global column, stroka, city_col
    column = []
    city_col_app()
    for i in range(len(city)):
        column.append(min(city_col[i]))
        
def minus_str_const():
    for i in range(len(city)):
        for j in range(len(city[i])):
            city[i][j] -= stroka[i]
            
def minus_col_const():
    for i in range(len(city)):
        for j in range(len(city[i])):
            city[j][i] -= column[i]

def sum_col_str():
    global column, stroka, H
    H = 0
    for i in range(len(stroka)):
        H += column[i] + stroka[i]
        
def evaluation_of_zero_cells():
    global evaluation_zero
    city_col_app()
    evaluation_zero = []
    gor = []
    vert = []
    min_gor = 0
    min_vert = 0
    for i in range(len(city)):
        for j in range(len(city_col)):
            if city[i][j] == 0:
                gor = city[i]
                del gor[j]
                min_gor = min(gor[i])
            if city_col[j][i] == 0:
                vert = city[i]
                del vert[j]
                min_vert = min(vert[i])
            if city[i][j] == 0:
                evaluation_zero.append(min_gor + min_vert)
            else:
                evaluation_zero.append(float('inf'))
    print(evaluation_zero)
                
            
def setup():
    global city,city_col,column,stroka
    size(600,400)
    str_const()
    minus_str_const()
    col_const()
    minus_col_const()
    sum_col_str()
    evaluation_of_zero_cells()
def draw():
    pass
