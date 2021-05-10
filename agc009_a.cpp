
#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>


using namespace std;
using ll=long long;
const long long INF = 1LL << 60;
template<class T> void chmin(T& a, T b) { if(a > b) { a = b; } }
template<class T> void Sort(vector<T>& input) { std::sort(input.begin(), input.end()); }

int main() {
    int N; 
    cin >> N;
    vector<ll> A(N), B(N);
    for(int i=0; i<N; i++) cin >> A[i] >> B[i];
    ll sum = 0;
    for(int i=N-1; i >= 0; --i) {
        A[i] += sum;
        ll amari = A[i]%B[i];
        ll D=0;
        if(amari != 0) D = B[i] - amari;
        sum+=D;
    }
    cout << sum << endl;
}