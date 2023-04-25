#include <iostream>
using namespace std;
int main() {
    int t, n, s, m, x, d;
    cin >> t;
    while (t--) {
        cin >> n >> s;
        int a[n]; 
        m = -1; d = -1;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        } 
        for (int i = 0; i < n; i++) {
            cin >> x;
            if (a[i] + i <= s && x > m) { 
                m = x;
                d = i+1;
            }
        }
        cout << d << endl;
    }
}