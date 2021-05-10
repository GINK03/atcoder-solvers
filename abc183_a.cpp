
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
  int X;
  cin >> X;
  if( X >= 0 ) cout << X << endl;
  else cout << 0 << endl;
}
