
#include<iostream>
#include<algorithm>
#include<vector>
#include<bits/stdc++.h>
#include<cmath>
#include<optional>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define print(s) std::cout << s << std::endl;
#define vec std::vector;
#define append push_back;
using namespace std;
using ll=long long;
const long long INF = 1LL << 60;
template<class T> void chmin(T& a, T b) { if(a > b) { a = b; } }
template<class T> void Sort(vector<T>& input) { std::sort(input.begin(), input.end()); }
template<class T> std::vector<T> mk_vec(int size,T init) { return std::vector<T>(size, init); }
template<class T> std::vector<std::vector<T>> mk_mat(int H, int W, T init) { return std::vector<std::vector<T>>(H, std::vector<T>(W, init)); }


int N, Q;
vector<tuple<int,int,int>> G;

vector<ll> bf(int s, int N) {
  auto d = mk_vec<ll>(N, INF);
  d[s] = 0;
  rep(n, N) {
	bool update = false;
	rep(pos, G.size()){
	  int i, j, c; tie(i, j, c) = G[pos];
	  if(d[j] > d[i] + c) { 
		  d[j] = d[i] + c;
		  update = true;
	  }
	}
	// 負閉路が存在する場合、空のベクターを返す
	if(update == false) {
	  return vector<ll>();
	}
  }
  return d;
}

int main() {
  cin >> N >> Q;
  rep(n, N-1) {
	int i, j;
	cin >> i >> j;
	i -= 1; j -=1;
	G.push_back(make_tuple(i, j, 1));
	G.push_back(make_tuple(j, i, 1));
  }
  vector<ll> dv = bf(0, N);
  rep(q, Q) {
	int c,d;
	cin >> c >> d;
	c -= 1; d -=1;
	int r = abs(dv[d] - dv[c]);
	// cout << "debug " <<  c << d << " " << r << endl;
	if(r%2 == 0) {
	  print("Town");
	} else {
	  print("Road");
	}
  }
  return 0;

}
