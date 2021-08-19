

#子串必须是连续的  所以要判断当前字符跟前面是不是有重复  如果没有重复 长度加1  继续下一个
#如果重复 初始的要处理  长度也要记录

def slove(nums):
    resu=[]
    begin = 0
    for i in range(1,len(nums)):
        res=nums[begin:i]
        if nums[i] in res:
            begin = begin+ res.index(nums[i])+1
            resu.append(i-begin+1)
        else:
            resu.append(i-begin)
    return max(resu)


print(slove("abcabcbb"))