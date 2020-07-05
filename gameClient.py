# coding:utf-8

from socket import *
import threading
import sys
import json
import re

#HOST = '65.49.209.247'
HOST = 'localhost'
PORT = 8023
BUFSIZE = 1024  # 缓冲区大小  1K
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
userAccount = None


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


def chat(target, op):
    #turnID, CmdType, CmdStr, optype
    dataObj = {'froms': userAccount, 'to': target,
               'turnID': op.turnID, 'CmdType': op.CmdType, 'CmdStr': op.CmdStr}
    datastr = json.dumps(dataObj)
    try:
        tcpCliSock.send(datastr.encode('utf-8'))
    except:
        print('awsl')

'''
#多线程运行时所需代码
class inputdata(threading.Thread):
    def run(self):
        target = input('Please choose your adversary: ')
        if target == 'Q':
            sys.exit(1)
        turnID = input()
        CmdType = input()
        CmdStr = input()
        op = Command(turnID, CmdType, CmdStr)
        dataObj = {'froms': userAccount, 'to': target,
                   'turnID': op.turnID, 'CmdType': op.CmdType, 'CmdStr': op.CmdStr}
        datastr = json.dumps(dataObj)
        try:
            tcpCliSock.send(datastr.encode('utf-8'))
        except:
            print('awsl')


class getdata(threading.Thread):
    def run(self):
        while True:
            data = tcpCliSock.recv(BUFSIZE).decode('utf-8')
            if data == '-1':
                print('can not connect to target!')
            elif data:
                dataObj = json.loads(data)
                print('{} ->{} : {} {} {}'.format(dataObj['froms'],
                                              userAccount, dataObj['turnID'], dataObj['CmdType'], dataObj['CmdStr']))
'''

def getdata():
    data = tcpCliSock.recv(BUFSIZE).decode('utf-8')
    if data == '-1':
        print('can not connect to target!')
    elif data:
        dataObj = json.loads(data)
        print('{} ->{} : {} {} {}'.format(dataObj['froms'],
                                                  userAccount, dataObj['turnID'], dataObj['CmdType'], dataObj['CmdStr']))

def main():
    try:
        tcpCliSock.connect(ADDR)
        print('Connected with server')
        while True:
            reg = register()
            if reg:
                break
        
        #myinputd = inputdata()  # 选择对手并开启chat
        #mygetdata = getdata()
        #myinputd.start()
        #mygetdata.start()
        #myinputd.join()
        #mygetdata.join()
        while True:
            target = input()
            turnID = input()
            CmdType = input()
            CmdStr = input()
            op = Command(turnID, CmdType, CmdStr)
            chat(target, op)
            getdata()

    except Exception:
        print('error')
        tcpCliSock.close()
        sys.exit()


if __name__ == '__main__':
    main()
