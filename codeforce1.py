import sys
import os
print(os.listdir())
input=sys.stdin.readline
sys.stdin=open('input.txt','r')
def solve():
    v,e=map(int, input().split())
    g={}
    visit=[-1 for _ in range(v)]
    for _ in range(e):
        a,b=map(int, input().split())
        g[a-1].append(b-1)
    que=[]
    for i in range(v):
        if visit[i]==-1:
            que.append(i)
            visit[i]=i
            while que:
                node=que.pop()
                for son in g[node]:
                    que.append(son)
                if visit[node]==-1:
                    