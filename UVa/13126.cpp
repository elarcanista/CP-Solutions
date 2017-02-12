//Author: Andres Felipe Ortega Montoya
//UVa 13126 - Wildcards

#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const ll MAXN = 10e6;

struct trie{
  static ll maxId;
  static ll C[MAXN];
  static ll k;
  static ll last;
  ll id;
  trie* f;
  map<char, trie*>* children;
  unordered_set<ll>* out;
 
  trie (string word): trie(){
    for(ll i = 0; i < word.size(); ++i){
      if(word[i] == '?'){
        ++last;
        continue;
      } 
      trie* current = this;
      while(i < word.size() && word[i] != '?'){
        current = current->add(word[i++]);
      }
      current->out->insert(i-1);
      last = (word[i] == '?');
      ++k;
    }
    fillF();
  }
  trie(): id(maxId), f(this), out(new unordered_set<ll>), children(new map<char, trie*>){++maxId;}
 
  trie* g(char c){
    if(children->count(c)){
      return (*children)[c];
    }
    if(!id){
      return this;
    }
    return NULL;
  }
 
  trie* add(char c){
    if(children->count(c)){
      return (*children)[c];
    }else{
      (*children)[c] = new trie();
      return (*children)[c];
    }
  }
 
  void fillF(){
    queue<trie*> q;
    for(auto& u: *children){
      u.second->f = this;
      q.push(u.second);
    }
    while(!q.empty()){
      trie* r = q.front(); q.pop();
      for(auto& a: *(r->children)){
        trie* u = r->g(a.first);
        q.push(u);
        trie* v = r->f;
        while(!v->g(a.first)){
          v = v->f;
        }
        u->f = v->g(a.first);
        u->out->insert(u->f->out->begin(), u->f->out->end());
      }
    }
  }
 
 
  unordered_set<ll> matches(string T){
    for (int i = 0; i < MAXN; ++i){
      C[i] = 0;
    }
    unordered_set<ll> matches;
    trie* q = this;
    for(ll i = 0; i < T.size(); ++i){
      while(!q->g(T[i])){
        q = q->f;
      }
      q = q->g(T[i]);
      for(auto& l: *(q->out)){
        if(i >= l)C[i-l]+=(i < T.size()-last);
      }
      matches.insert(q->out->begin(), q->out->end());
    }
    return matches;
  }
};

ll trie::maxId = 0;
ll trie::k = 0;
ll trie::last = 0;
ll trie::C[MAXN];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string P, T;
  while(cin >> T >> P){
    if(P.size() > T.size()){
      cout << 0 << "\n";
      continue;
    }
    trie::maxId = 0;
    trie::k = 0;
    trie::last = 0;
    trie* root = new trie(P);
    root->matches(T);
    ll counter = 0;
    for(ll i = 0; i < T.size()-(trie::last-1)*(trie::last>0); ++i){
      if((trie::C)[i] == trie::k)++counter;
    }
    cout << counter << "\n";
  }
}
