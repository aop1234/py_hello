## 添加一个字符可以形成回文的字符串判断

from timeit import timeit  

# by george
def f(str):
    result = True
    m=0
    n=-1
    fill_count = 0  # 补字符数量
    for i in range(len(str)//2 + len(str)%2):
        if(str[m]==str[n]):
            m += 1
            n -= 1
        else:
            fill_count += 1
            if(fill_count>1): # 如果须补字符数量大于1，提前退出
                result = False
                break

            if(str[m]==str[n-1]):  # 如果（左端）和（右端-1）匹配，补左端
                n -= 1
            elif(str[m+1]==str[n]):  # 如果（左端+1）和（右端）匹配，补右端
                m += 1
            else:
                result = False
    
    return result

# by Tang-ZhiXiong
def is_palindrome(str):
    str_1=str
    str_2=str_1[::-1]
    str_len=len(str)
    addLetter=list(set(list(str_1)))
    for i in range(str_len):
        for al in addLetter:  
            if str_1[:i]+al+str_1[i:]==str_2[:str_len-i]+al+str_2[str_len-i:]:
                return 'YES'
    return 'NO'


# by Wang-XingHai
def isp(string):    
    added = False # 是否已经添加单个字符
    def isp_(str):
        nonlocal added
        if str =='' or len(str)==1:
            return True
        else:
            if(str[0]==str[-1]):
                return isp_(str[1:-1])
            else:
                if added: 
                    return False
                added = True
                return isp_(str[-1]+str[:]) or isp_(str[:]+str[0])                    
    return 'YES' if isp_(string) else 'NO'


print('should be True', 'f:', f('evel'))
print('should be True', 'f:', f('noon'))
print('should be True', 'f:', f('abcdefghijklmnopqrstuvwxyzABzyxwvutsrqponmlkjihgfedcba'))
print('should be False', 'f:', f('nov'))
print('should be True', 'f:', f('novo'))
print('should be False', 'f:', f('noane'))

print(timeit("f('abcdefghijklmnopqrstuvwxyzABzyxwvutsrqponmlkjihgfedcba')",'from __main__ import f',number=10000))
print(timeit("isp('abcdefghijklmnopqrstuvwxyzABzyxwvutsrqponmlkjihgfedcba')",'from __main__ import isp',number=10000))
print(timeit("is_palindrome('abcdefghijklmnopqrstuvwxyzABzyxwvutsrqponmlkjihgfedcba')",'from __main__ import is_palindrome',number=10000))

