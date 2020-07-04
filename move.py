import warrior
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
    # 若前方有足够位置就前进
    WarriorList.sort(key=lambda student: student[2])
    for i in WarriorList:
        if i.mCD == 0 and not i.attacked and posDict.get(i.pos + 1, 0) <= 3:
            i.pos += 1

'''
# WarriorMove测试代码
l = []
l.append(warrior.Archer(1, 2))
l.append(warrior.Archer(1, 2))
l.append(warrior.Archer(1, 2))
l.append(warrior.Archer(1, 2))
for i in range(3):
    l[i].pos = 1
WarriorMove(l)
for i in range(4):
    print(l[i].pos)
'''
