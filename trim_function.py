# -*- coding: utf-8 -*-


def trim(s):

    length=len(s)
    print(length)
    i=0
    j=length

    if length >0:
        while i<length and s[i]==' ':
            i=i+1
            print(i)
        p=i
        print(p)

        while  s[j-1]==' ':
            j=j-1
        q=j
        print(q)
        return s[p:q]
    else:
        print('字符串长度不能为0')


str='    woshilimenglong       '
# x=len(str)
# print('x=%d'%x)
# v=str[0]
# print('字符串:%s'%str[1:])
# f=str[5:10]
# print(f)
a=trim(str)
print('截取字符串空格后结果：%s'%a)