# 给定两个整数 n 和k,返回1...n中所有可能的k个数的组合

#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

# def solve(n,k):
#     result=[]
#     def solve01(result,first=1,curr=[]):
#         if len(curr) == k:
#
#             #切片运算符[:]返回一个序列的切片。切片过程是切下列表的一部分，创建新的列表，将切下的部分复制到新列表。
#             result.append(curr[:])
#             return
#         for i in range(first,n+1):
#             curr.append(i)
#             solve01(result,i+1,curr)
#             curr.pop()
#     solve01(result,1,[])
#     return  result
#
# print(solve(4,2))

def slove(n,k):
    result= []

    def fun(result,n_list,tmp_list):
        if len(tmp_list) == k:
            result.append(tmp_list)
            return
        for i in range(len(n_list)):
            fun(result,n_list[i+1:],tmp_list+[n_list[i]])

    fun(result,[i for i in range(1,n+1)],[])

    return result

print(slove(4,2))


