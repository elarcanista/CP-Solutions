//Author: Andres-Felipe Ortega-Montoya
//872.cpp
#include <bits/stdc++.h>
#define DEBUG
#ifdef DEBUG
#define Debug(x) cout << x
#else
#define Debug(x)
#endif

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

vector<char> letters;
vector<char> g[30];
vector<char> ans;
char vis[30];
int income[30];
int V;

bool allTopos(){
  bool flag = false;
  for(auto&v : letters){
    if(!income[v-'A'] && !vis[v-'A']){
      vis[v-'A'] = true;
      ans.push_back(v);
      for(auto&u : g[v-'A'])
        --income[u-'A'];
      if(!allTopos()) return false;
      for(auto&u : g[v-'A'])
        ++income[u-'A'];
      ans.pop_back();
      vis[v-'A'] = false;
      flag = true;
    }
  }
  if(!flag){
    if((int)ans.size() != V) return false;
    cout << ans[0];
    for(int i = 1; i < (int)ans.size(); ++i)
      cout << " " << ans[i];
    cout << "\n";
  }
  return true;
}

void reset(){
  letters.clear();
  ans.clear();
  V = 0;
  for(int i = 0; i < 30; ++i){
    g[i].clear();
    vis[i] = false;
    income[i] = 0;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int TC;
  cin >> TC;
  cin.ignore();
  for(int tc = 1; tc <= TC; ++tc){
    reset();
    cin.ignore();
    string line, in;
    getline(cin, line);
    stringstream ss(line);
    while(ss >> in){
      letters.push_back(in[0]);
      ++V;
    }
    sort(letters.begin(), letters.end());
    ss.clear();
    getline(cin, line);
    ss.str(line);
    while(ss >> in){
      g[in[0]-'A'].push_back(in[2]);
      ++income[in[2]-'A'];
    }
    if(!allTopos()) cout << "NO\n";
    if(tc != TC) cout << "\n";
  }
}
