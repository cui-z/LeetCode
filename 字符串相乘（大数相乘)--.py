"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

"""

"""
思路：
    23 *56
        2      3
        5      6
——————
       （12）（18）
（10）  （15）
（10）  （27）（18）
  12         8      8
  
我们可以先不考虑进位，当所有位对应相加，产生结果之后，再考虑。从右向左依次累加，如果该位的数字大于10，那么我们用取余运算，在该位上只保留取余后的个位数，
而将十位数进位（通过模运算得到）累加到高位便可，循环直到累加完毕。

因为乘法是从 最后一个数字开始 所以第一步先反转 然后按照下表进行相乘 相加 最后再处理 
"""

def slove(str1,str2):
    str1 = str1[::-1]
    str2 = str2[::-1]

    result = [0 for _ in range(len(str1)+len(str2))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            result[i+j] += int(str1[i])*int(str2[j])

    for n in range(len(result)):
        if result[n] > 9:
            result[n+1] += result[n]//10
            result[n] = result[n] % 10
    result.reverse()
    return int("".join([str(i) for i in result]))

print(slove("23","56"))
