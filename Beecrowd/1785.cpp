//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

bool check(int X){
	vector<int> v;
	for(int i = 0; i < 4; ++i){
		v.push_back(X%10);
		X/=10;
	}
	sort(v.begin(), v.end());
	for(int i = 1; i < v.size(); ++i){
		if(v[i] != v[i-1]) return true;
	}
	return false;
}

int highest_number_with_digits_of(int X){
	vector<int> v;
	for(int i = 0; i < 4; ++i){
		v.push_back(X%10);
		X/=10;
	}
	sort(v.begin(), v.end());
	int ans = 0;
	int ten = 1;
	for(int i = 0; i < v.size(); ++i){
		ans += v[i]*ten;
		ten *= 10;
	}
	return ans;
}

int lowest_number_with_digits_of(int X){
	vector<int> v;
	for(int i = 0; i < 4; ++i){
		v.push_back(X%10);
		X/=10;
	}
	sort(v.begin(), v.end());
	int ans = 0;
	int ten = 1;
	for(int i = v.size()-1; i >= 0; --i){
		ans += v[i]*ten;
		ten *= 10;
	}
	return ans;
}

int krapekar(int X) {
   int cnt = 0;
   while (X != 6174) {
       int hi = highest_number_with_digits_of(X);
       int lo = lowest_number_with_digits_of(X);
       //cout << hi << " " << lo << "\n";
       X = hi - lo;
       cnt = cnt + 1;
   }
   return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	for(int i = 1; i <= TC; ++i){
		int in; cin >> in;
		cout << "Caso #" << i << ": "<< (check(in)? krapekar(in):-1) << "\n";
	}
	return 0;
}
