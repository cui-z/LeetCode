"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3] nums2 = [2]

则中位数是 2.0 示例 2:

nums1 = [1, 2] nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5


解析在 https://zhuanlan.zhihu.com/p/70654378
"""
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        print(j)
        print("----")
        if i != m and B[j-1] > A[i]:
            # i 的值太小， 增加它
            imin = i + 1
        elif i != 0 and A[i-1] > B[j]:
            # i 的值过大， 减小它
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0

print(median([1,3],[2,5,8,9]))