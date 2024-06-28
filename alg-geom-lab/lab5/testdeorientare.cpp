#include <bits/stdc++.h>
using namespace std;
long long t, xP,yP, xQ, yQ, xR, yR;
int main() {
    cin >> t;
    while(t!=0) {
        cin >> xP >> yP >> xQ >> yQ >> xR >> yR;
        // long long det = xQ*yR + xP*yQ + xR*yP - xR*yQ - xP*yR - xQ*yP;
        long long det = xQ*(yR-yP) + xP*(yQ-yR) +xR*(yP-yQ);
        if(det == 0) {
            cout << "TOUCH\n";
        } else if(det > 0) {
            cout << "LEFT\n";
        } else {
            cout << "RIGHT\n";
        }
        t--;
    }
    return 0;
}