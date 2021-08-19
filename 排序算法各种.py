
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
    mid = nums[first]
    l = first
    r =last
    while l < r:
        while l < r and nums[r] >= mid:
            r-=1
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