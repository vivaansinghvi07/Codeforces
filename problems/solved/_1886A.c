#include "stdio.h"
void solve(void) {
  int n;
  scanf("%d", &n);
  if (n < 7 || n == 9) {
    printf("NO\n");
  } else if (n % 3 == 0) {
    printf("YES\n%d %d %d\n", 1, 4, n-5);
  } else {
    printf("YES\n%d %d %d\n", 1, 2, n-3);
  }
}

int main(void) {
  int t = 0;
  scanf("%d", &t);
  while (t--) {
    solve();
  }
  return 0;
}
