

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

int main() {
    int N, M; cin >> N >> M;
    auto G = mk_mat<ll>(N, N, INF);
    rep(m, M) {
        int u, v, c; cin >> u >> v >> c;
        u-=1; v-=1;
        G[u][v] = c;
    }
    // 同じノード上の距離は0とする
    rep(i, N) {
        G[i][i] = 0;
    }

    ll acc = 0;
    // ワーシャルフロイド法
    rep(k, N) {
      rep(x, N) {
        rep(y, N) {
          G[x][y] = min(G[x][y], G[x][k] + G[k][y]);
          if(G[x][y] != INF) acc += G[x][y];
        }
      }
    }
    print(acc)
}
