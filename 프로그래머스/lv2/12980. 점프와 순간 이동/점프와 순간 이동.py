def solution(n):
    t = 0
    while n>0:
        if n%2==0:
            n=n/2
        elif n%2==1:
            n -=1
            t +=1
    return t