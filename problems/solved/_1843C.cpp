#include <iostream>
using namespace std;

void solve() {
	long long n; cin >> n;
	long long s = n;
	while (n > 1) {
		s += n /= 2; 
	} 	
	cout << s << endl;
}

int main() {
	int t; cin >> t;
	while (t--) {
		solve();
	}
}
