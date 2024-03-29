from random import random
import math


class ReservoirSampling(object):
    def __init__(self, sample_num):
        assert sample_num > 0
        self._sample_num = int(sample_num)
        self._reservoir = []
        self._threshold = 4 * sample_num
        self._pos = 0
        self._gap = 0
        self._cal_gap = True
        self._sample = self._no_sample

    """ Function to fill the ._resrvoir list by appending item from sample()
        to build a list of items.
    """
    def _no_sample(self, item):
        self._reservoir.append(item)
        if len(self._reservoir) >= self._sample_num:
            self._sample = self._naive_sample

    """ Naive sampling function to place item in the ._resrvoir list 
        for position 'k' in a random order.        
    """
    def _naive_sample(self, item):
        k = int(random() * self._pos)
        if k < self._sample_num:
            self._reservoir[k] = item
        if self._pos >= self._threshold:
            self._sample = self._gap_sample

    """ Gap sampling distribution function for skips betweem samples, 
        with 'sample_num' as reservoir size and 'pos' index of element considered.      
    """
    def _gap_sample(self, item):
        if self._gap > 0:
            self._gap += -1
            return
        if self._cal_gap:
            self._gap = int(math.log(random()) /
                            math.log(1 - self._sample_num / self._pos))
            self._cal_gap = False
            self._sample(item)
        else:
            k = int(random() * self._sample_num)
            self._reservoir[k] = item
            self._cal_gap = True

    def sample(self, item):
        self._pos += 1
        self._sample(item)

    def __iter__(self):
        return iter(self._reservoir)