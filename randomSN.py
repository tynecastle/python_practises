#!/usr/bin/env python

import random
import string

list_len = 10
SN_len = 12

def genSN(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in xrange(size))

for num in xrange(list_len):
    randSN = genSN()
    with open('SN.txt', 'a') as fd:
        fd.write(randSN + '\n')
