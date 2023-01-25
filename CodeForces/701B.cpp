//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
const ll MAXN = 100000;
bool rows[MAXN], cols[MAXN];
 
void reset(){
	for(int i = 0; i < MAXN; ++i){
		rows[i] = false;
		cols[i] = false;
	}
}
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll n,m; 
    while(cin >> n){
    	int numR = 0, numC = 0;
    	reset();
	    ll na = n*n;
		cin >> m;
		while(m--){
			ll row, col; cin >> row >> col;
			--row; --col;
			//cout << na;
			if(!rows[row]){
				rows[row] = true;
				//cout << "+" << numC << "-" << n;
				na += numC - n;
				numR++;
			}
			if(!cols[col]){
				cols[col] = true;
				//cout << "+" << numR << "-" << n;
				na += numR - n;
				numC++;
			}
			//cout << "=";
			cout << na << "\n";
		}
	}
	return 0;
}