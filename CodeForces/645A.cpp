#include <bits/stdc++.h>
using namespace std;

char a[2][2];
char b[2][2];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string sa, sb;
	cin >> a[0][0] >> a[0][1] >> a[1][0] >> a[1][1];
	cin >> b[0][0] >> b[0][1] >> b[1][0] >> b[1][1];
	
	if (a[0][0] != 'X')
		sa += a[0][0];
	if (a[1][0] != 'X')
		sa += a[1][0] ;
	if (a[1][1] != 'X')
		sa += a[1][1];
	if (a[0][1] != 'X')
		sa += a[0][1];
		
	if (b[0][0] != 'X')
		sb += b[0][0];
	if (b[1][0] != 'X')
		sb += b[1][0] ;
	if (b[1][1] != 'X')
		sb += b[1][1];
	if (b[0][1] != 'X')
		sb += b[0][1];
		
	bool eq;
	for(int i = 0; i < 3; ++i){
		eq = true;
		for(int j = 0; j < 3; ++j){
			if(sa[j] != sb[(i+j)%3]){
				eq = false;
				break;	
			} 
		}
		if(eq){
			cout << "YES\n";
			break;
		}
	}
	if(!eq) cout << "NO\n";
	return 0;
}
