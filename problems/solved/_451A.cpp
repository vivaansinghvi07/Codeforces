# include <iostream>
using namespace std;
int main() {
    int l, w;
    cin >> l >> w;
    cout << (min(l, w)%2 ? "Akshat": "Malvika") << endl;
}