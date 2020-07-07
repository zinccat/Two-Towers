import queue

from config import *

from warrior import *

from socket import *

import threading

import sys

import json

import re
from time import sleep


# 此处定义了游戏所用到的全局变量

#HOST = '65.49.209.247'

HOST = 'localhost'

PORT = 8023

BUFSIZE = 1024  # 缓冲区大小  1K

ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)

userAccount = None

target = ['']

game = ''

# 连接到服务器并注册

def connect():

    try:

        tcpCliSock.connect(ADDR)

        print('Connected with server')

        while True:

            reg = register()

            if reg:

                break

    except:

        print('error')

        sys.exit(0)

    global target

    target[0] = input('想打谁? ')

    # 这里还需添加是否与对手连接成功


class Command:

    """命令类
    包含四个参数:
    turnID:该命令所生效的回合
    CmdType:指令的类型,用于指导CmdStr的读取方式
    CmdStr:指令的内容，是一个列表
    """

    def __init__(self, turnID, CmdType, CmdStr):

        self.turnID = turnID

        self.CmdType = CmdType

        self.CmdStr = CmdStr

    # 比较函数,确定执行命令的优先级, 目前仅考虑回合先后

    def __lt__(self, other):

        return self.turnID < other.turnID


# 将本机注册到服务器


def register():

    account = input('Please input your account: ')

    global userAccount

    userAccount = account

    regInfo = [account, 'register']

    datastr = json.dumps(regInfo)

    tcpCliSock.send(datastr.encode('utf-8'))

    data = tcpCliSock.recv(BUFSIZE)

    data = data.decode('utf-8')

    if data == '0':

        print('Success to register!')

        return True

    else:

        print('Failed for exceptions!')

        return False


# 这是一个发送指令的接口, 可以直接调用以向对手的命令队列发送指令


def sendOp(target, op):

    #turnID, CmdType, CmdStr, optype

    dataObj = {'froms': userAccount, 'to': target,

               'turnID': op.turnID, 'CmdType': op.CmdType, 'CmdStr': op.CmdStr}

    datastr = json.dumps(dataObj)

    try:

        tcpCliSock.send(datastr.encode('utf-8'))

    except:

        print('awsl')


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

    def __lt__(self, other):

        return self.turnID < other.turnID


class Battle:

    """战斗类"""

    def __init__(self, WarriorAttack, WarriorDefence):

        self.WarriorAttack = WarriorAttack

        self.WarriorDefence = WarriorDefence

    def BattleGo(self):

        if self.WarriorDefence.wLife > 0:

            # 只有在对方没死的时候才会攻击并更新aCD

            self.WarriorAttack.updateaCD(1)

            self.WarriorDefence.wLife -= self.WarriorAttack.wAttack


