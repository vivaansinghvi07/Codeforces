# include <iostream>
using namespace std;
int main() {
    long long n, m;
    cin >> n >> m;
    long long s = 0, t = 1;
    while (m--) {
        long long x; cin >> x;
        long long d = (x - t) >= 0 ? (x - t) % n : (x - t) % n + n;
        s += d;
        t = x;
    }
    cout << s << endl;
}