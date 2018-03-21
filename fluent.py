import sys

from hue import *


_MODULE = sys.modules[__name__]


class Hue(object):

    def __init__(self, string):
        self.string = string
        self.stack = []

        def h(string):
            hue =  Hue(string)
            self.stack.append(hue)

        self._ = h

    def __call__(self, string):
        h = Hue(string)

        if len(self.stack):
            last = self.stack.pop()
            getattr(h, last)

        self.stack.append(h)

        return h

    def __getattr__(self, attr):
        self.stack.append(attr.lower())

        return self

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        string = self.string

        for h in self.stack:
            if isinstance(h, Hue):
                string += str(h)
            else:
                string = getattr(_MODULE, h)(string)

        return string
