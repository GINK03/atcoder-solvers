
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

ll N; 

// w = (N∗h∗n)//(4∗h∗n − N∗n − N∗h)
bool f(ll h,ll n) {
    if ((h == 0 and n == 0) or (4*h*n-N*n-N*h) <= 0)
        return false;
    if ((N*h*n)%(4*h*n-N*n-N*h) == 0) return true;
    else return false;
}

int main() {
    cin >> N;
    for(ll h =0; h<3501; h++) {
        for(ll n=0; n<3501; n++) {
            if(f(h,n)) {
                cout << h << " " << n << " " << (N*h*n)/(4*h*n-N*n-N*h) << endl;
                exit(0);
            }
        }
    }
}
