import queue
import warrior
#重置函数, 开启新一局游戏时调用

def reset():
    for i in range(3):
        w1[i].clear()
        w2[i].clear()

#包含Warrior的列表
w1 = [[], [], []]  # 分别对应左中右路
w2 = [[], [], []]

ops1 = queue.PriorityQueue()
ops2 = queue.PriorityQueue()

if not ops1.empty():
    print(ops1.get())

