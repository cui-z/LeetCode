'''
二分查找  一定是有顺序的   返回下标
'''

def slove(nums,target):
    l=0
    r = len(nums)-1

    while l <= r:
        mid = l+(r-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return False

print(slove([1,3,4,6,8,9],3))