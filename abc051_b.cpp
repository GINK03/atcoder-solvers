#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int K, S;
    cin >> K;
    cin >> S;
    int num = 0;
    for(int x=0; x<=K; x++) {
        for(int y=0; y<=K; y++) {
            int z = S - x - y;
            if((z >= 0) && (z <= K)){
                num += 1;
            }
        }
    }
    cout << num << endl;
}