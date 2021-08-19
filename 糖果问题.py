#每人至少一块糖 相邻的 评分高的必须多获得糖


def solve(nums):
    result=[1 for _ in range(len(nums))]
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            result[i] = result[i-1]+1
    for j in range(len(nums)-2,-1,-1):
        if nums[j] > nums[j+1]:
            print(j)
            result[j] = max(result[j],result[j+1]+1)
    return sum(result)

print(solve([1,0,2]))