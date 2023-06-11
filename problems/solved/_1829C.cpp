#include <iostream>
using namespace std;
#define fill(a, n) for (int i = 0; i < n; i++) cin >> a[i];

void solve() {
    int ii=1000000, oi=1000000, io=1000000, n, x, s;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        cin >> s;
        if (s == 10) {
            io = min(io, x);
        } else if (s == 11) {
            ii = min(ii, x);
        } else if (s == 1) {
            oi = min(oi, x);
        }
    }
    bool a = io == 1000000 or oi == 1000000;
    bool b = ii == 1000000;
    if (a and b) {
        cout << -1;
    } else if (a) {
        cout << ii;
    } else if (b) {
        cout << oi + io;
    } else {
        cout << min(ii, oi + io);
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t --> 0) {
        solve();
    }
}
