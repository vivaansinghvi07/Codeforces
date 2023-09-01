#include <stdlib.h>
#include <stdio.h>

void solve(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n / 2; i++) {
		if (i == n / 2 - 1 && n % 2 == 1) {
			printf("%d %d %d", i*2+3, i*2+1, i*2+2);
		}	
		else {
			printf("%d %d ", i*2+2, i*2+1);
		}
	}
	printf("\n");
}

int main(void) {
	int t;
	scanf("%d", &t);
	while (t--) { 
		solve();
	}
}
