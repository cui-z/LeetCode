'''
给定一个排序数组 原地删除重复的元素 使得每个元素最多出现两次
返回移除后数组的新长度
'''

def slove(nums):
    length = len(nums)
    i=1
    cnt=1
    while i < length:
        if nums[i] == nums[i-1]:
            if cnt ==1:
                cnt +=1
                i+=1
            elif cnt ==2:
                nums.remove(nums[i])
                length-=1
                cnt-=1
        else:
            i+=1
    return length

print(slove([0,0,1,1,1,1,2,3,3]))
