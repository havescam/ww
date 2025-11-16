#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<vector<int>> grid{
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    };

    // Печать построчно с суммой каждой строки
    for (size_t i = 0; i < grid.size(); ++i) {
        int rowSum = 0;
        cout << "row " << i << ": ";
        for (int x : grid[i]) {
            cout << x << ' ';
            rowSum += x;
        }
        cout << "| sum=" << rowSum << '\n';
    }
    return 0;
}
