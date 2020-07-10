# coding:utf-8
import socketserver
import json
import time
import subprocess


connLst = []
tick = dict()  # 用于维护时间刻的同步

# 代号 地址和端口 连接对象

# optype = {'ag':'group adding','cp':'chat with individual','cg':'chat with group'}


class Connector(object):  # 存放连接
    def __init__(self, account, addrPort, conObj):
        self.account = account
        self.addrPort = addrPort
        self.conObj = conObj


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("got connection from", self.client_address)
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
                    print('{} has connected to the system({})'.format(
                        account, self.client_address))
                except:
                    print('%s failed to register for exception!' %
                          account)
                    ret = '99'
            conn.sendall(ret.encode('utf-8'))
            if ret == '0':
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
                    tick[(dataobj['to'], dataobj['froms'])] = False
                    if len(connLst) > 0:
                        conn.sendall('0'.encode('utf-8'))
                        sendok = False
                        for obj in connLst:
                            if dataobj['to'] == obj.account:
                                try:
                                    obj.conObj.sendall('0'.encode('utf-8'))
                                    print('success')
                                    sendok = True
                                except:
                                    pass
                        if sendok == False:
                            print('no target valid!')
                else:
                    tick[(dataobj['froms'], dataobj['to'])] = True
            # 客户端将数据发给服务器端然后由服务器转发给目标客户端
            # print('connLst', connLst)
            elif len(connLst) > 1:
                print(data)
                sendok = False
                for obj in connLst:
                    if dataobj['to'] == obj.account:
                        try:
                            print('success')
                            obj.conObj.sendall(data)
                            sendok = True
                        except:
                            pass
                if sendok == False:
                    print('no target valid!')
            else:
                conn.sendall('-1'.encode('utf-8'))
                continue


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('', 8029), MyServer)
    print('waiting for connection...')
    server.serve_forever()