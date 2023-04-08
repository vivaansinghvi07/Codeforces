#include <iostream>

using namespace std;
long long int M = 1000000007;

void solve() {
    int len;
    cin >> len;
    int a[len];
    int map[len];
    bool found[len];
    int loops = 0;
    for (int i = 0; i < len; i++) {
        cin >> a[i];
        found[i] = false;
    }
    for (int i = 0; i < len; i++) {
        int x;
        cin >> x;
        map[a[i]-1] = x - 1;
    }
    for (int i = 0; i < len; i++) {
        int ii = i;
        if (found[i]) continue;
        while (true) {
            found[ii] = true;
            ii = map[ii];
            if (found[ii]) {
                loops++;
                break;
            }
        }
    }
    int ans = 1;
    for (int i = 0; i < loops; i++) {
        ans = ans * 2 % M;
    }
    cout << ans << endl;
}

int main() {
    int n;
    cin >> n;
    while (n--) {
        solve();
    }
}