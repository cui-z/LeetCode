'''
给定一个字符串 计算字符串中有多少个回文子串
具有不同开始位置和结束位置的子串  即使字符相同 也会被认为不同的子串
'''

def slove(s):
    result = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] ==s[i:j][::-1]:
                result+=1
    return  result

print(slove("aaa"))