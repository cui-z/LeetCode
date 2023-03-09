"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
字典里面的单词并不一定都用上

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""

def slove(str,dicts):
    dp = [False] * (len(str)+1)
    dp[0] = True

    for i in range(len(str)):
        for j in range(i,len(str)):
            if dp[i] and (str[i:j+1] in dicts):
                dp[j+1] = True
    print(dp)
    return dp[-1]

print(slove("catsandog", ["c","cats", "dog", "sand", "and", "cat"]))
print(slove("catsandog", ["cats", "og", "sand", "and", "cat"]))

