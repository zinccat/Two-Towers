import queue


# 重置函数, 开启新一局游戏时调用


def reset():

    for i in range(3):

        w1[i].clear()

        w2[i].clear()


# 包含Warrior的列表
w1 = [[], [], []]  # 分别对应左中右路

w2 = [[], [], []]


ops1 = queue.PriorityQueue()

ops2 = queue.PriorityQueue()


class Command:

    """命令类

    包含四个参数:

    turnID:该命令所生效的回合

    playerID:发出该命令的玩家,可以取1 or 2

    CmdType:指令的类型,用于指导CmdStr的读取方式

    CmdStr:指令的内容，是一个列表

    """

    def __init__(self, turnID, playerID, CmdType, CmdStr):

        self.turnID = turnID

        self.playerID = playerID

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

    # 命令读取函数

    def ReadCmd(CmdList):

        for op in CmdList

        # 这里我写

    # 士兵对战判断函数

    def BattleCheck(WarriorList1, WarriorList2):

        for i in range(3):

            TempList1 = WarriorList1[i]

            TempList2 = WarriorList2[i]

            for TempWarrior1 in TempList1:

                for TempWarrior2 in TempList2:

                    if TempWarrior1.wType == 0 and -10 <= TempWarrior1.pos-TempWarrior2.pos <= 10:

                        BattleSet.append(Battle(TempWarrior1, TempWarrior2))


                    if TempWarrior1.wType == 1 and -8 <= TempWarrior1.pos-TempWarrior2.pos <= 8:

                        BattleSet.append(Battle(TempWarrior1, TempWarrior2))


                    if TempWarrior1.wType == 2 and -1 <= TempWarrior1.pos-TempWarrior2.pos <= 1:

                        BattleSet.append(Battle(TempWarrior1, TempWarrior2))


                    if TempWarrior1.wType == 3 and -5 <= TempWarrior1.pos-TempWarrior2.pos <= 5:

                        BattleSet.append(Battle(TempWarrior1, TempWarrior2))


                    if TempWarrior2.wType == 0 and -10 <= TempWarrior1.pos-TempWarrior2.pos <= 10:
                        BattleSet.append(Battle(TempWarrior2, TempWarrior1))


                    if TempWarrior2.wType == 1 and -8 <= TempWarrior1.pos-TempWarrior2.pos <= 8:
                        BattleSet.append(Battle(TempWarrior2, TempWarrior1))


                    if TempWarrior2.wType == 2 and -1 <= TempWarrior1.pos-TempWarrior2.pos <= 1:

                        BattleSet.append(Battle(TempWarrior2, TempWarrior1))


                    if TempWarrior2.wType == 3 and -5 <= TempWarrior1.pos-TempWarrior2.pos <= 5:

                        BattleSet.append(Battle(TempWarrior2, TempWarrior1))





    # 战斗进行函数

    def BattleRun(BattleList):



        while BattleList:



            TempBattle=BattleList.pop(0)

            TempBattle.BattleGo()



    # 主塔阵亡函数

    def BaseDeath(WarriorList1, WarriorList2):

        sumAttack1=0

        for i in range(3):

            sumAttack1 += INF-WarriorList1[i][0].wLife

        if sumAttack1 >= InitBaseLife:

            # 向玩家2显示ta胜利

         sumAttack2=0

        for i in range(3):

            sumAttack2 += INF-WarriorList2[i][0].wLife

        if sumAttack2 >= InitBaseLife:

            # 向玩家1显示ta胜利




    # 士兵阵亡函数

    def WarriorDeath(WarriorList):



        for i in range(3):

            for j in range(len(WarriorList[i])):



                if WarriorList[i][j].wLife <= 0:

                    WarriorList[i].pop(j)





    # 士兵移动函数

    def WarriorMove():
