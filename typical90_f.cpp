

#include <iostream>
using namespace std;

string S;
int N,K;
int nex[100009][26];

int main() {
	// Step #1. 入力
	cin >> N >> K;
	cin >> S;

	// Step #2. 前計算
	for (int i = 0; i < 26; i++) nex[S.size()][i] = S.size();
	for (int i = (int)S.size() - 1; i >= 0; i--) {
		for (int j = 0; j < 26; j++) {
			if ((int)(S[i] - 'a') == j) {
				nex[i][j] = i;
			}
			else {
				nex[i][j] = nex[i + 1][j];
			}
		}
	}

	// Step #3. 一文字ずつ貪欲に決める
	string Answer = "";
	int CurrentPos = 0;
	for (int i = 1; i <= K; i++) {
		for (int j = 0; j < 26; j++) {
			int NexPos = nex[CurrentPos][j];
			int MaxPossibleLength = (int)(S.size() - NexPos - 1) + i;
			if (MaxPossibleLength >= K) {
				Answer += (char)('a' + j);
				CurrentPos = NexPos + 1;
				break;
			}
		}
	}

	// Step #4. 出力
	cout << Answer << endl;
	return 0;
}

