import warrior
from config import *
# 士兵移动函数


def WarriorMove(WarriorList):
    posDict = dict()
    # 第一轮扫描完成各位置上对象的计数
    for i in WarriorList:
        if posDict.get(i.pos, 0) == 0:
            posDict[i.pos] = 1
        else:
            posDict[i.pos] += 1
    print(posDict)
    # 若前方有足够位置就前进, 先排序避免堵车
    WarriorList.sort(key=lambda Warrior: Warrior.pos,
                     reverse=(WarriorList[0].wTeam == 1))
    # 友方移动量为1
    mov = 1
    # 敌方移动量为-1
    if WarriorList[0].wTeam == 2:
        mov = -1
    for i in WarriorList:
        print(i.pos)
        if i.mCD == 0 and not i.attacked and posDict.get(i.pos + 1, 0) < 3:
            posDict[i.pos] -= 1
            i.pos += mov


'''
# WarriorMove测试代码
l = []
l.append(warrior.Archer(1, 2))
l.append(warrior.Archer(1, 2))
l.append(warrior.Archer(1, 2))
l.append(warrior.Archer(1, 2))
for i in range(1, 4):
    l[i].pos = mLen-1
WarriorMove(l)
for i in range(4):
    print(l[i].pos)
'''
