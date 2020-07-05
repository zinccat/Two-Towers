# -*- coding: utf-8 -*-
# 命令接口

import queue
from warrior import *


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

# 命令读取函数


# SideWarriorList为某一方的总list
# team为1 友方, 2 敌方
def ReadCmd(CmdList, SideWarriorList, team):
    genNum = 0 #本回合生成了几个warrior?
    while(not CmdList.empty()):
        tempOp = ops.get() #ops为命令队列
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
            ops.put(tempOp)
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
