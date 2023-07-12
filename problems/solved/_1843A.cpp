#include <iostream>

using namespace std;

void solve() {
	int n; cin >> n;
	int a[n];
	for (int i=0;i<n;i++) {cin>>a[i];}
	sort(a, a+n);
	int b = 0;
	for (int i=0;i<n/2;i++) {
		b = b + a[n-i-1] - a[i];
	}
	cout << b << endl;
}

int main() {
	int t; cin >> t;
	while(t--) {solve();}	
}