# coding:utf-8

import socketserver
import json
import time
import subprocess

connLst = []
# 代号 地址和端口 连接对象
# optype = {'ag':'group adding','cp':'chat with individual','cg':'chat with group'}


class Connector(object):  # 存放连接
    def __init__(self, account, addrPort, conObj):
        self.account = account
        self.addrPort = addrPort
        self.conObj = conObj


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # 测试
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
                    conObj = Connector(account, self.client_address, self.request)
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

        while True:
            conn = self.request
            data = conn.recv(1024)
            if not data:
                continue
            print(data)
            dataobj = data.decode('utf-8')
            dataobj = json.loads(dataobj)
            # 客户端将数据发给服务器端然后由服务器转发给目标客户端
            # print('connLst', connLst)
            if len(connLst) > 1:
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
    server = socketserver.ThreadingTCPServer(('', 8023), MyServer)
    print('waiting for connection...')
    server.serve_forever()
