//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAXN = 500;
vector<ii> g [MAXN];
priority_queue<ii> q;
bool visited[MAXN];

void reset(){
	for(int i = 0; i < MAXN; ++i){
		visited[i] = false;
		g[i].clear();
	}	
}

int distance(int a, int b){
	int weight = 0;
	bool flag = false;
	//if(a == 5678 && b == 9090)flag = true;
	//cout << a << " " << b << "\n";
	while(a || b){
		int da = a%10;
		int db = b%10;
		if((da - db) > 5){
			
		} 
		int w1 = abs(min(da,db) + (10 - max(da,db)));
		//int w2 = abs(db - (10 - da));
		int w2 = abs(db - da);
		weight += min(w1, w2);
		//cout << da << " " << db << " " << w2 << " " << w1 << " " << weight << "\n";
		a /= 10;
		b /= 10;
	}
	//cout << " " << weight << "\n";
	return weight;
}

void primq(int u){
	visited[u] = true;
	for(auto &v: g[u]){
		if(!visited[v.second]) q.push({-v.first, v.second});
	}
}

int prim(int u){
	primq(u);
	int weight = 0;
	while(!q.empty()){
		ii v = q.top(); q.pop();
		if(!visited[v.second]){
			//cout << v.second << "\n";
			primq(v.second);
			weight += -v.first;
		}
	}
	return weight;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	while(TC--){
		reset();
		int n; cin >> n;
		int a[n];
		int start = 1 << 30;
		for(int i = 0; i < n; ++i){
			cin >> a[i];
			int temp = distance(0, a[i]);
			if(temp < start)start = temp;
		}
		for(int i = 0; i < n; ++i){
			for(int j = i+1; j < n; ++j){
				//cout << a[i] << " " << a[j] << "\n";
				int temp = distance(a[i], a[j]);
				g[i].push_back({temp, j});
				g[j].push_back({temp, i});
			}
		}
		int weight = prim(0);
		cout << (weight + start) << "\n";
	}
	return 0;
}
