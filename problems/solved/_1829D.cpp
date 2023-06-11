#include <iostream>
using namespace std;
#define fill(a, n) for (int i = 0; i < n; i++) cin >> a[i];

bool valid(int n, int m) {
    if (n == m) {
        return true;
    } else if (m > n or n % 3) {
        return false;
    } else {
        return valid( (int) n / 3, m ) or valid ( (int) (n / 3) * 2, m );
    }
}

int main() {
    int t, n, m;
    cin >> t;
    while (t --> 0) {
        cin >> n >> m;
        cout << (valid(n, m) ? "YES" : "NO") << endl;
    }
}
