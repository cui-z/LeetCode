'''

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
————————————————
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

输出: [1,2,2,3,5,6]

'''

def slove(nums1,m,nums2,n):
    p1 = m-1
    p2 = n-1
    p = m+n-1

    while p1 >=0 or p2 >=0:
        if p1 < 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        elif p2 < 0:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1

        elif nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
        elif nums1[p1] <= nums2[p2]:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

    return  nums1




print(slove([1,2,3,0,0,0],3,[2,5,6],3))