from ACN.new_dist.distribution  import *

range_start = 1
range_end = 1000

d = Distribution([range_start,range_end]) # 以start为开始和end为结束创造一个分布范围

print(d.uniform_distribution())
print(d.normal_distribution())
print(d.laplace_distribution())
print(d.zipf_distribution())

for i in range(500):
    print(d.uniform_distribution())