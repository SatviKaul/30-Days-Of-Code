T = int(input())
i=1
while i<=T:
    str=input()
    even=""
    odd=""
    x=str[::2]
    y=str[1::2]
    even=x
    odd=y
    i+=1
    print(even,odd)