#include <stdio.h>
#include <stdlib.h>
#define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
      __typeof__ (b) _b = (b); \
      _a < _b ? _a : _b; })

void solve(void) {
	int x, y, a, b, i, j, s=0;
	scanf("%d %d %d %d %d %d",&x,&y,&a,&b,&i,&j);
	if (!(a <= x && x <= i || i <= x && x <= a)) {
		if (x > a) { 
			s += min(x-a, x-i);
		} else {
			s += min(a-x, i-x);
		}
	}
	if (!(b <= y && y <= j || j <= y && y <= b)) {
		if (y > b) { 
			s += min(y-b, y-j);
		} else {
			s += min(b-y, j-y);
		}
	}
	printf("%d\n", s+1);
}
int main(void) {
	int t;
	scanf("%d", &t);
	while(t--) {
		solve();
	}
}
