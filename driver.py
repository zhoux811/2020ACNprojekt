from threading import Thread
from time import sleep
import os
import sys


def server():
    # global n, buffer_time, processing_capacity
    # cmd = 'python FCFS.py '
    cmd = 'python unicast_basedon.py '
    os.system(cmd)


def client():
    # global n
    cmd = 'python  client.py   '
    os.system(cmd)


t_server = Thread(target=server, args=())
t_client = Thread(target=client, args=())

t_server.start()
sleep(0.5)
t_client.start()
