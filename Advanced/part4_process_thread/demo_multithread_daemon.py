import time
import threading   # 1. 引入包


def sing(num, msg):
    for i in range(num):
        # print("I am singing...")
        print(msg)
        time.sleep(1)


def dance(msg):
    for i in range(10):
        # print("I am dancing...")
        print(msg)
        time.sleep(1)


def ball():
    for i in range(10):
        print("I am playing ball...")
        time.sleep(1)


if __name__ == '__main__':

    # 2. 创建子线程对象
    # 以字典形式进行传参
    # 如果主线程结束时不想等待子线程结束，可以设置子线程守护主线程
    singThread = threading.Thread(target=sing, kwargs={"num": 10, "msg": "I am singing..."}, daemon=True)
    # 以元组形式传参
    danceThread = threading.Thread(target=dance, args=("I am dancing...",), daemon=True)  
    ballThread = threading.Thread(target=ball)
    ballThread.setDaemon(True)  # 方式二： 设置守护线程

    # 3. 启动子线程对象
    singThread.start()
    danceThread.start()
    ballThread.start()

    # 类似地，主线程会等待子线程执行完成才结束
    time.sleep(1)
    print("主线程执行结束啦!")