class Action:

    def __init__(self):

        # 回合数记录

        self.turnID = 0

        # 用于计算金钱补给

        self.timeCount = 0

        self.money = 0

        # 包含Warrior的列表

        self.w1 = [[], [], []]  # 分别对应左中右路

        self.w2 = [[], [], []]

        # 更新血量数值

        self.life = [0, 0, 0, 0, 0, 0, 0, 0]

        # 建立一个战斗列表

        self.BattleList = []

        # 指令集

        self.ops1 = queue.PriorityQueue()

        self.ops2 = queue.PriorityQueue()

        # 初始化己方主塔和防御塔

        for i in range(3):

            self.w1[i].append(Base(1, 0, 0))

            self.w1[i].append(Turret(1, 2, dLen))

        # 初始化对方主塔和防御塔

        for i in range(3):

            if i == 1:

                self.w2[i].append(Base(2, 0, mLen))

                self.w2[i].append(Turret(2,  2, mLen - dLen))

            else:

                self.w2[i].append(Base(2, 0, aLen))

                self.w2[i].append(Turret(2, 2, aLen - dLen))

    # 打钱!

    def MoneyAccumulate(self, x):

        self.money += x

    """行动系统"""

    # 重置函数, 开启新一局游戏时调用

    def reset(self):

        self.turnID = 0

        self.money = 0

        self.BattleList.clear()

        while not self.ops1.empty():

            self.ops1.get()

        while not self.ops2.empty():

            self.ops2.get()

        for i in range(3):

            self.w1[i].clear()

            self.w2[i].clear()

        self.__init__()

    # 回合初状态更新

    def update(self):

        self.turnID += 1

        # 金钱更新

        if self.money < 10:

            self.timeCount += 1

            if self.timeCount == 60:

                self.MoneyAccumulate(1)

                self.timeCount = 0

        # 武士状态刷新

        for i in range(3):

            for w in self.w1[i]:

                w.attacked = False  # 重置攻击状态

                w.updatemCD(0)  # 更新mCD

                w.updateaCD(0)  # 更新aCD

                if w.wType == 1:  # Turret

                    self.life[i + 1] = w.wLife

        for i in range(3):

            for w in self.w2[i]:

                w.attacked = False  # 重置攻击状态

                w.updatemCD(0)  # 更新mCD

                w.updateaCD(0)  # 更新aCD

                if w.wType == 1:  # Turret

                    self.life[i + 5] = w.wLife

    # 收取命令

    class getCmd(threading.Thread):

        def __init__(self, game):
            threading.Thread.__init__(self)
            self.ops2 = game.ops2

        # 为了处理ops2不存在的问题

        def run(self):

            while True:

                try:

                    data = tcpCliSock.recv(BUFSIZE).decode('utf-8')

                    if data == '-1':

                        print('can not connect to target!')

                        break

                    else:
                        dataObj = json.loads(data)
                        print('{} ->{} : {} {} {}'.format(

                            dataObj['froms'], userAccount, dataObj['turnID'], dataObj['CmdType'], dataObj['CmdStr']))

                        t = Command(dataObj['turnID'], dataObj['CmdType'], dataObj['CmdStr'])
                        self.ops2.put(t)
                        print(123)
                except:
                    pass

    # 命令读取函数

    # SideWarriorList为某一方的总list

    # team为1 友方, 2 敌方

    def ReadCmd(self):

        genNum = 0  # 本回合生成了几个warrior?

        while(not self.ops1.empty()):

            tempOp = self.ops1.get()  # ops为命令队列

            if self.turnID == tempOp.turnID:

                if tempOp.CmdType == 2:  # 骑士

                    genNum += 1

                    tempObj = Knight(1, genNum, 0)

                    self.w1[int(tempOp.CmdStr[0]-1)].append(tempObj)

                if tempOp.CmdType == 3:  # 弓箭手

                    genNum += 1

                    tempObj = Archer(1, genNum, 0)

                    self.w1[int(tempOp.CmdStr[0]-1)].append(tempObj)

            else:

                # 时机未到

                self.ops1.put(tempOp)

                break

        genNum = 0  # 本回合生成了几个warrior?

        while(not self.ops2.empty()):

            tempOp = self.ops2.get()  # ops为命令队列

            if self.turnID == tempOp.turnID:

                if tempOp.CmdType == 2:  # 骑士

                    genNum += 1

                    tempObj = Knight(2, genNum, mLen if tempOp.CmdStr[0] == 2 else aLen)
                    self.w2[int(tempOp.CmdStr[0]-1)].append(tempObj)
                if tempOp.CmdType == 3:  # 弓箭手

                    genNum += 1

                    tempObj = Archer(
                        2, genNum, mLen if tempOp.CmdStr[0] == 2 else aLen)

                    self.w2[int(tempOp.CmdStr[0]-1)].append(tempObj)
            else:

                # 时机未到

                self.ops2.put(tempOp)

                break

    # 士兵对战判断函数

    def BattleCheck(self):

        for i in range(3):

            for Warrior1 in self.w1[i]:

                for Warrior2 in self.w2[i]:

                    if abs(Warrior1.pos - Warrior2.pos) <= Warrior1.wRange:
                        Warrior1.attacked = True
                        self.BattleList.append(Battle(Warrior1, Warrior2))
                    if abs(Warrior1.pos - Warrior2.pos) <= Warrior2.wRange:
                        Warrior2.attacked = True
                        self.BattleList.append(Battle(Warrior2, Warrior1))
        

    # 战斗进行函数

    def BattleRun(self, BattleList):

        while BattleList:

            TempBattle = BattleList.pop(0)

            TempBattle.BattleGo()

    # 主塔阵亡函数

    def BaseDeath(self):

        sumAttack2 = 0

        for i in range(3):

            for w in self.w2[i]:

                if w.wType == 0:

                    sumAttack2 += INF - w.wLife

                    break

        self.life[4] = max(0, TrueBaseLife - sumAttack2)

        if sumAttack2 >= TrueBaseLife:

            # 向玩家1显示ta胜利

            # 士兵阵亡函数

            return 1

        sumAttack1 = 0

        for i in range(3):

            for w in self.w1[i]:

                if w.wType == 0:

                    sumAttack1 += INF - w.wLife

        self.life[0] = max(0, TrueBaseLife - sumAttack1)

        if sumAttack1 >= TrueBaseLife:

            # 向玩家2显示ta胜利

            return 2

        return 0

    def WarriorDeath(self):

        for i in range(3):

            for w in self.w1[i]:

                if w.wLife <= 0:

                    if w.wType == 1:

                        print('防御塔被攻陷!')

                        self.life[i + 1] = 0

                    self.w1[i].remove(w)

        for i in range(3):

            for w in self.w2[i]:

                if w.wLife <= 0:

                    if w.wType == 1:

                        print('防御塔被攻陷!')

                        self.life[i + 5] = 0

                    self.w2[i].remove(w)

    # 士兵移动函数

    def WarriorMove(self, WarriorList, posOccu, team):

        posDict = dict()

        # 第一轮扫描完成各位置上对象的计数

        for i in WarriorList:

            posDict[(i.pos, i.wGrid)] = True

            posOccu[i.pos] = team

        # 若前方有足够位置就前进, 先排序避免堵车

        WarriorList.sort(key=lambda Warrior: Warrior.pos,

                         reverse=(WarriorList[0].wTeam == 1))

        # 友方移动量为1

        mov = 1

        # 敌方移动量为-1

        if WarriorList[0].wTeam == 2:

            mov = -1

        for i in WarriorList:

            if i.mCD == 0 and not i.attacked and i.wType > 1:  # 塔不能跑!

                for j in range(1, 4):

                    if posDict.get((i.pos + mov, j), 0) == False and posOccu.get(i.pos + mov, team) == team:

                        posDict[(i.pos, i.wGrid)] = False

                        i.pos += mov

                        posDict[(i.pos, j)] = True

                        posOccu[i.pos] = team

                        i.wGrid = j

                        i.updatemCD(1)

                        break

    def end(self, result):

        if result == 1:

            print('你赢了!')

        elif result == 2:

            print('你挂了!')


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
WarriorMove(l)for i in range(4):
    print(l[i].pos)

'''

