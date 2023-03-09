'''
给定一个字符串S和一个字符串T,请在S中找出包含T所有字母的最小子串


'''

#需要看代码理解

def slove(s,t):
    res =""
    d={}
    for char in t:
        d[char]=d.get(char,0)+1
    l=0
    r=0
    count=0
    min_len = len(s)
    while r < len(s)-1:
        if s[r] in d:
            d[s[r]]=d.get(s[r])-1
            if d.get(s[r]) >=0:
                count+=1
            while count == len(t):
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                if s[l] in d:
                    d[s[l]]+=1
                    if d[s[l]] >0:
                        count-=1
                l+=1
        r+=1
    return  res

print(slove("avfcdtfasf","vcd"))