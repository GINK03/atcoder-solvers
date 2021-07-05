
#include<iostream>
#include<algorithm>
#include<vector>
#include<bits/stdc++.h> 
#include<cmath>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define print(s) std::cout << s << std::endl
using namespace std;
using ll=long long;
const long long INF = 1LL << 60;
template<class T> void chmin(T& a, T b) { if(a > b) { a = b; } }
template<class T> void Sort(vector<T>& input) { std::sort(input.begin(), input.end()); }


int main() {
  ll N; 
  cin >> N;
  vector<ll> X(N, 0), Y(N, 0), Z(N, 0);
  rep(i, N) {
	cin >> X[i] >> Y[i] >> Z[i];
  }
  vector<vector<ll>> edge(N, vector<ll>(N, INF));
  rep(i, N) {  rep(j, N) {
	edge[i][j] = abs(X[i] - X[j]) + abs(Y[i] - Y[j]) + max(0ll, Z[i] - Z[j]);
	edge[j][i] = abs(X[i] - X[j]) + abs(Y[i] - Y[j]) + max(0ll, -Z[i] + Z[j]);
  }}

  vector<vector<ll>> dp(1<<N, vector<ll>(N,INF));
  dp[0][0] = 0ll;
  rep(mask, 1<<N) {
	rep(i, N) {
	  rep(j, N) {
		if(i!=j and (mask&1<<i) > 0 and edge[j][i] != INF) {
		  dp[mask][i] = min(dp[mask][i], dp[mask^(1<<i)][j] + edge[j][i]);
		}
	  }
	}
  }
  print(dp[(1<<N) - 1][0]);
}

