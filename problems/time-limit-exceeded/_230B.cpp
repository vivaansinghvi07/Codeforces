#include <iostream>
#include <cmath>
using namespace std;
#define fill(a, n) for (int i = 0; i < n; i++) cin >> a[i];

bool prime(long long n) {
    if (n == 1) {
        return false;
    }
    for (long long i = 2; i <= (long long) sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

void solve() {
    int n;
    cin >> n;
    long long t[n];
    fill(t, n);
    for(int a = 0; a < n; a++) {
        long long i = t[a];
        if (pow((long long)sqrt(i), 2) == i and prime((long long)sqrt(i))) {
            cout << "YES";
        } else {
            cout << "NO";
        }
        cout << endl;
    }
    
}

int main() {
    int t;
    t = 1;
    while (t --> 0) {
        solve();
    }
}
