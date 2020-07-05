from backstage import*


# 读取三条线路信息

road_1 = [[], [], []] # 己方的小兵 第三阶的dict代表（兵种，个数）
road_2 = [[], [], []] # 地方的小兵


'''
tower_1 
tower_2 
'''


# 初始化路径信息
def init_soldier():
    for i in range(69):
        road_1[0].append({'Knight': 0, 'Archer': 0})
        road_1[2].append({'Knight': 0, 'Archer': 0})
        road_2[0].append({'Knight': 0, 'Archer': 0})
        road_2[2].append({'Knight': 0, 'Archer': 0})

    for i in range(49):
        road_1[1].append({'Knight': 0, 'Archer': 0})
        road_2[1].append({'Knight': 0, 'Archer': 0})
    print(road_1, "\n", road_2) 



def save_soldier():
    for i in range(3):
        for k in range(len(w1[i])):
            if w1[i][k].wtype == 2:
                road_1[i][w1[i][k].pos]['Knight'] += 1
            if w1[i][k].wtype == 3:
                road_1[i][w1[i][k].pos]['Archer'] += 1
        for k in range(len(w2[i])):
            if w2[i][k].wtype == 2:
                road_2[i][w2[i][k].pos]['Knight'] += 1
            if w1[i][k].wtype == 3:
                road_2[i][w2[i][k].pos]['Archer'] += 1
        


