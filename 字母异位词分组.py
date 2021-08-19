'''
给定一个字符串数组 将字母异位词组合在一起
字母异位词是指 字母相同 但排列不同的字符串

输入 eat tea tan ate nat bat
[
[ ate eat tea]
[nat tan]
[bat]
]
'''

def slove(strs):
    res={}
    for str in strs:
        k = "".join(sorted(str))
        res[k] = res.get(k,[])+[str]
    return list(res.values())

print(slove(['eat','tea','tan','ate','nat','bat']))