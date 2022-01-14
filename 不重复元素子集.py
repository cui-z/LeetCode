
'''
给定一组不含重复元素的整数数组nums 返回该数组所有可能的子集

【1 2 3】

[
[1]
[2]
[3]
[1 2 3]
[1 3]
[1 2]
[2 3]
[]
]

'''

def slove(nums):
    result=[]
    def dfs(nums,path,start):
        if path:
            result.append(path)
        for i in range(start,len(nums)):
            dfs(nums,path+[nums[i]],i+1)
    dfs(nums,[],0)
    return  result

print(slove([1,2,3]))