#include <iostream>
#include <algorithm>
void solve() {
	int n, m, t, x;
	std::cin >> n >> m;
	int d[n-1];
	for (int i = -1; i < n-1; i++) {
		std::cin >> x;
		if (i > -1) {
			d[i] = std::abs(t - x);
		}
		t = x;
	}
	std::sort(d, d+n-1);
	int s = 0;
	for (int i = 0; i < n-m; i++) {
		s += d[i];
	}
	std::cout << s << std::endl;
}	

int main() {
	int t; 
	std::cin >> t;
	while (t--) { 
		solve();
	}
}
