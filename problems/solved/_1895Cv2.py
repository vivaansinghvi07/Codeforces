n,a,o,s,m,r,l,e,h=(i:=int)(input()),input().split(),0,sum,map,range,len,{1:{3:{},5:{}},2:{4:{}},3:{5:{}}},{1:{},2:{},3:{},4:{},5:{}}
for x in a:
    for j in r(1+((D:=l(x))%2==0),D+1,2): h[j][y]=h[j].get((y:=s(m(i,x[(c:=2-j//2-(3==D)-(D==2)-2*(D==1)):]))-s(m(i,x[:c]))),0)+1
    if D<4:e[D][D+2][y]=e[D][D+2].get(y,0)+1
    if D==1:e[D][D+4][y]=e[D][D+4].get(y,0)+1
print(s([h[(D:=l(x))].get(s(m(i,x)),0)+s([e[D-2-((-1-j)*2)][D].get(s(m(i,x[:j]))-s(m(i,x[j:])),0)for j in r(-1,-D//2,-1)])for x in a]))
