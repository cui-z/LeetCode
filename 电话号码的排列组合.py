'''

给定一个包含2-9的字符串 返回所有他能代表的字母组合
映射如下
phonne ={"2":"abc","3":"def","4":"ghi","5":'jkl',"6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
'''

def dfs(phone,strings,index,result,res):
    if len(res) == len(strings):
        result.append(res)
        return
    for char in phone[strings[index]]:
        dfs(phone,strings,index+1,result,res+char)


def slove(strings):
    phone = {"2": "abc", "3": "def", "4": "ghi", "5": 'jkl', "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result=[]
    index = 0
    res=""
    dfs(phone,strings,index,result,res)
    return result

print(slove("24"))