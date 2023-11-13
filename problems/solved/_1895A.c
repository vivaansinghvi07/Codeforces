#include <stdio.h>

void solve(void) {
  int x, y, z;
  scanf("%d %d %d", &x, &y, &z);
  if (x + z > y) {
    printf("%d ", x > y ? x : y);
  } else {
    printf("%d ", y + y - x - z);
  }
}

int main(void) {
  int t;
  scanf("%d", &t);
  while(t--){
    solve();
  }
}
