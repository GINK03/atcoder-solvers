
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<bits/stdc++.h>
#include<cmath>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define print(s) std::cout << s << std::endl;
#define True true
#define False false

using namespace std;
using ll=long long;
const long long INF = 1LL << 60;
template<class T> void chmin(T& a, T b) { if(a > b) { a = b; } }
template<class T> void Sort(vector<T>& input) { std::sort(input.begin(), input.end()); }


int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };
int H, W;
//char c[20][20];
//bool used[20][20];
vector<vector<char>> G;
vector<vector<bool>> used;

int dfs(int sx, int sy, int px, int py) {
	if (sx == px && sy == py && used[px][py] == true) return 0;
	used[px][py] = true;

	int ret = -10000;
	for (int i = 0; i < 4; i++) {
		int nx = px + dx[i], ny = py + dy[i];
		if (nx < 0 || ny < 0 || nx >= H || ny >= W || G[nx][ny] == '#') continue;
		if ((sx != nx || sy != ny) && used[nx][ny] == true) continue;
		int v = dfs(sx, sy, nx, ny);
		ret = max(ret, v + 1);
	}
	used[px][py] = false;
	return ret;
}

int main() {
	// Step #1. Input
	cin >> H >> W;
	G = vector<vector<char>>(H, vector<char>(W, '.'));
	used = vector<vector<bool>>(H, vector<bool>(W, false));
	rep(h, H) rep(w, W) 
		  cin >> G[h][w];

	// Step #2. DFS
	int Answer = -1;
	rep(h, H) rep(w, W) 
			Answer = max(Answer, dfs(h, w, h, w));
	if (Answer <= 2) Answer = -1;
	cout << Answer << endl;
	return 0;
}
