'''
编写一个函数来查找字符串数组中的最长公共前缀

["flower","flow","fligint"]

"fl"
'''

#筛选出一个最短的去比较就可以了


def slove(strings):
    min_string = min(strings,key=len)

    for i in range(len(min_string)):
        for str in strings:
            if min_string[i] == str[i]:
                pass
            else:
                return min_string[:i]
    return min_string

print(slove(["abc","ab","abv"]))

