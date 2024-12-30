b=[1,2,3,4,5,6,7,8,9,11,12,13,14,15]
for i in range(1,101):
    a=i/7
    if a in b or "7" in str(i):    #也可以用%余数为零
        continue
    print(i)
