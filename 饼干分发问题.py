'''
假设你是一位很棒的家长 想给你的孩子们分发饼干 但是每个孩子最多只能给一块饼干 对于每个孩子
i,都有一个胃口值gi,这是能让孩子满足胃口的饼干的最小尺寸；对于每块饼干j,都有一个尺寸sj 如果sj>=gi
我们可以将饼干j给孩子i,这个孩子会满足，你的目标是尽可能满足更多数量的孩子，返回这个数量

例 【1,2,3】 【1,1】
只能满足一个孩子
'''

def slove(g_list,s_list):
    g_list.sort()
    s_list.sort()
    num=0
    for s in s_list:
        for g in g_list:
            if s >=g:
                num+=1
                g_list.remove(g)

    return num

print(slove([1,2,3],[1,4]))