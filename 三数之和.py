'''
给定一个数组  判断里面的三个元素 a b c 使得 a+b+c=0
找出满足条件的元素  不能包含重复的三个元素
'''

def slove(nums):
    nums.sort()
    result=[]

    for i in range(len(nums)):
        if i ==0 or nums[i]>nums[i-1]:
            l = i+1
            r = len(nums)-1
            while l < r:
                sum = nums[i] + nums[l]+nums[r]
                if sum ==0:
                    result.append([nums[i] ,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l <r and nums[l] == nums[l-1]:
                        l+=1
                    while l <r  and nums[r] == nums[r+1]:
                        r-=1
                if sum < 0:
                    l+=1
                if sum > 0:
                    r-=1
    return result

print(slove([0,0,0]))