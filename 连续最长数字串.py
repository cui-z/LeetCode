#在字符串中找出连续最长的数字串


def slove(s):
    res1=[]
    res2=[]
    for char in s:
        if char in ['1','2','3','4','5','6','7','8','9']:
            res1.append(char)
        else:
            if len(res2) > len(res1):
                pass
            else:
                res2 = res1
                res1 = []
    return  res2

print(slove("asfj35sdvfj0q2349vadfs"))