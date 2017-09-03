//Author: Andres-Felipe Ortega-Montoya
//CHEFPDIG.cpp
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

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int TC;
  cin >> TC;
  for(int tc = 1; tc <= TC; ++tc){
    int num[10];
    memset(num,0,sizeof(num));
    string str;
    cin >> str;
    for(int i = 0; i < (int)str.size(); ++i){
      ++num[str[i]-'0'];
    }
    for(char i = 'A'; i <= 'Z'; ++i){
      if(i%10 == i/10){
        if(num[i%10] >= 2){
          cout << i;
        }
      }else if(num[i%10] && num[(i/10)%10]){
        cout << i;
      }
    }
    cout << "\n";
  }
}
