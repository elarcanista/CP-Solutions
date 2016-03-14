#include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("B-large-practice.in", "r", stdin);   reads input from file
    //freopen("B-large-practice.out", "w", stdout);   writes output to a file
    int TC; cin >> TC;
    for(int i = 1; i <= TC; ++i){
        stack<string> s;
        string temp;
        if(i == 1)cin.ignore();
        getline(cin, temp);
        stringstream line(temp);
        while(line >> temp){  //fills a stack with words on the line
            s.push(temp);
        }
        cout << "Case #" << i << ": " << s.top(); //output words on reverse order
        s.pop();
        while(!s.empty()){
            cout << " " << s.top();
            s.pop();
        }
        cout << "\n";
    }
}

