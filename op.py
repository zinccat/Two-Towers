# -*- coding: utf-8 -*-
# 命令接口

import queue


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

# 命令读取函数


def ReadCmd(CmdList):
    while(not CmdList.empty()):
        tempOp = ops.get()
        if turnID == tempOp.turnID:
            print(tempOp.playerID)
        else:
            # 时机未到
            ops.put(tempOp)
            break


ops = queue.PriorityQueue()
turnID = 1
ops.put(Command(1, 1, 1, 1))
ReadCmd(ops)
