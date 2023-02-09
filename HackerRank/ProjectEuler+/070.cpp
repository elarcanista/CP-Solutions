//Author: Andres Felipe Ortega Montoya
//HackerRank Project Euler #1 - Multiples of 3 and 5 
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
vector<int> primes;
int totient[(int) 10e7 + 1];

void sieve(int n){
    int prime = 3;
    primes.push_back(2);
    int p = 3;
    while(p*p < n){
        if((prime & (1 << p)) == 1)
            continue;
        primes.push_back(p);
        for(int kp = 3*p; kp*kp <= n; kp += 2*p)
            prime |= (1 << kp);
        p += 2;
    }
}

int phi(int n){
    if(totient[n] != 0)
        return totient[n];
    for(int p: primes){
        if(p*p > n)
            break;
        if(n % p != 0)
            continue;
        int k = 1;
        int reduced = n/p;
        totient[n] = p-1;
        while(reduced % p == 0)
            ++k, reduced /= p, totient[n] *= p;
        if(reduced != 1)
            totient[n] *= phi(reduced);
        return totient[n];
    }
    totient[n] = n-1;
    return totient[n];
}

int fingerprint(int n){
    int ans = 0;
    while(n != 0){
        int shift = 1;
        for(int i = 0; i < n % 10; ++i){
            shift *= 10;
        }
        ans += shift;
        n /= 10;
    }
    return ans;
}

int main() {
    int N;
    cin >> N;
    sieve(N);
    pair<int, double> best = {2, 10e7};
    for(int n=3; n < N; ++n){
        int phi_n = phi(n);
        double quotient = (double) n/phi_n;
        if(get<1>(best) <= quotient)
            continue;
        if(fingerprint(n) == fingerprint(phi_n))
            best = {n, quotient};
    }
    cout << get<0>(best) << endl;
    return 0;
}
