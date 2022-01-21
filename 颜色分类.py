"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地**对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]


对数组进行两次遍历，考虑使用单指针 ptr 进行遍历，第一次遍历中需要把所有的 0 交换到数组的 头部，每交换一次，ptr 向右移动一位，直
到遍历结束，此时 ptr 之前的元素都为 0；第二次遍历从 ptr 开始遍历，将所有的 1 交换到中间位置，每交换一次，ptr 向后移动一位，直到遍
历结束，此时 ptr 之后 （包括 ptr）的元素都为 2，排序完成

"""

def  slvoe(nums):

    pre = 0
    for i in range(len(nums)):
        if nums[i] ==0:
            nums[pre] ,nums[i] = nums[i],nums[pre]
            pre+=1

    for i in range(pre,len(nums)):
        if nums[i] ==1:
            nums[pre], nums[i] = nums[i], nums[pre]
            pre += 1


    return nums

print(slvoe([0,1,0,1,1,2,2,0,1]))