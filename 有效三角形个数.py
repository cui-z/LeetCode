'''

给定一个包含非负整数的数组 你的任务是统计其中可以组成三角形三条边的三元组个数

2 2 3 4
结果 3
2,3,4
2,3,4
2，2,3
'''


#只需要满足两个短边之和大于第三边就可


def slove(nums):
    num = 0
    nums.sort()
    for i in range(2,len(nums)):
        l = 0
        r = i-1
        while l <= r:
            if nums[l] + nums[r] > nums[i]:
                num+=(r-l)
                r-=1
            else:
                l+=1
    return  num

print(slove([2,3,2,4]))

