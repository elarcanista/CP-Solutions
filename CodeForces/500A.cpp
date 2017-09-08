#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, t, act;
	cin >> n;
	cin >> t;
	--n;
	bool yes = false;
	int i = 1;
	while(i <= n){
		cin >> act;
		int next = i + act;
		if(next == t){
			yes = true;
			break;
		}
		if(i + act > t) break;
		while(++i < next){
			cin >> act;
		}
	}
	if(yes) cout << "YES\n";
	else cout << "NO\n";
}
