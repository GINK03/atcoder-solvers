#include<iostream>
#include<algorithm>
#include<vector>
#include<bits/stdc++.h>
#include<cmath>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rng(i, s, n) for (int i = s; i < (int)(n); i++)
#define print(s) std::cout << s << std::endl
using namespace std;
using ll=long long;
const long long INF = 1LL << 60;
template<class T> void chmin(T& a, T b) { if(a > b) { a = b; } }
template<class T> void Sort(vector<T>& input) { std::sort(input.begin(), input.end()); }

int main() {
	int N, K;
	cin >> N >> K;
	vector<int> A(N), B(N);
	rep(i, N) {
		cin >> A[i] >> B[i];
	}
	int R = max(*max_element(A.begin(), A.end()), K) + 1;
	int C = max(*max_element(B.begin(), B.end()), K) + 1;
	vector<vector<int>> sum(R + 1, vector<int>(C + 1));
	rep(i, N) ++sum[A[i] + 1][B[i] + 1];
	rng(i, 1, R+1) rng(j, 1, C+1) sum[i][j] += sum[i - 1][j];
	rng(i, 1, R+1) rng(j, 1, C+1) sum[i][j] += sum[i][j - 1];
	int ans = 0;
	for (int i = 0; i <= R - K - 1; ++i)
		for (int j = 0; j <= C - K - 1; ++j) 
			ans = max(ans, sum[i][j] + sum[i + K + 1][j + K + 1] - sum[i][j + K + 1] - sum[i + K + 1][j]);
	cout << ans << endl;
	return 0;
}
