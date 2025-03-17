import os
import time


def addIp(ip: str):
    if not os.path.exists("./logIp/"):
        os.mkdir("./logIp/")
    with open("./logIp/logIp.txt", "a") as f:
        t = str(time.ctime())
        f.write(t + " >> " + ip + "\n")
