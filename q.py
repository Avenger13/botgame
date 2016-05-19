# -*- coding: utf-8 -*-
class Q:
    def __init__(self, q, vargs):
        self.q = q
        self.vargs = vargs
        for v in vargs:
            if vargs[v]:
                self.right = v

    def is_right(self, e):
        # keys = self.vargs.keys()
        # for k in keys:
        #     if k == e:
        #         return self.vargs[e]
        #
        # print('choose one of the listed variants')
        print('e = ' + e)
        print(type(e))
        print('right = ' + self.right)
        print(type(self.right))
        return e == self.right
