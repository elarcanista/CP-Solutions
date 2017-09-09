#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

ll arr[MAXN];
ll tree[MAXN*4];

void build(int node, int l, int r){
  if(l > r) return;
  if(l == r){
    tree[node] = arr[l];
    return;
  }
  build(node*2, l, (l+r)/2);
  build(node*2+1, 1+(l+r)/2, r);
  tree[node] = tree[node*2] + tree[node*2+1];
}

ll query(int node, int l, int r, int a, int b){
  if(l > r || l > b || r < a) return 0;
  if(l >= a && r <= b){
    return tree[node];
  }
  ll temp1 = query(node*2, l, (l+r)/2, a, b);
  ll temp2 = query(node*2+1, 1+(l+r)/2, r, a, b);
  return temp1 + temp2;
}

void update(int node, int l, int r, int a, int b, ll p){
  if(l > r || l > b || r < a) return;
  if(l == r){
    tree[node] += p;
    return;
  }
  update(node*2, l, (l+r)/2, a, b, p);
  update(node*2+1, 1+(l+r)/2, r, a, b, p);
  tree[node] = tree[node*2] + tree[node*2+1];
}
