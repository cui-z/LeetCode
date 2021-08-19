'''
给定一个数组nums 和一个值 val 你需要原地移除等于val的值 返回移除后数组的长度
 不要使用额外的数组空间 原地修改
'''

def slove(nums,val):
    curr=0
    length = len(nums)
    while curr < length:
        if nums[curr] == val:
            nums.remove(nums[curr])
            length-=1
        else:
            curr+=1
    return length


print(slove([0,1,2,2,3,0,4,2],2))