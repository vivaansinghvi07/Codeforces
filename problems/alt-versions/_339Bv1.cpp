# include <iostream>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    int t [m];
    for (int i = 0; i < m; i++) {
        cin >> t[i];
    }
    int s = 0, i = 0, ii = 0;
    while (i < m) {
        while (s % n + 1 != t[i]) {
            s++;
        }
        while (t[i] == s % n + 1) {
            i++;
        }
    }
    cout << s << endl;
}