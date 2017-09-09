#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n; cin >> n;
	vector<int> v;
	int temp; cin >> temp;
	v.push_back(temp);
	bool dec = false;
	bool good = true;
	int last = v[0];
	int beg = -1;
	int end = -1;
	for(int i = 1; i < n; ++i){
		cin >> temp;
		v.push_back(temp);
		if(v[i] < last && !dec){
			if(beg != -1){
				good = false;
				break;
			}
			dec = true;
			beg = i-1;
		}else if(v[i] > last && dec){
			dec = false;
			end = i-1;
		}
		last = v[i];
	}
	if(end == -1) end = v.size()-1;
	if(beg == -1) cout << "yes\n1 1";
	else if(good && ((beg == 0 || v[end] >= v[beg-1]) && (end == (v.size() -1) || v[beg] <= v[end+1])))
		cout << "yes\n" << beg+1 << " " << end+1;
	else cout << "no";
}
