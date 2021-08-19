'''
在一条道路上有N个加油站，其中第i个加油站有汽油gas[i]升
你有一辆油箱无限的汽车，从第i个加油站开始往往i+1个加油站消耗cost[i]

你从其中的一个加油站出发，开始时为空
如果你可以绕一圈，则返回出发时加油站编号 否则返回-1
'''

def slove(gas,cost):

    if sum(cost) < sum(gas):
        return  -1

    total=0
    num=0
    for i in range(len(gas)):
        total+=gas[i]-cost[i]
        if total<0:
            total=0
            num=i+1
    return num


print(slove([1,2,3,4,5],[3,4,5,1,2]))