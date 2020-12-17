import socket

from ACN_final.new_dist.distribution import *


def main(n):
    range_start = 1
    range_end = n
    d = Distribution([range_start, range_end])

    # buffer_time = 0.5
    IP = '127.0.0.1'
    PORT = 5005
    BUFFER_SIZE = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    counter = 0
    while True:
        for i in range(100):  # generation capacity

            # MESSAGE = bytes(str(random.randint(1, n)), encoding='utf-8')
            # MESSAGE = bytes(str(d.uniform_distribution()), encoding='utf-8')
            MESSAGE = bytes(str(d.normal_distribution()), encoding='utf-8')
            # MESSAGE = bytes(str(d.laplace_distribution()), encoding='utf-8')
            # MESSAGE = bytes(str(d.zipf_distribution()), encoding='utf-8')

            s.send(MESSAGE)
            counter += 1

    s.close()


if __name__ == '__main__':
    main(3000)
