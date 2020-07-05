import queue
from config import *
from warrior import *

# 重置函数, 开启新一局游戏时调用


def reset():
    turnID = 0
    for i in range(3):
        w1[i].clear()
        w2[i].clear()


# 回合数记录
turnID = 0

# 包含Warrior的列表
w1 = [[], [], []]  # 分别对应左中右路
w2 = [[], [], []]


ops1 = queue.PriorityQueue()
ops2 = queue.PriorityQueue()


class Command:

    """命令类
    包含四个参数:
    turnID:该命令所生效的回合
    # 已删除 直接归类到己方和敌方列表即可 playerID:发出该命令的玩家,可以取1 or 2
    CmdType:指令的类型,用于指导CmdStr的读取方式
    CmdStr:指令的内容，是一个列表
    """

    def __init__(self, turnID, CmdType, CmdStr):

        self.turnID = turnID
        self.CmdType = CmdType
        self.CmdStr = CmdStr

    # 比较函数,确定执行命令的优先级
    def __cmp__(self, other):

        return self.turnID < other.turnID


# 建立一个由Command构成的列表，作为指令集


CmdSet = []

class Battle:
    """战斗类"""
    def __init__(self, WarriorAttack, WarriorDenfence):
        self.WarriorAttack = WarriorAttack
        self.WarriorDenfence = WarriorDenfence
    def BattleGo(self):
        self.WarriorDenfence.wLife -= self.WarriorAttack.wAttack


# 建立一个战斗列表


BattleSet = []


class Action:

    """行动系统"""

    # 回合初状态更新
    def update(self, SideWarriorList):
        global turnID
        turnID += 1
        for i in range(3):
            for w in SideWarriorList[i]:
                w.attacked = 0  # 重置攻击状态
                w.updatemCD()  # 更新mCD
                w.updateaCD()  # 更新aCD

    # 命令读取函数

    # SideWarriorList为某一方的总list
    # team为1 友方, 2 敌方
    def ReadCmd(self, CmdList, SideWarriorList, team):
        genNum = 0  # 本回合生成了几个warrior?
        while(not CmdList.empty()):
            tempOp = CmdList.get()  # ops为命令队列
            if turnID == tempOp.turnID:
                if tempOp.CmdType == 2:  # 骑士
                    genNum += 1
                    tempObj = Knight(team, genNum)
                    SideWarriorList[int(tempOp.CmdStr[0]-1)].append(tempObj)
                if tempOp.CmdType == 3:  # 弓箭手
                    genNum += 1
                    tempObj = Archer(team, genNum)
                    SideWarriorList[int(tempOp.CmdStr[0]-1)].append(tempObj)
            else:
                # 时机未到
                CmdList.put(tempOp)
                break

    # 士兵对战判断函数

    def BattleCheck(self, WarriorList1, WarriorList2):
        for i in range(3):
            TempList1 = WarriorList1[i]
            TempList2 = WarriorList2[i]
            for TempWarrior1 in TempList1:
                for TempWarrior2 in TempList2:
                    if abs(TempWarrior1.pos-TempWarrior2.pos) <= TempWarrior1.wRange:
                        BattleSet.append(Battle(TempWarrior1, TempWarrior2))

    # 战斗进行函数

    def BattleRun(self, BattleList):
        while BattleList:
            TempBattle = BattleList.pop(0)
            TempBattle.BattleGo()

    # 主塔阵亡函数

    def BaseDeath(self, WarriorList1, WarriorList2):
        sumAttack1 = 0
        for i in range(3):
            sumAttack1 += INF-WarriorList1[i][0].wLife

        if sumAttack1 >= BaseLife:
            # 向玩家2显示ta胜利
            sumAttack2 = 0

        for i in range(3):
            sumAttack2 += INF-WarriorList2[i][0].wLife

        if sumAttack2 >= BaseLife:
            # 向玩家1显示ta胜利
            # 士兵阵亡函数
            pass

    def WarriorDeath(self, WarriorList):
        for i in range(3):
            for j in range(len(WarriorList[i])):
                if WarriorList[i][j].wLife <= 0:
                    WarriorList[i].pop(j)

    # 士兵移动函数

    def WarriorMove(self, WarriorList):
        posDict = dict()
        # 第一轮扫描完成各位置上对象的计数
        for i in WarriorList:
            posDict[(i.pos, i.wGrid)] = True
        # 若前方有足够位置就前进, 先排序避免堵车
        WarriorList.sort(key=lambda Warrior: Warrior.pos,
                         reverse=(WarriorList[0].wTeam == 1))
        # 友方移动量为1
        mov = 1
        # 敌方移动量为-1
        if WarriorList[0].wTeam == 2:
            mov = -1
        for i in WarriorList:
            if i.mCD == 0 and not i.attacked:
                for j in range(1, 4):
                    if posDict[(i.pos + mov, j)]:
                        posDict[(i.pos, i.wGrid)] = False
                        i.pos += mov
                        posDict[(i.pos, j)] = True
                        i.wGrid = j
                        break


'''
# 命令测试
w1 = [[], [], []]
ops = queue.PriorityQueue()
turnID = 1
ops.put(Command(1, 2, [2]))
ReadCmd(ops, w1, 1)
print(w1)
'''


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
