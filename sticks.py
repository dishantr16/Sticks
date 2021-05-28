for _ in range(int(input())):
    n = int(input())
    l=list(map(int,input().split()))
    num=[l[0]]
    a =[]
    for i in range(1,n):
        if(l[i] in num):
            num.remove(l[i])
            a.append(l[i])
        else:
            num.append(l[i])
    if(len(a)<2):
        print(-1)
    else:
        m= max(a)
        a.remove(m)
        n= max(a)
        print(m*n)