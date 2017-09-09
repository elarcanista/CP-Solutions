#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXN = 200008;
k
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
  tree[node] = min(tree[node*2], tree[node*2+1]);
}

ll lazy[MAXN*4];

void prop(int node, int l, int r){
  if(lazy[node]){
    tree[node] += lazy[node];
    if(l!=r){
      lazy[node*2] += lazy[node];
      lazy[node*2+1] += lazy[node];
    }
    lazy[node] = 0;
  }
}

void update(int node, int l, int r, int a, int b, ll p){
  prop(node, l, r);
  if(l > r || l > b || r < a) return;
  if(l >= a && r <= b){
    tree[node] += p;
    if(l!=r){
      lazy[node*2] += p;
      lazy[node*2+1] += p;
    }
    return;
  }
  update(node*2, l, (l+r)/2, a, b, p);
  update(node*2+1, 1+(l+r)/2, r, a, b, p);
  tree[node] = min(tree[node*2], tree[node*2+1]);
}

ll query(int node, int l, int r, int a, int b){
  if(l > r || l > b || r < a) return INF;
  prop(node, left, right);
  if(l >= a && r <= b){
    return tree[node];
  }
  ll temp1 = query(node*2, l, (l+r)/2, a, b);
  ll temp2 = query(node*2+1, 1+(l+r)/2, r, a, b);
  return min(temp1, temp2);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  memset(lazy, 0, sizeof lazy);
  int n,m;
  cin >> n;
  for(int i = 0; i < n; ++i){
    int temp;
    cin >> temp;
    arr[i] = temp;
  }
  build(1,0,n-1);
  cin >> m;
  cin.ignore();
  for(int i = 0; i < m; ++i){
    string temp;
    getline(cin, temp);
    stringstream ss(temp);
    int a, b;
    ll c;
    ss >> a >> b;
    if(ss >> c){
      if(a > b){
	incr(1,0,n-1,a,n-1,c);
	incr(1,0,n-1,0,b,c);
      }else incr(1,0,n-1,a,b,c);
    }else if(a > b){
      cout << min(query(1,0,n-1,a,n-1), query(1,0,n-1,0,b)) << "\n";
    }else{
      cout << query(1,0,n-1,a,b) << "\n";
    }
  }
}
