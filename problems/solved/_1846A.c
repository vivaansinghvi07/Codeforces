#include <stdio.h>
void solve(void) {
	int a, b, n, i = 0;
	scanf("%d", &n);
	while(n--) {
		scanf("%d %d", &a, &b);
		i += a > b;
	}
	printf("%d\n", i);
}

int main(void) {
	int t;
	scanf("%d", &t); 
	while(t--) {
		solve();
	}
	return 0;
}