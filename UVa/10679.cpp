//Author: Andres Felipe Ortega Montoya
//UVa 10679 - I Love Strings!!

#include <bits/stdc++.h>
using namespace std;
 
struct trie{
  static int maxId;
  int id;
  trie* f;
  map<char, trie*> children;
  unordered_set<int> out;
 
  trie (vector<string> words): trie(){
    for(int i = 0; i < words.size(); ++i){
      trie* current = this;
      for(auto &c: words[i]){
        current = current->add(c);
      }
      current->out.insert(i);
    }
    fillF();
  }
  trie(): id(maxId), f(this){++maxId;}
 
  trie* g(char c){
    if(children.count(c)){
      return children[c];
    }
    if(!id){
      return this;
    }
    return NULL;
  }
 
  trie* add(char c){
    if(children.count(c)){
      return children[c];
    }else{
      children[c] = new trie();
      return children[c];
    }
  }
 
  void fillF(){
    queue<trie*> q;
    for(auto& u: children){
      u.second->f = this;
      q.push(u.second);
    }
    while(!q.empty()){
      trie* r = q.front(); q.pop();
      for(auto& a: r->children){
        trie* u = r->g(a.first);
        q.push(u);
        trie* v = r->f;
        while(!v->g(a.first)){
          v = v->f;
        }
        u->f = v->g(a.first);
        u->out.insert(u->f->out.begin(), u->f->out.end());
      }
    }
  }
 
  unordered_set<int> matches(string T){
    unordered_set<int> matches;
    trie* q = this;
    for(auto& c: T){
      while(!q->g(c)){
        q = q->f;
      }
      q = q->g(c);
      matches.insert(q->out.begin(), q->out.end());
    }
    return matches;
  }
};
 
int trie::maxId = 0;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int k, q;
  string T;
  cin >> k;
  while(k--){
    trie::maxId = 0;
    cin >> T >> q;
    vector<string> words;
    for(int i = 0; i < q; ++i){
      string temp;
      cin >> temp;
      words.push_back(temp);
    }
    trie root(words);
    unordered_set<int> matches = root.matches(T);
    for(int i = 0; i < q; ++i){
      cout << (matches.count(i)? "y": "n") << "\n";
    }
  }
}
