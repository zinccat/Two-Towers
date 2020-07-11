# -*- coding: utf-8 -*-
# 这是没有GUI欢迎界面的游戏后端, 需安装easygui

from config import *
from warrior import *
from socket import *
import threading
import sys
import json
from time import sleep, time
import queue

# 用于同步
flag = [-1]

# 此处定义了游戏所用到的全局变量
#HOST = '65.49.209.247'
HOST = '62.234.107.120'
#HOST = 'localhost'
PORT = 8026
BUFSIZE = 1024  # 缓冲区大小  1K
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
account = [None]
target = [None]
game = None
clicktime = 0
ide = []
syncTimeCount = [0]

# 无比简单的等待函数 (用于同步)


def waiting():
    while flag[0] <= 0:
        sleep(0.05)
        if syncTimeCount[0] != 0 and time() - syncTimeCount[0] > 10:
            print('对方把网线拔掉了, 你赢了!')
            game.sendCmd(target[0], '', -1)  # 如果对面上线就告诉他他挂了
            sleep(3)
            sys.exit(0)

# 连接到服务器并注册


def connect():
    try:
        tcpCliSock.connect(ADDR)
        print('Connected with server')
        while True:
            msg = "请输入双方id并点击开始游戏"
            while True:
                account[0] = input('你是谁? ')
                target[0] = input('想打谁? ')
                if account[0] == '' or target[0] == '':
                    print('id不能为空!')
                elif account[0] == target[0]:
                    print('不允许 我 打 我 自 己!')
                else:
                    break
            regInfo = [account[0], 'register']
            datastr = json.dumps(regInfo)
            tcpCliSock.send(datastr.encode('utf-8'))
            data = tcpCliSock.recv(BUFSIZE)
            data = data.decode('utf-8')
            if data == '0':
                print('等待对手上线中...')
                break
            else:
                print('失败, 请再试一次')
                continue
    except:
        sys.exit(0)


class Command:

    """命令类
    包含三个参数:
    turnID:该命令所生效的回合
    CmdType:指令的类型,用于指导CmdStr的读取方式
    CmdStr:指令的内容，是一个列表
    """

    # 初始化函数
    def __init__(self, turnID, CmdType, CmdStr):
        self.turnID = turnID
        self.CmdType = CmdType
        self.CmdStr = CmdStr

    # 比较函数,确定执行命令的优先级, 供优先队列使用
    def __lt__(self, other):
        return self.turnID < other.turnID


class Battle:
    """战斗类"""

    # 初始化战斗双方
    def __init__(self, WarriorAttack, WarriorDefence):
        self.WarriorAttack = WarriorAttack
        self.WarriorDefence = WarriorDefence

    # 打起来了, 打起来了
    def BattleGo(self):
        if (self.WarriorAttack.attacked == False) and self.WarriorDefence.wLife > 0:
            # 只有在对方没死的时候才会攻击并更新aCD
            self.WarriorAttack.attacked = True
            self.WarriorAttack.updateaCD(1)
            self.WarriorDefence.wLife -= max(
                1, self.WarriorAttack.wAttack - self.WarriorDefence.wDefence)


