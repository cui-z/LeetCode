# 左括号必须用相同类型的右括号闭合
#左括号必须以正确的顺序闭合
#栈思想


def solve(s):
    resu=[]
    res={")":"(",  "]":"[",  "}":"{"}

    for char in s:
        if char in res.keys():
            if resu:
                pop_char = resu.pop()
            else:
                return False
            if pop_char != res[char]:
                return False
        else:
            resu.append(char)
    return not resu

print(solve("(){[]}"))