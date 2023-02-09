//Author: Andres Felipe Ortega Montoya                                                                                                                        
//HackerRank Sock Merchant                                                                                                                                    
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

set<int> s;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int TC, count = 0, in; cin >> TC;
  while(TC--){
    cin >> in;
    if(s.count(in)){
      ++count;
      s.erase(in);
    }else{
      s.insert(in);
    }
  }
  cout << count << "\n";
}
