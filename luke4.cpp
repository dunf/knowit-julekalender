#include <iostream>
#include <string>

using namespace std;

int tall[1338];
int a = 1;

bool contains7(int n) {
    string b = to_string(n);
    size_t f = b.find('7');
    return (f != string::npos) ? true : false;
}
void luke4() {
    int j = 1;
    int tallrekke[1338]; 
    for (int i = 1; i <= 1338; i++) 
        tallrekke[i] = (i % 7 == 0 || contains7(i)) ? tallrekke[j++] : i;
    cout << "Solution: " << tallrekke[1337] << "\n";
}
void luke4rekursiv(int n) {
    if (n < 1338) {
        tall[n] = (n % 7 == 0 || contains7(n)) ? tall[a++] : n;
        luke4rekursiv(n+1);
    }
}
int main() {
    luke4();
    luke4rekursiv(1);
    cout << "Solution: " << tall[1337] << "\n";
    return 0;
}