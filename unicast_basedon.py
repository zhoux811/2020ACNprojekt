import socket
import time
from collections import deque
import plotly.express as px


def main(n, buffer_time, processing_capacity, counter):
    c = 1
    '''    
    buffer_time = 0.5
    processing_capacity = 10
    n = 1000
    '''

    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    # counter = 0
    conn, addr = s.accept()
    print('Connection address:', addr)

    queues = deque()
    process_counter = 0
    queue_len = []

    while c < counter:
        t_end = time.time() + buffer_time
        while time.time() < t_end:
            data = conn.recv(6555)
            if not data:
                break
            # counter += 1
            queues.append(len(data))

        to_be_deleted = list(set(queues))[:processing_capacity]  # previous processed

        for tbd in to_be_deleted:
            queues.remove(tbd)

        to_be_deleted.clear()
        f = open('result.txt', 'a+')
        f.write('\n buffer_time: %f ,  '
                'processing_capacity: %d, '
                'use n: %d , '
                'counter: %d, '
                'queue length left is : %d '
                % (buffer_time, processing_capacity, n, c, len(queues)))
        # queue_len.append(len(queues))
        queue_len.append(len(queues) / c)

        c += 1

    fig = px.scatter(y=queue_len)
    fig.show()
    f.write('\n\n\n ')


if __name__ == '__main__':
    # main(sys.argv[1], sys.argv[2], sys.argv[3])
    # (n, buffer_time, processing_capacity, counter):
    main(3000, 0.2, 1, 100)
