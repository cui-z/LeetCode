
'''
冒泡排序
    没一次都进行大小的比较 并且进行转换
'''

def slove1(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return  nums
print(slove1([4,1,3,5,2,5]))

'''
选择排序  
    提高了冒泡排序的效率 每一次遍历只进行一次交换数据 没戏遍历选择出一个极值
'''
def slove2(nums):
    for i in range(len(nums)):
        min_index =i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return  nums

print(slove2([2,1,2,3,5,3,4,8]))



'''
插入排序

总是保持一个位置在前的已经排好的子表   然后拿后面的数值 在前面的子表里面比较 
移动子表里面的数据 确定新的数据的插入位置
'''
def slove3(nums):

    for i in range(1,len(nums)):
        num = nums[i]
        pos = i
        while nums[pos-1] > num  and pos>1:
            nums[pos] = num
            pos -=1
        nums[pos] = num
    return  nums

print(slove3([1,4,2,3,5]))



'''
快速排序
随意选择一个数作为基准 小的在左  大的右
'''

def slove(nums,first,last):
    if first >= last:
        return
    mid = nums[first] #相当于把比较数 拿出来
    l = first
    r =last
    while l < r:
        while l < r and nums[r] >= mid:
            r-=1
        #把右边小的数拿出来 放单比较数的初始位置
        nums[l] = nums[r]
        while l< r and nums[l] < mid:
            l+=1
        nums[r] =  nums[l]
    nums[l] = mid
    slove(nums,first,l-1)
    slove(nums,l+1,last)
l = [2,4,1,2,5,8,3]
slove(l,0,len(l)-1)
print(l)

"""
归并排序。

归并排序的核心思想是分治法，将已有序的子序列合并，得到完全有序的序列。基本过程：假设初始序列含有n个记录，则可以
看成是n个有序的子序列，每个子序列的长度为1，然后两两归并，得到n/2个长度为2或1的有序子序列，再两两归并，最终得到
一个长度为n的有序序列为止，这称为2路归并排序。

复杂度 nlogn

"""
def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return marge_sort(merge_sort(left),merge_sort(right))
def marge_sort(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result+=left
    result+=right
    return result
arr = [2,36,32,54,89,98,65,12,74]
print(merge_sort(arr))