class Game:
    """游戏类"""

    # 初始化函数
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

    # 重置函数, 开启新一局游戏时调用
    def reset(self):
        self.turnID = 0
        self.money = 0
        self.timeCount = 0
        self.BattleList.clear()
        while not self.ops1.empty():
            self.ops1.get()
        while not self.ops2.empty():
            self.ops2.get()
        for i in range(3):
            self.w1[i].clear()
            self.w2[i].clear()
        self.__init__()

    # 回合初状态刷新
    def update(self):
        self.turnID += 1
        # 金钱刷新
        if self.money < 10:
            if self.turnID < AccTurn1:
                self.timeCount += 1
            elif self.turnID < AccTurn2 and self.turnID >= AccTurn1:
                self.timeCount += AccSpeed1
            else:
                self.timeCount += AccSpeed2
            if self.timeCount >= 50:
                self.money += 1
                self.timeCount = 0
        else:
            self.timeCount = 0
        # 武士状态刷新
        for i in range(3):
            for w in self.w1[i]:
                w.attacked = False  # 重置攻击状态
                w.updatemCD(0)  # 更新mCD
                w.updateaCD(0)  # 更新aCD
                w.couldMove = True
                if w.wType == 1:  # Turret
                    self.life[i + 1] = w.wLife
        for i in range(3):
            for w in self.w2[i]:
                w.attacked = False  # 重置攻击状态
                w.updatemCD(0)  # 更新mCD
                w.updateaCD(0)  # 更新aCD
                w.couldMove = True
                if w.wType == 1:  # Turret
                    self.life[i + 5] = w.wLife

    # 升级主塔或防御塔 num=0代表升级主塔, n=1-3对应上中下三路防御塔
    def upgrade(self, num, team):
            # 发送指令部分在gameclient里面写
            if team == 1:
                if num == 0:
                    for i in range(3):
                        for w in self.w1[i]:
                            if w.wType == 0:
                                w.wAttack = int(UpgradeRate * w.wAttack)
                                w.wDefence = int(UpgradeRate * w.wDefence)
                                break
                else:
                    for w in self.w1[num - 1]:
                        if w.wType == 1:
                            w.wAttack = int(UpgradeRate * w.wAttack)
                            w.wDefence = int(UpgradeRate * w.wDefence)
                            break
                        else:
                            print('防御塔已损毁, 升级失败!')
            elif team == 2:
                if num == 0:
                    for i in range(3):
                        for w in self.w2[i]:
                            if w.wType == 0:
                                w.wAttack = int(UpgradeRate * w.wAttack)
                                w.wDefence = int(UpgradeRate * w.wDefence)
                                break
                else:
                    for w in self.w2[3 - num]:
                        if w.wType == 1:
                            w.wAttack = int(UpgradeRate * w.wAttack)
                            w.wDefence = int(UpgradeRate * w.wDefence)
                            break

    # 这是一个发送指令的接口, 可以直接调用以向对手的命令队列发送指令
    def sendCmd(self, target, op, mode):
        if mode == 0:  # 同步
            dataObj = {'froms': account[0], 'to': target, 'CmdType': '-1'}
        elif mode == 1:  # 指令
            #turnID, CmdType, CmdStr, optype
            dataObj = {'froms': account[0], 'to': target,
                       'turnID': op.turnID, 'CmdType': op.CmdType, 'CmdStr': op.CmdStr}
        elif mode == -1:  # 友善(划掉)的提醒对面他挂了
            dataObj = {'froms': account[0], 'to': target, 'CmdType': '-2'}
        datastr = json.dumps(dataObj)
        try:
            tcpCliSock.send(datastr.encode('utf-8'))
        except:
            print('网络罢工了!')

    # 收取命令
    class getCmd(threading.Thread):

        def __init__(self, game):
            threading.Thread.__init__(self)
            self.ops2 = game.ops2  # 内部类通过引用调用外部类变量

        def run(self):
            tcpCliSock.settimeout(0.1)
            while True:
                try:
                    data = tcpCliSock.recv(BUFSIZE).decode('utf-8')
                    if data == '0':  # 同步指令
                        flag[0] = 20  # 每20回合同步一次, 看起来不用线程锁也行
                    elif data == '-1':
                        print('can not connect to target!')
                        sleep(3)
                        sys.exit(0)
                    elif data == '-2':
                        print('你掉线太久, 被自动判负!')
                        sleep(3)
                        sys.exit(0)
                    else:
                        dataObj = json.loads(data)
                        print('{} ->{} : {} {} {}'.format(
                            dataObj['froms'], account[0], dataObj['turnID'], dataObj['CmdType'], dataObj['CmdStr']))
                        t = Command(
                            dataObj['turnID'], dataObj['CmdType'], dataObj['CmdStr'])
                        self.ops2.put(t)  # 收到的指令放进指令堆
                except:
                    pass

    # 读取命令堆中的命令
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

                elif tempOp.CmdType == 3:  # 弓箭手
                    genNum += 1
                    tempObj = Archer(1, genNum, 0)
                    self.w1[int(tempOp.CmdStr[0] - 1)].append(tempObj)
                elif tempOp.CmdType == 0:  # 升级
                    self.upgrade(int(tempOp.CmdStr[0]), 1)
            else:
                # 时机未到
                self.ops1.put(tempOp)
                break

        genNum = 0  # 本回合生成了几个warrior?
        while(not self.ops2.empty()):
            tempOp = self.ops2.get()  # ops为命令队列
            if self.turnID >= tempOp.turnID:  # 尽量让等号成立, 否则游戏不对称
                if tempOp.CmdType == 2:  # 骑士
                    genNum += 1
                    tempObj = Knight(
                        2, genNum, mLen if tempOp.CmdStr[0] == 2 else aLen)
                    self.w2[3 - int(tempOp.CmdStr[0])].append(tempObj)
                elif tempOp.CmdType == 3:  # 弓箭手
                    genNum += 1
                    tempObj = Archer(
                        2, genNum, mLen if tempOp.CmdStr[0] == 2 else aLen)
                    self.w2[3 - int(tempOp.CmdStr[0])].append(tempObj)
                elif tempOp.CmdType == 0:  # 升级
                    self.upgrade(int(tempOp.CmdStr[0]), 2)
            else:
                # 时机未到
                self.ops2.put(tempOp)
                break

    # 武士对战判断函数
    def BattleCheck(self):
        for i in range(3):
            for Warrior1 in self.w1[i]:
                for Warrior2 in self.w2[i]:
                    if abs(Warrior1.pos - Warrior2.pos) <= Warrior1.wRange:
                        Warrior1.couldMove = False
                        if Warrior1.aCD == 0:
                            self.BattleList.append(Battle(Warrior1, Warrior2))
                    if abs(Warrior1.pos - Warrior2.pos) <= Warrior2.wRange:
                        Warrior2.couldMove = False
                        if Warrior2.aCD == 0:
                            self.BattleList.append(Battle(Warrior2, Warrior1))

    # 战斗进行函数
    def BattleRun(self):
        for b in self.BattleList:
            b.BattleGo()
        self.BattleList.clear()

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
        if self.turnID >= 30000 and sumAttack1 != sumAttack2 :
            return 1 if sumAttack2 > sumAttack1 else 2
        return 0  # 战斗尚未结束

    # 武士死亡结算
    def WarriorDeath(self):
        for i in range(3):
            for w in self.w1[i]:
                if w.wLife <= 0:
                    if w.wType == 1:
                        print('己方防御塔被攻陷!')
                        self.life[i + 1] = 0
                        for ww in self.w1[i]:
                            if ww.wType == 0:  # 找到主塔
                                ww.wAttack -= BaseAttack / AttackReduction
                    self.w1[i].remove(w)

        for i in range(3):
            for w in self.w2[i]:
                if w.wLife <= 0:
                    if w.wType == 1:
                        print('敌方防御塔被攻陷!')
                        self.life[i + 5] = 0
                        self.timeCount += 60 * TurretReward  # 奖励
                        for ww in self.w2[i]:
                            if ww.wType == 0:  # 找到主塔
                                ww.wAttack -= BaseAttack / AttackReduction
                    else:
                        self.timeCount += 60 * WarriorReward  # 奖励
                    self.w2[i].remove(w)

    # 武士移动函数
    def WarriorMove(self, WarriorList, team):
        posDict = dict()
        # 第一轮扫描完成各位置上对象的计数
        for i in WarriorList:
            posDict[(i.pos, i.wGrid)] = team

        # 若前方有足够位置就前进, 先排序避免堵车
        WarriorList.sort(key=lambda Warrior: Warrior.pos,
                         reverse=(WarriorList[0].wTeam == 1))
        # 友方移动量为1
        mov = 1
        # 敌方移动量为-1
        if WarriorList[0].wTeam == 2:
            mov = -1
        for i in WarriorList:
            if i.mCD == 0 and i.couldMove and i.wType > 1:  # 塔不能跑!
                for j in range(1, 4):
                    # 前方格子被对方占领时停止移动
                    if posDict.get((i.pos + mov, 0), 0) == 3 - team:
                        break
                    if posDict.get((i.pos + mov, j), 0) == False:
                        posDict[(i.pos, i.wGrid)] = False
                        i.pos += mov
                        posDict[(i.pos, j)] = True
                        i.wGrid = j
                        i.updatemCD(1)
                        break
