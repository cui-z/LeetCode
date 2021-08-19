resu=[]
def solve(nums,list):
    if len(nums) ==0:
        resu.append(list)
        return
    for i in range(len(nums)):
        solve(nums[:i]+nums[i+1:],list+[nums[i]])

solve([1,2,3],[])
print(resu)

#[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]