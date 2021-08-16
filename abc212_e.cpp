
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

int main(){
    ll MOD = 998244353;
    int N, M, K;
    cin >> N >> M >> K;
    auto G = vector<vector<ll>>(N);
    rep(m, M) { 
        int u,v;
        cin >> u >> v; u-=1; v -= 1;
        G[u].push_back(v); G[v].push_back(u);
    }
    auto dp = vector<ll>(N, 0);
    auto ndp = vector<ll>(N, 0);
    dp[0] = 1;
    rep(k, K) {
        ll s = 0; 
        rep(j,N) s += dp[j];
        rep(n,N) {
            ndp[n] = s - dp[n];
            rep(ii, G[n].size()) ndp[n] -= dp[G[n][ii]];
            ndp[n] %= MOD;
        }
        rep(n,N) dp[n] = ndp[n];
    }
    print(dp[0]);
}
