# -*- coding: utf-8 -*-
# 这里是游戏的服务器端, 如果你想自己部署游戏服务器, 请运行该程序

import socketserver
import json
import subprocess

HOST = 8026  # 开放的端口
connLst = []
tick = dict()  # 用于维护时间刻的同步

# 存放连接


class Connector(object):
    def __init__(self, account, addrPort, conObj):
        self.account = account
        self.addrPort = addrPort
        self.conObj = conObj

# 用于注册新连接, 并完成命令转发的类


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("收到连接", self.client_address)
        userIn = False
        global connLst
        while not userIn:
            conn = self.request
            data = conn.recv(1024)
            if not data:
                continue
            dataobj = json.loads(data.decode('utf-8'))
            # 如果连接客户端发送过来的信息格式是一个列表且注册标识为False时进行用户注册
            ret = '0'
            # 注册新连接
            if type(dataobj) == list and not userIn:
                account = dataobj[0]
                try:
                    conObj = Connector(
                        account, self.client_address, self.request)
                    if len(connLst) > 15:
                        #列表出现冗余, 移除多余的账户
                        cnt = 0
                        for u in connLst:
                            connLst.remove(u)
                            cnt += 1
                            if cnt > 5:
                                break
                    connLst.append(conObj)
                    print('{}已成功注册!({})'.format(
                        account, self.client_address))
                except:
                    print('%s 注册失败!' %
                          account)
                    ret = '99'
            conn.sendall(ret.encode('utf-8'))
            if ret == '0':  # 注册成功
                break
        global tick
        while True:
            conn = self.request
            data = conn.recv(1024)
            if not data:
                continue
            dataobj = data.decode('utf-8')
            dataobj = json.loads(dataobj)
            if dataobj['CmdType'] == '-1':  # 同步指令
                if tick.get((dataobj['to'], dataobj['froms']), False) == True:
                    # 本地运行的回合数一致, 此时给两个人都发'0', 允许本地继续运行
                    tick[(dataobj['to'], dataobj['froms'])] = False
                    if len(connLst) > 0:
                        conn.sendall('0'.encode('utf-8'))
                        sendok = False
                        for obj in connLst:
                            if dataobj['to'] == obj.account:
                                try:
                                    obj.conObj.sendall('0'.encode('utf-8'))
                                except:
                                    pass
                else:
                    # 仅收到一个本地端的运行结束信号, 设置flag后继续等待
                    tick[(dataobj['froms'], dataobj['to'])] = True
            elif dataobj['CmdType'] == '-2':  # 告诉对方他因为超时挂了
                for obj in connLst:
                    if dataobj['to'] == obj.account:
                        try:
                            obj.conObj.sendall('-2')
                        except:
                            pass
            # 客户端将指令发给服务器端然后由服务器转发给目标客户端
            elif len(connLst) > 1:
                for obj in connLst:
                    if dataobj['to'] == obj.account:
                        try:
                            obj.conObj.sendall(data)
                        except:
                            pass
            else:
                conn.sendall('-1'.encode('utf-8'))
                continue


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('', HOST), MyServer)
    print('等待连接中')
    server.serve_forever()
