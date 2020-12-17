import random
import numpy


# usage:  d = Distribution([1,10])
#         d.uniform_distribution()
#         d.normal_distribution()
#         d.zipf_distribution(1.2)  #suggest to use 1.2


class Distribution:

    threshold = []
    def __init__(self, threshold_ = [1,10]):
        self.threshold = threshold_

    def uniform_distribution(self):
        r = random.uniform(self.threshold[0], self.threshold[1]+1)
        if r <self.threshold[0] or r >self.threshold[1]+1:
            r = self.uniform_distribution()
        return int(r)

    def normal_distribution(self,loc=5, scale = 1.5,size = None):
        loc = self.threshold[1]/2
        scale = self.threshold[1]/5*1.5
        # you can use loc=5 and scale=1.5 for 10 different instance types, use Distribution.normal_distribution() as default
        r = int(numpy.random.normal(loc, scale, size))
        if r < self.threshold[0] or r > self.threshold[1] + 1:
            r = int(self.normal_distribution(loc,scale,size))
        return r

    def laplace_distribution(self,loc=5, scale = 1.5,size = None):
        loc = self.threshold[1]/2
        scale = self.threshold[1]/5*1.5
        r = int(numpy.random.laplace(loc,scale,size))
        if r < self.threshold[0] or r > self.threshold[1] + 1:
            r = int(self.laplace_distribution(loc,scale,size))
        return r

    def zipf_distribution(self,a=1.2):
        a = 1.2
        r = int(numpy.random.zipf(a, size=None))
        if r < self.threshold[0] or r > self.threshold[1] + 1:
            r = int(self.zipf_distribution(a))
        return r

