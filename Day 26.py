import sys

inlist = sys.stdin.readlines()
ad, am, ay = map(int, inlist[0].strip().split())
ed, em, ey = map(int, inlist[1].strip().split())

if ay > ey: 
    print(10000)
elif ay == ey and am > em: 
    print((am-em)*500)
elif ay == ey and am == em and ad > ed: 
    print((ad-ed)*15)
else: print(0)