//Массив на C++
#include <iostream>
using namespace std;
int main() {
    const int n = 7;
    int a[n];
    for(int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    return 0;
}


//Cтек на C++
#include <iostream>
#include <stack>
using namespace std;
int main()
{
    stack<string>st;
    st.push("a");
    st.push("b");
    st.push("c");
    cout << "stack size: " << st.size() << endl;
}
