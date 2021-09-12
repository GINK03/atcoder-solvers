
#include<iostream>
#include<algorithm>
#include<vector>
#include<bits/stdc++.h>
#include<cmath>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define print(s) std::cout << s << std::endl;
#define vec std::vector;
using namespace std;
using ll=long long;
const long long INF = 1LL << 60;
template<class T> void chmin(T& a, T b) { if(a > b) { a = b; } }
template<class T> void Sort(vector<T>& input) { std::sort(input.begin(), input.end()); }
template<class T> std::vector<T> mk_vec(int size,T init) { return std::vector<T>(size, init); }
template<class T> std::vector<std::vector<T>> mk_mat(int H, int W, T init) { return std::vector<std::vector<T>>(H, std::vector<T>(W, init)); }

ll L, Q;
vector<ll> C, X;
int main() {
    cin >> L >> Q;
    C = vector<ll>(Q, 0);
    X = vector<ll>(Q, 0);
    
    vector<ll> tmp = {0, L};
    rep(q, Q) {
        cin >> C[q] >> X[q];
        if( C[q] == 1L ) {
            auto idx = lower_bound(tmp.begin(), tmp.end(), X[q]);
            tmp.insert(idx, X[q]);
        } else { 
            /*for( auto a: tmp ) {
                cout << a << " ";
            }
            cout << endl;*/
            auto idx = lower_bound(tmp.begin(), tmp.end(), X[q]);
            cout << tmp[idx-tmp.begin()] - tmp[idx-1-tmp.begin()] << endl;
            
        }
    }

}
