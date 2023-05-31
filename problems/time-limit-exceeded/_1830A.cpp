#include <iostream>
using namespace std;
#define fill(a, n) for (int i = 0; i < n; i++) cin >> a[i];
#define iton(n) for (int i = 0; i < n; i++)
#define jton(n) for (int i = 0; i < j; j++)

bool all(bool arr[], int n) {
    iton(n) {
        if (not arr[i]) {
            return false;
        }
    }
    return true;
}

void solve() {
    int n, i = 0, c = 0; 
    cin >> n;
    bool drawn [n];
    int a [n-1];
    int b [n-1];
    iton(n) {
        drawn[i] = false;
    }
    drawn[0] = true;
    iton(n*2-2) {
        if (i % 2 == 1) {
            cin >> b [i / 2];
        }
        else {
            cin >> a [i / 2];
        }
    }
    while (not all(drawn, n)) {
        iton(n-1) {
            int x = a[i]-1, y = b[i]-1;
            if (drawn[x] or drawn[y]) {
                drawn[x] = true; 
                drawn[y] = true;
            }
        }
        i++;
    }
    cout << i << endl;
}

int main() {
    int t;
    cin >> t;
    while (t --> 0) {
        solve();
    }
}
