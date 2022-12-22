D, H, R = map(int, input().split())
T = D + H + R

HH = (H/T) * (H-1)/(T-1) * (1/4)
HR = (H/T) * R/(T-1) * (1/2)
RH = (R/T) * H/(T-1) * (1/2)
RR = (R/T) * (R-1)/(T-1)
print(round(1 - (HH + HR + RH + RR), 5))