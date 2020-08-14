#!/usr/bin/python3
def sqr(x):
   return x*x
print(list(map(sqr, [x for x in range(1,5)])))
