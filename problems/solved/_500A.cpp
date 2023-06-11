#include <iostream>
using namespace std;
#define fill(a, n) for (int i = 0; i < n; i++) cin >> a[i];
int main() {
    int n, a, i=1;
    cin >> n >> a;
    int arr[n-1];
    fill(arr, n-1);
    while (i <= a) {
        if (i == a) {
            cout << "YES" << endl;
            return 0;
        }
        i += arr[i-1];
    }
    cout << "NO" << endl;
}