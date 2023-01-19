//Author: Andrés Felipe Ortega Montoya
//URI 1573 - Chocolate Factory
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int cbrt(int a){
	float b = a;
	float curr = b/2;
	float left = 0;
	float right = b;
	float cub;
	while(abs((cub = curr*curr*curr) - b) > 0.1 || (cub) - b < 0){
		//cout << cub << " " << curr << "\n";
		if(cub > b){
			right = curr;
			curr = (curr + left)/2;
		}else{
			left = curr;
			curr = (curr + right)/2;
		}
	}
	return (int) curr;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int A, B, C;
	while(cin >> A >> B >> C && (A || B || C)){
		cout << cbrt(A*B*C) << "\n";
	}
	return 0;
}
