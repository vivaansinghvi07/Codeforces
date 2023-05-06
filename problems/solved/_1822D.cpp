#include <iostream>
using namespace std;

void solve() {
    int n;
    cin >> n;
    if (n == 1) {
        cout << 1 << endl;
        return;
    } else if (n % 2 == 1) {
        cout << -1 << endl;
        return;
    }
    cout << n << " ";
    for (int i = n-1; i >= 1; i--) {
        if (i % 2 == 0) {
            cout << n - i << " ";
        } else {
            cout << i << " ";
        }
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

// turn 8 into
// 8 7 2 5 4 3 6 1
