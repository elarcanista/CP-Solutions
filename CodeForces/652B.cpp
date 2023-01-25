//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n; cin >> n;
	vector<int> v;
	while(n--){
		int t; cin >> t;
		v.push_back(t);
	}
	sort(v.begin(), v.end());
	vector<int> ans;
	for(int i = 0, tot = 0; tot < v.size(); ){
		ans.push_back(v[i]);
		if(i != v.size()-1-i){
			ans.push_back(v[v.size()-1-i]);
			++tot;
		}
		++i;
		++tot;
	}
	cout << ans[0];
	for(int i = 1; i < ans.size(); ++i){
		cout << " " << ans[i];
	}
	cout << "\n";
	return 0;
}