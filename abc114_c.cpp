#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
using ll=long long;

void func(ll n, ll x, int flg, ll& ans) {
    if(x > n) return;
    if(flg == 0b111) ans++;
    func(n, x*10+3, flg|0b001, ans);
    func(n, x*10+5, flg|0b010, ans);
    func(n, x*10+7, flg|0b100, ans);

}

int main() {
    int n;
    cin >> n;
    ll ans = 0;
    func(n, 0, 0b000, ans);
    cout << ans << endl;
}