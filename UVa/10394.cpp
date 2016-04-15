//Author: Andrés Felipe Ortega Montoya
//UVa 10394 - Twin Primes
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll MAXN = 20000000;
bool primes[MAXN]; //stores if a number is prime or not
vector<pair<ll, ll>> twins; //stores twin primes

void sieve(){ //sieve of eratosthenes
	for(ll i = 3LL; i < MAXN; ++i){ //set all pairs false and odds true
		if (i % 2LL) primes[i] = true;
		else primes[i] = false;
	} 
	primes[0LL] = primes[1LL] = false; //sets 0 and 1 as not primes and 2 as a prime
	primes[2LL] = true;
	//mark not prime numbers and checks if there are pair primes
	for(ll i = 3LL; i < MAXN; i+=2LL){
		if(primes[i]){
			if(primes[i-2LL]) twins.push_back({i-2LL, i}); 
			if(i*i < MAXN){
				ll temp = i*2LL;
				while(temp < MAXN){
					primes[temp] = false;
					temp += i;
				}
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll in;
	sieve(); //generate all prime numbers
	while(cin >> in){
		cout << "(" << twins[in-1LL].first << ", " << twins[in-1LL].second << ")\n";
		cout.flush();
	}
	return 0;
}
