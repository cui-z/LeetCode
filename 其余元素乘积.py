#给一个长度为n的整数数组nums，返回输出数组output,其中output[i] = nums中除了nums[i]之外其余各元素的乘积
# 不能使用chu法  复杂度为n

# 从左到右 乘一边  然后从右到左乘一遍 然后想乘

def slove(nums):
    #result=[1]*len(nums)
    res1=[1]
    for i in range(1,len(nums)):
        res = res1[-1]*nums[i-1]
        res1.append(res)

    print(res1)
    res=1
    for j in range(len(nums)-1,-1,-1):
        if j == (len(nums)-1):
            res=1
        else:
            res=res*nums[j+1]
        res1[j] =res1[j]*res
    return  res1

print(slove([1,2,3,4]))








#例如【1,2，3,4】  当求位置3时，就相当于从左边数的乘积 * 右边数的乘积先把左边的存起来  然后把右边的跟他撑起来就行