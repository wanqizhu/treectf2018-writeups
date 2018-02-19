# python 3
from antigravity import *
import datetime
import time
import numpy as np


f = open("flag.txt").read()
np.random.seed(ord(f[-1]))

for c1, c2 in zip(f[::-2], f[::2]):
	t = datetime.datetime.now()
	t = str.encode("_".join(map(str,[t.year, t.month, t.second])))
	geohash(ord(c1)+np.random.random(), ord(c2)+np.random.random(), t)
	time.sleep(np.random.randint(1,13))