'''
假设按照升序排序的数组在预先位置的某个点进行了旋转
1 2 3 4 5 6       4 5 6 1 2 3
搜索一个给定的目标值 如果目标值存在则返回索引 否则返回-1
不存在重复元素

'''

def slove(nums,target):
    l=0
    r = len(nums)-1

    while l <= r:
        mid = l+(r-l)//2  #向下取整
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if target >= nums[l] and target <= nums[mid]:
                r = mid-1
            else:
                l = mid+1
        else:
            if target >= nums[mid] and target <= nums[r]:
                l = mid+1
            else:
                r = mid-1
    return -1


print(slove([4,5,1,2,3],3))