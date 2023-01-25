//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, k, qq; cin >> n >> k >> qq;
	map<int, int> f1;
	map<int, int> f2;
	priority_queue<int> q;
	for(int i = 0; i < n; ++i){
		int temp; cin >> temp;
		f1[i] = temp;
		f2[temp] = i;
	}
	while(qq--){
		int o, id; cin >> o >> id;
		--id;
		if(!--o){
			q.push(f1[id]);
		}else{
			priority_queue<int> q2;
			int i = 0;
			while(true){
				if(i == k || q.empty()){
					cout << "NO\n";
					break;
				}
				int temp2 = q.top(); q.pop();
				q2.push(temp2);
				if(f2[temp2] == id){
					cout << "YES\n";
					break;
				}
				++i;
			}
			while(!q2.empty()){
				q.push(q2.top()); q2.pop();
			}
		}
	}
	return 0;
}