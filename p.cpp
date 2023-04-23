#include <iostream>
using namespace std;
int main() {
    long long t, a, b, c;
    cin >> t;
    while (t--) {
        cin >> a >> b;
        if (b == 1) {
            cout << "NO" << endl;
            continue;
        }
        c = a * b * 2;
        cout << "YES" << endl;
        cout << a << " " << c - a << " " << c << endl;
    }
}