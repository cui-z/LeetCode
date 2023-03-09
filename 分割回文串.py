"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]
"""


"""
实切割问题类似组合问题。

例如对于字符串abcdef：

组合问题：选取一个a之后，在bcdef中再去选取第二个，选取b之后在cdef中在选组第三个.....。
切割问题：切割一个a之后，在bcdef中再去切割第二段，切割b之后在cdef中在切割第三段.....。

回溯法
"""
results=[]
def slove(strings):
    result=[]
    def fun(strings,begin_index):
        if begin_index >= len(strings):
            results.append(result[:])  # 一定加：
            return
        for s in range(begin_index,len(strings)):
            tmp = strings[begin_index:s+1]
            if tmp == tmp[::-1]:
                result.append(tmp)
                fun(strings,s+1)
                result.pop()
            else:
                continue

    fun(strings,0)
    return results
slove("aab")
print(results)
