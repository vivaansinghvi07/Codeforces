#include <iostream>
using namespace std;

void solve() {
    int a, b, n, count = 0, t;
    cin >> a >> b >> n;
    while (a <= n) {
        t = a;
        a += b;
        b = max(t, b);
        count++;
    }
    cout << count << endl;
}

int main() {
    int t;
    cin >> t;
    while (t --> 0) {
        solve();
    }
}
