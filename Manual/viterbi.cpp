//Author: Andres-Felipe Ortega-Montoya
//viterbi.cpp
#include <bits/stdc++.h>

using namespace std;

template <typename N, typename M>
using umap = unordered_map<N, M>;

struct graph{
  umap<string, umap<string, double> > g;

  graph():g(){}

  void add(string u, string v, double prob){
    g[u][v] = prob;
  }

  umap<string, double>& get(string u){
    return g[u];
  }

  double get(string u, string v){
    return g[u][v];
  }

  void print(){
    for(auto& u : g){
      for(auto& v : u.second){
        cout << u.first << " " << v.first << " " << v.second << "\n";
      }
    }
  }

  void fill(){
    string in;
    while(getline(cin, in) && in != ""){
      stringstream ss(in);
      string state1, state2;
      double prob;
      ss >> state1 >> state2 >> prob;
      add(state1, state2, prob);
    }
  }
};

void in_obs(vector<string> &obs){
  obs.clear();
  string in;
  getline(cin, in);
  stringstream ss(in);
  while(ss >> in){
    obs.push_back(in);
  }
}

double viterbi(string start, graph &cause, graph &symptom,
             vector<string> &obs, vector<string> &pred){
  pred.clear();
  vector<umap<string, pair<double,string> > >dp;
  umap<string, pair<double,string> > init;
  dp.push_back(init);
  //initial probs
  for(auto& u : cause.get(start)){
    dp[0][u.first] = {u.second * symptom.get(u.first,obs[0]), start};
  }
  //probs on time t
  for(int t = 1; t < (int) obs.size(); ++t){
    umap<string, pair<double,string> > temp_umap;
    dp.push_back(temp_umap);
    for(auto& u : cause.get(start)){
      double max_pr = 0;
      for(auto& v : cause.get(u.first)){
        //prob of ending in v coming from u having made observation t
        double prob_u_v = dp[t-1][u.first].first * v.second * symptom.get(v.first,obs[t]);
        if(prob_u_v > max_pr){
          max_pr = prob_u_v;
          dp[t][v.first] = {max_pr, u.first};
        }
      }
    }
  }
  //max prob
  double max_pr = 0;
  string max_st = "";
  for(auto& u : dp[dp.size()-1]){
    if(u.second.first > max_pr){
      max_pr = u.second.first;
      max_st = u.first;
    }
  }
  //backtrack
  int t = dp.size()-1;
  while(max_st != start){
    pred.push_back(max_st);
    max_st = dp[t][max_st].second;
    --t;
  }
  reverse(pred.begin(),pred.end());
  return max_pr;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  graph cause, symptom;
  vector<string> obs, pred;
  cause.fill();
  symptom.fill();
  in_obs(obs);
  cout << viterbi("Start", cause, symptom, obs, pred) << "\n";
  for(auto &i : pred){
    cout << i << " ";
  }
}
