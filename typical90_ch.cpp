
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

ll mod = 1000000007;
ll N, Q;
ll X[100], Y[100], Z[100], W[100];
ll x[100], y[100], z[100], w[100];

ll bit_zentansaku() {
    ll ways = 0;
    rep(i, 1<<N) {
        ll bit[15];
        for (int j = 0; j < N; j++) bit[j + 1] = (i / (1 << j)) % 2;

        bool flag = true;
        rep(j, Q) {
            if (((bit[x[j]] | bit[y[j]]) | bit[z[j]]) != w[j]) flag = false;
        }
        if (flag == true) ways++;
    }
    return ways;
}

int main() {
    // Step #1. Input
    cin >> N >> Q;
    rep(i, Q) cin >> X[i] >> Y[i] >> Z[i] >> W[i];

    // Step #2. Brute Force
    ll Answer = 1;
    rep(i, 60) { // i桁目を検証する
        rep(j, Q) {
            x[j] = X[j]; y[j] = Y[j]; z[j] = Z[j];
            w[j] = (W[j] / (1LL << i)) % 2LL; // i桁目のとき, wの評価は W[j] // (1LL << i)と等しい
        }
        ll ret = bit_zentansaku();
        Answer *= ret;
        Answer %= mod;
    }
    cout << Answer << endl;
    return 0;
}
