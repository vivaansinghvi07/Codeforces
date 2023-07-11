#include <iostream>
using namespace std;
void solve(){
	int n,t,x,i,s;
	cin>>n>>t;
	for(i=s=0;i<n-1;i++){
		cin>>x;
		if(t==0){
			s+=1;
			t=x; 
		}
		else {
			t&=x;
		}
	}
	if(t==0){
		s+=1;
	}
	cout<<max(s,1)<<endl;
}
int main(){
	int t;
	cin>>t;
	while(t--){
		solve();
	}
}
