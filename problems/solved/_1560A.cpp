#include <iostream>
using namespace std;
#define fill(a, n) for (int i = 0; i < n; i++) cin >> a[i];

void solve() {
    int n, s = 0, i = 0;
    cin >> n;
    while(s < n) {
        if (!(i % 3 == 0 or i % 10 == 3)) {
            s++;
        }
        i++;
    }
    cout << i-1 << endl;
}

int main() {
    int t;
    cin >> t;
    while (t --> 0) {
        solve();
    }
}
