#include <iostream>
using namespace std;
int main() {
    int t, n, m;
    bool f;
    cin >> t;
    while (t--) {
        cin >> n;
        n--;
        int a[n];
        f = false;
        m = (int) 1e9;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            m = min(m, a[i]);
        }
        for (int i = 0; i < n; i++) {
            if (a[i] == m and !f) {
                cout << a[i] << " ";
                f = true;
            }
            cout << a[i] << " ";
        }
        cout << endl;
    }
}