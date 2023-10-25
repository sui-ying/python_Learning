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
    singThread = threading.Thread(target=sing, kwargs={"num": 10, "msg": "I am singing..."})
    # 以元组形式传参
    danceThread = threading.Thread(target=dance, args=("I am dancing...",))  
    ballThread = threading.Thread(target=ball)

    # 3. 启动子线程对象
    singThread.start()
    danceThread.start()
    ballThread.start()
