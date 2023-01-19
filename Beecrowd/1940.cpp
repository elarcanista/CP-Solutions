//Author: Andrés Felipe Ortega Montoya
//URI 1940 - Strategy Game
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int play, round;
	while(cin >> play >> round){
		int a[play];
		memset(a, 0, sizeof(a));
		int hip;
		int his = 1 << 31;
		int curr;
		for(int i = 0; i < play*round; ++i){
			cin >> curr;
			a[i%play] += curr;
			if(a[i%play] >= his){
				his = a[i%play];
				hip = i%play;
			}
		}
		cout << (hip+1) << "\n";
	}
	return 0;
}
