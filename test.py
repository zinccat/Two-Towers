# 所有跑单函数测试的操作都在这里进行
'''
from backstage import *
game = Action()
c1 = Command(1, 2, [0])
c2 = Command(2, 2, [0])
game.ops2.put(c1)
game.ops2.put(c2)
print(game.ops2.get().turnID)
print(2==[2][0])
'''

import easygui as gui
from socket import *
import sys
import json

HOST = '62.234.107.120'
# HOST = 'localhost'
PORT = 8026
BUFSIZE = 1024  # 缓冲区大小  1K
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
account = [None]
target = [None]
game = None


def connect():
    try:
        tcpCliSock.connect(ADDR)
        print('Connected with server')
        while True:  # 注册
            msg = "请输入双方id并点击开始游戏"
            title = "Welcome"
            fieldNames = ["*你是谁", "*想打谁"]
            fieldValues = []
            fieldValues = gui.multenterbox(msg, title, fieldNames)
            while True:
                if fieldValues == None:
                    break
                errmsg = ""
                for i in range(len(fieldNames)):
                    option = fieldNames[i].strip()
                    if fieldValues[i].strip() == "" and option[0] == "*":
                        errmsg += ("[%s]为必填项! " % fieldNames[i])
                if errmsg == "":
                    break
                fieldValues = gui.multenterbox(errmsg, title, fieldNames, fieldValues)
            print(fieldValues)
            account[0] = fieldValues[0]
            target[0] = fieldValues[1]
            regInfo = [fieldValues[0], 'register']
            datastr = json.dumps(regInfo)
            tcpCliSock.send(datastr.encode('utf-8'))
            data = tcpCliSock.recv(BUFSIZE)
            data = data.decode('utf-8')
            if data == '0':
                print('Success to register!')
                break
            else:
                print('Failed for exceptions!')
                continue
    except:
        print('error')
        sys.exit(0)

tcpCliSock.settimeout(0.1)
connect()
print(account)
print(target)
