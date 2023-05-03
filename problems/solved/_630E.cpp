#include <iostream>
using namespace std;
int main() {
    long long x, xx, y, yy;
    cin >> x >> y >> xx >> yy;
    cout << (xx-x+1)*(yy-y+1)/2+1 << endl;
}