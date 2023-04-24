#include <iostream>
using namespace std;
int main() {
    int n, l, r, s, d, x;
    bool t = true;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    l = 0; r = n - 1;
    s = 0; d = 0;
    while (l <= r) {
        if (a[l] > a[r]) {
            x = a[l];
            l++;
        } else {
            x = a[r];
            r--;
        }
        if (t) {
            s += x;
        } else {
            d += x;
        }
        t = !t;
    }
    cout << s << " " << d << endl;
 }