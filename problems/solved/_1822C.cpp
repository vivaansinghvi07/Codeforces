#include <iostream>
using namespace std;

void solve() {
    long long n;
    cin >> n;
    cout << n * n + 2 * (n + 1) << endl;
}

int main() {
    int t;
    cin >> t;
    while (t --> 0) {
        solve();
    }
}

