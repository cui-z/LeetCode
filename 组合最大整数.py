# 给定一组非负整数，重新排列他们顺序使之组成一个最大整数

def solve(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(int(str(nums[i])+str(nums[j])) < int(str(nums[j])+str(nums[i]))):
                nums[i],nums[j] = nums[j],nums[i]
                # tmp = nums[i]
                # nums[i] = nums[j]
                # nums[j] = tmp
        
    print(nums)

solve([3,30,34,5,9])