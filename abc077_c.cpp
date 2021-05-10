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
    int N = 0;
    cin >> N;
    vector<int> A(N, 0);
    vector<int> B(N, 0);
    vector<int> C(N, 0);
    for(int i=0; i<N; i++) {
        cin >> A[i];
    }
    Sort(A);
    for(int i=0; i<N; i++) {
        cin >> B[i];
    }
    Sort(B);
    for(int i=0; i<N; i++) {
        cin >> C[i];
    }
    Sort(C);

    ll ans = 0;
    for(int b: B){
        auto b_idx_num = lower_bound(A.begin(),A.end(),b) - A.begin(); // bより大きい最大の境界
        auto c_idx_num = C.end() - upper_bound(C.begin(),C.end(),b); // bより小さい最小の境界
        ans += b_idx_num * c_idx_num;
    }
    cout << ans << endl;
}