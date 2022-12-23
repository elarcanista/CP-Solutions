N, m = map(int, input().split())

adults = [0, 0] + [0] * (N-1)
babies = [0, 1] + [0] * (N-1)
for n in range(2, N+1):
    babies[n] = adults[n-1]
    adults[n] = adults[n-1] + babies[n-1] - babies[n-m]

print(babies[-1] + adults[-1])