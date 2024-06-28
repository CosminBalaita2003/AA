#include <bits/stdc++.h>
using namespace std;

//functie care calculeaza virajul dintre 3 puncte
long long viraj(long long xP, long long yP, long long xQ, long long yQ, long long xR, long long yR) {
    return xQ * yR + xP * yQ + xR * yP - xR * yQ - xP * yR - xQ * yP;
}


//functie care compara 2 puncte in functie de coordonatele lor
bool cmp(pair<int, int>& p1, pair<int, int>& p2) {
    if (p1.first == p2.first)
        return p1.second < p2.second;
    return p1.first < p2.first;
}

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }

    sort(points.begin(), points.end(), cmp); //sortam punctele pentru a putea aplica algoritmul lui Graham

    vector<pair<int, int>> poligon; //vectorul in care vom retine punctele care formeaza acoperirea convexa

    
    for (int i = 0; i < n; i++) {
        while (poligon.size() >= 2 && viraj(poligon[poligon.size() - 2].first, poligon[poligon.size() - 2].second,
            poligon[poligon.size() - 1].first, poligon[poligon.size() - 1].second,
            points[i].first, points[i].second) <= 0) //daca virajul este mai mic sau egal cu 0, eliminam ultimul punct din poligon
            //echivalent cu a elimina ultimul punct din acoperirea convexa
            {
            poligon.pop_back(); //eliminam ultimul punct din poligon
        }
        poligon.push_back(points[i]);  //adaugam punctul curent in poligon
    }


    int t = poligon.size() + 1;//retinem numarul de puncte din poligon pentru a sti cand sa ne oprim
    
    //parcurgem punctele in ordine inversa pentru a adauga punctele care formeaza acoperirea convexa in ordinea corecta
    for (int i = n - 2; i >= 0; i--) {
        while (poligon.size() >= t && viraj(poligon[poligon.size() - 2].first, poligon[poligon.size() - 2].second,
            poligon[poligon.size() - 1].first, poligon[poligon.size() - 1].second,
            points[i].first, points[i].second) <= 0)  
            {
            poligon.pop_back();
        }
        poligon.push_back(points[i]);
    }

    //eliminam ultimul punct din poligon deoarece acesta este primul punct adaugat in poligon
    poligon.pop_back();

    cout << poligon.size() << endl;
    for (auto p : poligon) {
        cout << p.first << " " << p.second << endl;
    }

    return 0;
}