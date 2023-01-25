//Author: Andres Felipe Ortega Montoya
//
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

int main(){
  //ios_base::sync_with_stdio(false);
  //cin.tie(NULL);
  int a, b; cin >> a >> b;
  string str; cin >> str;
  stack<int> s;
  bool v[str.size()];
  //cout << str;
  int i = 0;
  int grass;
  for(; i < a; ++i){
    v[i] = false;
    //cout << str[i] << " " << i << "\n";
    if(str[i] == 'G'){
      //cout << "leeeeel";
      s.push(i);
      grass = i;
      v[i] = true;
    }
  }
  //cout << i << "\n";
  bool done = false;
  i = grass-b;
  while(i >= 0){
    if(str[i] == '#') break;
    if(str[i] == 'T'){
      done = true;
      break;
    }
    i-=b;
  }
  i = grass+b;
  while(i < a){
    if(str[i] == '#') break;
    if(str[i] == 'T'){
      done = true;
      break;
    }
    i+=b;
  }
  // while(!s.empty()){
  //   int curr = s.top();
  //   //cout << curr << "\n";
  //   s.pop();
  //   if(curr-b >= 0 && !v[curr-b] && str[curr-b] != '#'){
  //     if(str[curr-b] == 'T'){
  // 	done = true;
  // 	break;
  //     }
  //     v[curr-b] = true;
  //     s.push(curr-b);
  //   }
  //   if(curr+b < a && !v[curr+b] && str[curr+b] != '#'){
  //     if(str[curr+b] == 'T'){
  // 	done = true;
  // 	break;
  //     }
  //     v[curr+b] = true;
  //     s.push(curr+b);
  //   }
  // }
  if(done) cout << "YES\n";
  else cout << "NO\n";
}