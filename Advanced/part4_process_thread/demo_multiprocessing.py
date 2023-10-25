# 1. 引入包
import multiprocessing
import time


def sing(msg):
    for i in range(10):
        # print("I am singing...")
        print(msg)
        time.sleep(1)


def dance(num, msg):
    for i in range(num):
        # print("I am dancing...")
        print(msg)
        time.sleep(1)


def ball():
    for i in range(10):
        print("I am playing ball...")
        time.sleep(1)


if __name__ == '__main__':
    # 2. 创建子进程对象
    # 元组方式传参, 参数顺序一致
    singProcess = multiprocessing.Process(target=sing, args=("I am singing...",))
    # 字典方式传参，以key名为参数名
    danceProcess = multiprocessing.Process(target=dance, kwargs={"num": 10, "msg": "I am dancing..."})

    # 3. 子进程对象对象启动执行任务
    singProcess.start()
    danceProcess.start()
