#include <iostream>
using namespace std;
#define YES cout << "YES" << endl
#define NO cout << "NO" << endl


void solve() {
	long long a, b, c;
	cin >> a >> b >> c;
	bool d, e, f; 
	double j = ((c-a)/2.0+a);
	d = (int)j == j and (int)j % b == 0 and ((c-a)/2+a) / b != 0;
	e = (b-a+b) % c == 0 and (b-a+b) / c > 0;	
	f = (b-c+b) % a == 0 and (b-c+b) / a > 0;
	if (d||e||f)
		YES;
	else
		NO;
}

int main() {
	int t; cin >> t;
	while (t--) {
		solve();
	}
}
