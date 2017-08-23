//Author: Andres-Felipe Ortega-Montoya
//339D.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXN = 1 << 17;

int arr[MAXN+8];
int tree [4*MAXN+8];

void build(int node, int l, int r){
  if(l>r) return;
  if(l==r){
    tree[node]=arr[l];
    return;
  }
  build(node*2, l, (l+r)/2);
  build(node*2+1, (l+r)/2 + 1, r);
  tree[node] = ((int)log2(node)%2)? (tree[node*2]^tree[node*2+1])
    : (tree[node*2]|tree[node*2+1]);
}

int update(int node, int l, int r, int p, int b){
  if(l>r) return 0;
  if(l==r) return tree[node] = b;
  if(p <= (l+r)/2)
    update(node*2, l, (l+r)/2, p, b);
  else
    update(node*2+1, (l+r)/2 + 1, r, p, b);
  return tree[node] = ((int)log2(node)%2)? (tree[node*2]^tree[node*2+1])
    : (tree[node*2]|tree[node*2+1]);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int m, n;
  cin >> n >> m;
  for(int i = 0; i < (1<<n); ++i){
    int temp;
    cin >> temp;
    arr[i] = temp;
  }
  int root = 1;
  if(n%2){
    build(1, 0, (1<<n) -1);
  }else{
    build(2, 0, (1<<n) -1);
    root = 2;
  }
  while(m--){
    int p, b;
    cin >> p >> b;
    cout << update(root, 0, (1<<n)-1, p-1, b) << "\n";
  }
}
