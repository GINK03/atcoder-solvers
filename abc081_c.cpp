#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n];
    for(int& e : a){
        cin >> e;
    }
    int tmp_res[n];
    for(int i=0; i<n; i++){
        int tmp = 0;
        int e = a[i];
        while(true){
            if(e%2 == 0){
                e /= 2;
                tmp+=1;
            } else {
                break;
            }
        }
        tmp_res[i] = tmp;
    }
    cout << *min_element(tmp_res, tmp_res+n) << endl;
}