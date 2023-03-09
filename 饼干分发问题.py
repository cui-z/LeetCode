'''
假设你是一位很棒的家长 想给你的孩子们分发饼干 但是每个孩子最多只能给一块饼干 对于每个孩子
i,都有一个胃口值gi,这是能让孩子满足胃口的饼干的最小尺寸；对于每块饼干j,都有一个尺寸sj 如果sj>=gi
我们可以将饼干j给孩子i,这个孩子会满足，你的目标是尽可能满足更多数量的孩子，返回这个数量

例 【1,2,3】 【1,1】
只能满足一个孩子
'''
#g胃口  s饼干
#思路 贪心思路  饼干和胃口先排序，大饼干应该优先满足大胃口，逆序从大饼干开始跟大胃口比较
def slove(g_list,s_list):
    g_list.sort()
    s_list.sort()
    #饼干下biao
    s_index=len(s_list)-1
    num=0
    for index in range(len(g_list)-1,-1,-1):
        if (s_index >=0) and (s_list[s_index] >= g_list[index]):
            s_index-=1
            num+=1
    return  num
print(slove([1,2,3],[1,4]))