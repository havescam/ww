#include <bits/stdc++.h>
using namespace std;

// Рекурсивная проверка по индексу i (слева направо)
bool isSortedRec(const vector<int>& a, int i = 1) {
    if (i >= (int)a.size()) return true;          // база: дошли до конца — отсортирован [web:2]
    if (a[i-1] > a[i]) return false;              // нарушение порядка — не отсортирован [web:2]
    return isSortedRec(a, i + 1);                 // рекурсивно проверяем следующий соседний парный элемент [web:2]
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Примеры
    vector<int> v1 = {};                          // True [web:2]
    vector<int> v2 = {1};                         // True [web:2]
    vector<int> v3 = {1, 2, 2, 5};                // True [web:2][web:3]
    vector<int> v4 = {1, 3, 2};                   // False [web:2][web:3]

    cout << boolalpha;
    cout << isSortedRec(v1) << "\n";
    cout << isSortedRec(v2) << "\n";
    cout << isSortedRec(v3) << "\n";
    cout << isSortedRec(v4) << "\n";

    return 0;
}

Результат работы:
true
true
true
false
