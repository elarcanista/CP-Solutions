//Author: Andres-Felipe Ortega-Montoya
//11235.cpp
#include <bits/stdc++.h>
//#define DEBUG
#ifdef DEBUG
#define Debug(x) cout << x
#else
#define Debug(x)
#endif
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXN = 100005;

int arr[MAXN];
int pos[MAXN];
int tree[MAXN*4];

ii binl(int l, int r, int g){
  if(l >= r) return {l,pos[l]};
  if(g > pos[(l+r)/2]) return binl((l+r)/2 + 1, r, g);
  return binl(l, (l+r)/2, g);
}

ii binr(int l, int r, int g){
  if(l >= r) return {r,pos[r]};
  if(g < pos[(l+r+1)/2]) return binr(l,(l+r+1)/2 -1, g);
  return binr((l+r+1)/2, r, g);
}

void build(int node, int l, int r){
  if(l > r) return;
  if(l == r){
    tree[node] = arr[l];
    return;
  }
  build(node*2, l, (l+r)/2);
  build(node*2+1, (l+r)/2 +1, r);
  tree[node] = max(tree[node*2], tree[node*2+1]);
}

int query(int node, int l, int r, int a, int b){
  if(a > r || b < l) return -INF;
  if(l == r) return tree[node];
  if(l >= a && r <= b) return tree[node];
  int t1 = query(node*2, l, (l+r)/2, a, b);
  int t2 = query(node*2+1, (l+r)/2 + 1, r, a, b);
  return max(t1,t2);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n,q;
  while(cin >> n >> q && n){
    int curr, last, ind = 0;
    cin >> last;
    arr[0] = 1;
    for(int i = 1; i < n; ++i){
      cin >> curr;
      if(last == curr){
        ++arr[ind];
      }else{
        pos[++ind] = i;
        arr[ind] = 1;
        last = curr;
      }
    }
    pos[++ind] = n;
    arr[ind] = 0;
    build(1,0,ind);
    for(int i = 0; i < q; ++i){
      int a,b;
      cin >> a >> b;
      --a;
      --b;ii c = binl(0,ind,a);
      ii d = binr(0,ind,b);
      if(c.second > b || d.second < a) cout << b-a+1 << "\n";
      else cout << max(query(1,0,ind,c.first,d.first-1),
                       max(c.second - a, b - d.second +1)) << "\n";
    }
  }
}
