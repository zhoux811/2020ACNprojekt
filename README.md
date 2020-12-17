# 2020ACNprojekt
This program generates log file. Please watch for permission to write/read.


How to run:

Step1: decide what parameters and multicast strategy you want to use: 
Listed below are some interesting ones that produce good result:
Buffer time *
times:	Unicast or
Multicast	multicasting 
strategy	Number of
unique requests	Processing capacity	distribution
0.2*200	unicast	unicast	3000	1	uniform
0.2*150	unicast	unicast	2000	1	uniform
0.15s*500	multi	FCFS	1000	5	uniform
0.15s*300	multi	FCFS	1000	5	zipf
0.15s*300	multi	FCFS	1000	3	laplacian
0.15s*500	multi	FCFS	1000	5	normal
0.15s*500	multi	FCFS	1000	7	normal
0.15s*500	multi	FCFS	1000	9	normal
0.15s*1000	multi	FCFS	1000	10	uniform

Depending on your system, buffer time should not exceed a certain value, too large of a buffer time will have the program crash due to not enough cache or bad result due to packet time-out.
If you see the queue length(total or average) close to zero at all times, it means too little of buffer time.

There are tho different files for server, unicast and multicast respectively.
Number of unique requests used in the paper for reference is always 1000. Too little of that if you do not have more than 30s of running time, it is not suggested that you go over 1000, where all combinations will be met.

Processing capacity has been tested to be mostly valid around five to ten. Depends on the system, if you want to adjust it , please increase or decrease by value of one since this is a very sensitive variable.

Zipf, laplacian and normal distribution functions can be adjusted separately in the new_dist directory. They produce similar result. Use any. When using uniform distribution, the number of unique requests requirement mentioned above is even more important to follow.

The processing capacity of unicast should always be 1.

Step2. after you have decided the parameters, fill in those parameters in :

Line 35 of client.py (number of unique requests)
Line 63 of FCFS.py (number of unique requests, buffer time, processing capacity, running time)
or
Line 66 of unicast_basedon.py (number of unique requests, buffer time, processing capacity, running time)

Step3:
Depends on the type of distribution you want to use, comment out desired method in line 22 to line 26 in client.py.

Step4:
If you want to see graph and data: total queue length: 
Keep line 51, comment out line 52 in FCFS.py
Keep line 53, comment out line 54 in unicast_basedon.py

If you want to see the derivative of total queue length (the “average queue length” as in the paper):
Keep line 52, comment out line 51 in FCFS.py
Keep line 54, comment out line 53 in unicast_basedon.py

Step5: 
If you are running client on a different ip, make changes on the head of the files respectively.

Step6:
Run FCFS.py or unicast_basedon.py first, then client.py. The result will be visualized and appended to result.txt after trial is finished.
A driver program has been included to ease the running, but it does not change the parameters for you.
