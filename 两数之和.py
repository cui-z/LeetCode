#返回索引值
def solve(nums,target):
    res={}
    for i  in range(len(nums)):
        n = nums[i]
        r = target -n
        if r in res.keys():
            return res[r],i
        else:
            res[n] = i

    return None


print(solve([2,7,11,15],9))