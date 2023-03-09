"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。如果数组中不存在目标值，返回 [-1, -1]。
"""


def slove(nums, target):
    if nums == []:
        return [-1, -1]
    if len(nums) == 1 and nums[0] == target:
        return [0, 0]
    elif len(nums) == 1 and nums[0] != target:
        return [-1, -1]

    l = 0
    r = len(nums)-1
    while l <= r:
        mid = l + (r - l) // 2
        print(mid)
        if nums[mid] == target:
            m = mid
            ll = mid
            rr = mid
            while (ll -1) >=0 and nums[ll-1] == target:
                ll-=1
            while (rr +1 ) <= len(nums)-1 and nums[rr+1] == target:
                rr+=1
            # while (mid - 1) >= 0 and nums[mid - 1] == target:
            #     ll = mid - 1
            #     mid =mid-1
            # while (m + 1) <= len(nums)-1 and nums[m + 1] == target:
            #     rr = m + 1
            #     m = m+1
            return [ll, rr]
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return [-1, -1]

print(slove(nums=[ 8,8,8, 8,9,10], target=8))
