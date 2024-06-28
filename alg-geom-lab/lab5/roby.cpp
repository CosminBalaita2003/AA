#include <bits/stdc++.h>

using namespace std;
struct Point {
    int x;
    int y;
};


int orientation(Point p1, Point p2, Point p3) {
    long long val = p2.x * (p3.y - p1.y) + p1.x * (p2.y - p3.y) + p3.x * (p1.y - p2.y);
    if (val == 0)
        return 0;
    else if (val > 0)
        return 1;
    else
        return -1;

}

int main ()
{
    int left = 0, right = 0, touch = 0;
    long long t;
    cin >> t;
    Point p1, p2, p3;
    Point Primul;
    cin >> p1.x >> p1.y >> p2.x >> p2.y;
    Primul=p1;
    t-=2;
    while(t!=0) {
        cin >> p3.x >> p3.y;
        int det = orientation(p1, p2, p3);
        if(det == 0) touch++;
        else if(det > 0) left++;
        else right++;
        p1 = p2;
        p2 = p3;
        t--;
        if (t==0) 
        {
            int det = orientation(p1, p2, Primul);
            if(det == 0) touch++;
            else if(det > 0) left++;
            else right++;
        }
}
    cout <<left << " " << right << " " << touch;}