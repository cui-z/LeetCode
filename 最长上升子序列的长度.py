# 子序列是不连续的  返回长度

def solve(nums):
    result= [1 for _ in range(len(nums))]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                result[i] = max(result[i],result[j]+1)
    return  max(result)


print(solve([10,9,2,5,3,7,101,18]))