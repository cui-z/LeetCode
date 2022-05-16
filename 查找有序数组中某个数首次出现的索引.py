"""
给定一个升序的数组，这个数组中可能含有相同的元素，并且给定一个目标值。要求找出目标值在数组中首次出现的下标。


有序序列 ——》 二分法
"""


def slove(nums,target):
    l =0
    r =len(nums)-1

    while l <= r:
        mid = l + (r-l)//2
        if (nums[mid] == target) and (nums[mid-1]!= target):
            return mid
        elif nums[mid] < target:
            l = mid+1
        else: ##除了包括  nums[mid] > target 的情况  还有 (nums[mid] == target) and (nums[mid-1] == target)
            r = mid-1
    return -1

print(slove([1,3,4,4,5,5,6],5))
