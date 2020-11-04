#include <iostream>
#include <algorithm>
#include <bitset>
using namespace std;
using ll=long long;
int main() {
    string n;
    cin >> n;

    ll res = 0;
    for(int bit=0; bit < (1 << n.size()-1); bit++) {
        //cout << bitset<32>(bit) << endl;
        ll buff = 0;
        ll tmp = 0;

        for(int i=0; i< n.size(); ++i) {
            buff = buff*10 + n[i] - '0';
            if(bit & (1 << i)) {
                tmp += buff;
                buff = 0;
            }
        }
        res += tmp + buff;
    }
    cout << res << endl;
}