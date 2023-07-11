#include <iostream>
#include <algorithm>
void solve() {
	int n, m, h, i, j, s, t;
	std::cin >> n >> m >> h;
	int comp[n][m];
	for (i = 0; i < n; i++) { 
		for (j = 0; j < m; j++) { 
			std::cin >> comp[i][j];
		}	
		std::sort(comp[i], comp[i] + m);
	}
	int scores[n];
	int pens[n];
	for (i = 0; i < n; i++) {
		s = 0; t = 0; j = 0;
		while (t <= h && j < m) {
			t += comp[i][j];
			s += t;
			j++;
		}
		if (t<=h) {
			pens[i] = s;
			scores[i] = j;
		}
		else {
			pens[i] = s - t;
			scores[i] = j - 1;
		}
	}
	for (i = 0; i < n; i++) {
		std::cout << pens[i] << ' ' << scores[i] << std::endl;
	}
	std::cout << std::endl;
}
int main() {
	int t;
	std::cin >> t;
	while(t--) {
		solve();
	}
}
