//Author: Andres-Felipe Ortega-Montoya
//viterbi.cpp
#include <bits/stdc++.h>

using namespace std;

template <typename N, typename M>
using umap = unordered_map<N, M>;

const int INF = 1<<30;

struct graph{
  umap<string, umap<string, double> > g;

  graph():g(){}

  void add(string u, string v, double prob){
    g[u][v] = prob;
  }

  umap<string, umap<string, double>>& get(){
    return g;
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

  void reverse(graph& g2){
    for(auto& u : g){
      for(auto& v : u.second){
        g2.add(v.first,u.first,v.second);
      }
    }
  }
};

void in_vec(vector<string> &obs){
  obs.clear();
  string in;
  getline(cin, in);
  stringstream ss(in);
  while(ss >> in){
    obs.push_back(in);
  }
  getline(cin, in);
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

void dijkstra(graph &g, string &start, umap<string, double> &distance){
  priority_queue<pair<double,string> > q;
  q.push({0,start});
  distance[start]=0;
  while(!q.empty()){
    double w = -q.top().first;
    string u = q.top().second;
    q.pop();
    for(auto& v: g.get(u)){
      if(!distance.count(v.first) || w+v.second < distance[v.first]){
        distance[v.first] = w+v.second;
        q.push({-(w+v.second),v.first});
      }
    }
  }
}

void build(graph &cause, graph &symptom){
  graph in;
  in.fill();
  string str;
  vector<string> obs;
  in_vec(obs);
  //what is left to go from each state to the final ones
  graph inverse;
  in.reverse(inverse);
  umap<string, umap<string, double> > distances;
  for(auto &u : obs){
    umap<string, double> temp;
    dijkstra(inverse, u, temp);
    distances[u] = temp;
  }
  //fill temp_symptom graph
  umap<string, double> min_dist;
  graph temp_symptom;
  for(auto &u : inverse.get()){
    double min_w = INF, max_w = 0, total = 0;
    for(auto &v : obs){
      if(u.first == v){
        min_w = min(min_w, 1.0);
        max_w = max(max_w, 1.0);
      }else if(!distances[v].count(u.first)){
        continue;
      }else{
        min_w = min(min_w, distances[v][u.first]);
        max_w = max(max_w, distances[v][u.first]);
      }
    }
    for(auto &v : obs){
      if(u.first == v) total += max_w;
      else if(!distances[v].count(u.first)) continue;
      total += max_w-distances[v][u.first]+1;
    }
    min_dist[u.first] = min_w;
    for(auto &v : obs){
      if(u.first == v) temp_symptom.add(u.first, v, max_w/total);
      else if(!distances[v].count(u.first)) continue;
      temp_symptom.add(u.first, v, (max_w-distances[v][u.first]+1)/total);
    }
  }
  for(auto &u : obs){
    double total = 0;
    for(auto &v : temp_symptom.get()){
      total += temp_symptom.get(v.first, u);
    }
    for(auto &v : temp_symptom.get()){
      symptom.add(u,v.first,temp_symptom.get(v.first, u)/total);
    }
  }
  //fill cause graph
  for(auto &u : symptom.get()){
    cause.add("Start", u.first, 1/(double)obs.size());
    for(auto &v : symptom.get()){
      cause.add(u.first,v.first,1/1/(double)obs.size());
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  graph cause, symptom;
  build(cause, symptom);
  vector<string> obs;
  vector<string> ans;
  in_vec(obs);
  viterbi("Start", cause, symptom, obs, ans);
  for(auto &i : ans){
    cout << i << " ";
  }
  cout << "\n";
}
