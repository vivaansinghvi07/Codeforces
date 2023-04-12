# include <iostream>
using namespace std;
int main()                                      {
    int t, a, b, c                              ;
    cin >> t                                    ;
    while (t--)                                 {
        cin >> a >> b                           ;
        a = abs(a); b = abs(b); c = abs(b-a)    ;
        cout << a + b + max(c-1, 0) << endl     ;}}