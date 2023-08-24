#include <stdlib.h>
#include <stdio.h>
void solve(void) {
    int n, a, b, i, m = 0, o;
    scanf("%d", &n);
    i = n;
    while (n--) {
        scanf("%d %d", &a, &b);
        if (a > 10) {
            continue;
        } 
        if (b > m) {
            o = i - n; 
            m = b;
        }
    }
    printf("%d ", o);
}
int main(void) {
    int t;
    scanf("%d", &t);
    while (t--) {
        solve();
    }
    return 0;
}