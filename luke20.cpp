#include <iostream>

using namespace std;

// Global
const int N = 10;
int arr[N] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0 };
long long int biggest = 0;


long long int lagInt(int a[], int m, int n) {
    long long int tall = 0;
    for (int i = m; i <= n; i++)
    tall = tall * 10 + a[i];
    return tall;
}

void sjekk(int a[]) {
    long long int b = lagInt(a, 0, 4);
    long long int c = lagInt(a, 5, 9);
    if (b * c > biggest)
        biggest = b * c;
}

void roterVenstre(int a[], int i) {
    int x, k;
    x = a[i];
    for (k = i + 1; k < N; k++)
        a[k - 1] = a[k];
    a[N - 1] = x;
}

void bytt(int & a1, int & a2) {
    int aa = a1;   a1 = a2;   a2 = aa;
}

void perm(int i) {
    int t;
    if (i == N - 1)
        sjekk(arr);
    else {
        perm(i + 1);
        for (t = i + 1; t < N; t++) {
            bytt(arr[i], arr[t]);
            perm(i + 1);
        }
        roterVenstre(arr, i);
    }
}

int main() {
    perm(0);     
    cout << biggest << endl;
    return 0;
}