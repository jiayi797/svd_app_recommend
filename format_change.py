#!/usr/bin/python
#coding=utf-8
from time import time

t0 = time()

lines = []
print("loading data ...")
with open("user_installedapps.csv") as f:
    lines = f.readlines()
print("load data in %.3f s."%(time() - t0))



m = 0
for i in range(1, len(lines)):
    line = lines[i]
    line = line.strip().split(",")
    m = max(m, int(line[0]))
print m


"""
t0 = time()
info = [[] for i in range(433269 + 1)]
for i in range(1, len(lines)):
    line = lines[i]
    line = line.strip().split(",")
    info[int(line[1])].append(line[0])   
    if i % 100000 == 0:
        print("transform data %d in %.3f s."%(i, time() - t0))

f=open("user_installedapps.txt", "w")
for i in range(len(info)):
    if len(info[i]) <= 0:
        continue

    f.write(str(i) + ":" + " ".join(info[i]) + "\n")    
    if i % 10000 == 0:
        print("write data %d in %.3f s."%(i, time() - t0))

f.close()
"""

