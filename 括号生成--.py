"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


画图 可得  如果左括号的数量<右括号数量   那么一定失败

回溯 :通过确保每一步都能够实现有效序列，尽早实现剪枝；

我们首先找到回溯的出口条件：当左右括号都达到最大数量n时，加入结果集；
接下来以左括号开始，不断判断两个条件进行递归调用,直到满足出口条件：
    （1）左括号是否达到最大数量n; 若小于，则使左括号数量加一，路径加上'(';
     (2)左括号个数是否大于右括号个数; 若大于，则使右括号数量加一，路径加上')';


回溯法的模板
res = []    # 定义全局变量保存最终结果
state = []  # 定义状态变量保存当前状态
p,q,r       # 定义条件变量（一般条件变量就是题目直接给的参数）
def back(状态，条件1，条件2，……):
    if # 不满足合法条件（可以说是剪枝）
        return
    elif # 状态满足最终要求
        res.append(state)   # 加入结果
        return
    # 主要递归过程，一般是带有 循环体 或者 条件体
    for # 满足执行条件
    if  # 满足执行条件
        back(状态，条件1，条件2，……)
back(状态，条件1，条件2，……)
return res


"""

def slove(n):
    result =[]

    def dfs(result,n,l_num,r_num,strs):
       #  print(result,n,l_num,r_num,strs)
         if l_num < r_num:
             return
         if l_num == r_num ==n:
             result.append(strs)
             return
         if l_num < n:
             dfs(result,n,l_num+1,r_num,strs+"(")
         if  r_num < l_num:
             dfs(result,n,l_num,r_num+1,strs+")")
    dfs(result,n,0,0,"")
    return result

print(slove(3))


