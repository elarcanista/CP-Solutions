//Author: Andres Felipe Ortega Montoya
//HackerRank Project Euler #8 - Largest product in a series
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        int k;
        cin >> n >> k;
        string num;
        cin >> num;
        int beg = 0;
        int end = 0;
        long long max = 0;
        long long temp = 1;
        for(; end < n; ++end){
            if(num[end]-'0' == 0){
                beg = end+1;
                temp = 1;
            }else{
                temp *= num[end]-'0';
                if(end - beg >= k){
                    temp /= num[beg]-'0';
                    ++beg;
                }
            }
            if(temp > max && end-beg == k-1) max = temp;
        }
        cout << max << "\n";
    }
    return 0;
}
