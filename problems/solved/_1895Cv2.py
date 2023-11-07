n,a,o = int(input()), input().split(),0
e,h={1:{3:{},5:{}},2:{4:{}},3:{5:{}}},{1:{},2:{},3:{},4:{},5:{}}
for x in a:
    D,i=len(x),int(x)
    for j in range(1+(D%2==0),D+1,2):
        c=2-j//2-(3==D)-(D==2)-2*(D==1)
        y=sum(map(int,x[c:]))-sum(map(int,x[:c]))
        h[j][y]=h[j].get(y,0)+1
    if D<4:e[D][D+2][y]=e[D][D+2].get(y,0)+1
    if D==1:e[D][D+4][y]=e[D][D+4].get(y,0)+1
print(sum([h[(D:=len(x))].get(sum(map(int,x)),0)+sum([e[D-2-((-1-j)*2)][D].get(sum(map(int,x[:j]))-sum(map(int,x[j:])),0)for j in range(-1,-D//2,-1)])for x in a]))
