'''
给定一个数组nums，编写一个函数将所有的0移动到数组的末尾，同时保持非0元素的相对顺序
'''

def slove(nums):
    i,j = 0,0
 # i 是找0   j找非0
    while(i < len(nums)) and (j < len(nums)):
        if nums[i]:
            i+=1
            j+=1
            continue
        if nums[j]:
            nums[i] = nums[j]
            nums[j] = 0
            i+=1
        j+=1
    return nums

print(slove([0,0,2,4,0,0,6]))
