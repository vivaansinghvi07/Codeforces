#include <iostream>
using namespace std;
int main() {
    int t, a, b, m;
    cin >> t;
    while (t--) {
        cin >> a >> b;
        m = min(a, b);
        cout << 2 << endl << (a < b ? m - 1: m) << " " << (a < b ? m : m - 1) << endl << a << " " << b << endl;
    }
}