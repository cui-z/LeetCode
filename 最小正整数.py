# 给定一个未排序的整数数组  找出其中没有出现的最小正整数

def solve(nums):
    for i in range(len(nums)):
        if 0 <nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
            #print(nums[i], nums[nums[i] - 1])
            tmp = nums[nums[i]-1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = tmp
        else:
            pass
    for i in range(len(nums)):
        if nums[i] != i+1:
            return  i+1
    return len(nums)+1

print(solve([2,2,1]))