import pgzrun

# 好多数值都用的拼音...

WIDTH=1200
HEIGHT=700

money0=Actor('金钱框')
money0.topleft=25,200
money2=Actor('钱币图标')
money2.topleft=25,177
money1=Actor('金钱块')

qianshu=0
jiaqianjishi=0

def draw():
    screen.clear()
    screen.fill((128,128,128))
    money0.draw()
    money2.draw()
    for i in range(qianshu):
        money1.topleft=28+20*i,203
        money1.draw()
    screen.draw.text("Money:%d/10" % qianshu,(50,182))

def update():
    global jiaqianjishi
    if qianshu<10:
        jiaqianjishi=jiaqianjishi+1
        if jiaqianjishi==60:
            qianshubh(1)
            jiaqianjishi=0

#钱数变化的函数
def qianshubh(qsbh):
    global qianshu
    qianshu=qianshu+qsbh

# 这里还要再改应该
# 随便设了个减掉钱数的指令，改的时候还要考虑如果钱不够就不能造兵
def on_mouse_down():
    if qianshu>=2:
        qianshubh(-2)

pgzrun.go()