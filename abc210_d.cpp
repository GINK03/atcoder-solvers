
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

ll H,W,C;

vector<vector<int>> dd = {{1, 0}, {0, 1}};

ll calc(tuple<ll, ll, ll> e0, tuple<ll, ll, ll> e1 ){
    ll c0, c1; ll h0, h1, w0, w1;
    tie(c0, h0, w0) = e0;
    tie(c1, h1, w1) = e1;
    return c0 + c1 + C*(abs(h0-h1) + abs(w0-w1));
}
int main() {
    cin >> H >> W >> C;
    auto G = mk_mat<ll>(H, W, 0);
    vector<tuple<ll, ll, ll>> G2;
    rep(h, H) {
        rep(w, W) {
            cin >> G[h][w];
            G2.push_back(make_tuple(G[h][w], h, w));
        }
    }
    ll ans2 = INF;
    rep(h, H) {
        rep(w, W) {
            auto src = G[h][w];
            rep(i, 2) {
                ll nh, nw; nh = h; nw = w;
                nh += dd[i][0];
                nw += dd[i][1];
                if( !( 0 <= nh && nh < H && 0 <= nw && nw < W) )
                    continue;
                ll tgt = G[nh][nw];
                ll cost = src+tgt + C*(abs(h-nh) + abs(w-nw));
                ans2 = min(ans2, cost);
            }
        }
    }
    Sort(G2);
    ll ans1 = calc(G2[0], G2[1]);
    rep(i, H*W) {
        if(i == 0) continue;
        ll tmp = calc(G2[0], G2[i]);
        if(tmp > ans2) {
            break;
        }
        ans1 = min(ans1, tmp);
    }
    print(min(ans1, ans2));
}
