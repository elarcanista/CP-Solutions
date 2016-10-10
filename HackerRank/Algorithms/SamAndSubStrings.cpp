//Author: Andres Felipe Ortega Montoya
//HackerRank - Sam and sub-strings
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXN = 200001;
const int MOD = 1000000007;

int ones[MAXN];

void init(){
  ones[0] = 0;
  ones[1] = 1;
  for(int i = 2; i <= MAXN; ++i){
    ones[i] = (ones[i-1]*10+1)%MOD;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  init();
  string num; cin >> num;
  int ans = 0;
  for(int i = 0; i < num.size(); ++i){
    int temp = (i+1) * ones[num.size()-i] * (num[i]-'0');
    temp %= MOD;
    ans += temp;
    ans %= MOD;
  }
  cout << ans << "\n";
}
