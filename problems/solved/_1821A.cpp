#include <iostream>
using namespace std;

#define farr(a, n) for(int i = 0; i < n; i++) cin >> a[i];

void solve() {
    int n, l, r;
    cin >> n;
    int a[n];
    int b[n];
    farr(a, n);
    farr(b, n);
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) {
            l = i;
            break;
        }
    }
    for (int i = n - 1; i >= 0; i--) {
        if (a[i] != b[i]) {
            r = i;
            break;
        }
    }
    for (int i = l; i >= 0; i--) {
        if (b[i - 1] > b[i] or i == 0) {
            l = i;
            break;
        }
    }
    for (int i = r; i < n; i++) {
        if (b[i + 1] < b[i] or i == n - 1) {
            r = i;
            break;
        }
    }
    cout << l+1 << " " << r+1 << endl;
}

int main() {
    int t;
    cin >> t;
    while (t --> 0) {
        solve();
    }
}
