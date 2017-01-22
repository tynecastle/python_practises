#!/usr/bin/env python

L = [7,4,6,3,9,1,5,2,8,0,2]

for i in xrange(len(L)):
    for j in xrange(i):
        if L[j] > L[i]:
            L[i],L[j] = L[j],L[i]

print(L)
