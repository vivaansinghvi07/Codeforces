# include <iostream>
using namespace std;

int main() {
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        int tea[n];
        int tasters[n];
        long long drank[n];
        for (int i = 0; i < n; i++ ) {
            cin >> tea[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> tasters[i];
            drank[i] = 0;
        }
        for (int step = 0; step < n; step++) {
            for (int i = 0; i < n - step; i++) {
                int drink = min(tea[i], tasters[i + step]);
                tea[i] -= drink;
                drank[i + step] += drink;
            }
        }
        for (int i = 0; i < n; i++) {
            cout << drank[i] << " ";
        }
        cout << endl;
    }
}