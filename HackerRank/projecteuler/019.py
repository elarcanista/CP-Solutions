# https://www.hackerrank.com/contests/projecteuler/challenges/euler019/
import datetime as dt

def next_month(date):
    return (date.replace(day=1) + dt.timedelta(days=32)).replace(day=1)

def date_cycle(y, m, d):
    cycles = (y - 1900) // (400 * 7)
    y = (y - 1900) % (400 * 7) + 1900
    return dt.date(y, m ,d), cycles

def count_hits(date_start, date_end):
    if date_start.day == 1:
        date_curr = date_start
    else:
        date_curr = next_month(date_start)
    ans = 0
    while date_curr <= date_end:
        if date_curr.weekday() == 6:
            ans += 1
        date_curr = next_month(date_curr)
    return ans

cycle_hits = count_hits(dt.date(1900, 1, 1), dt.date(1900 + 400 * 7 - 1, 12, 31))

for _ in range(int(input())):
    date_start, cycle_start = date_cycle(*map(int, input().split()))
    date_end, cycle_end = date_cycle(*map(int, input().split()))

    hits = 0
    cycles = (cycle_end - cycle_start)
    if cycles != 0:
        cycles -= 1
        hits += count_hits(date_start, dt.date(1900 + 400 * 7 - 1, 12, 31))
        hits += count_hits(dt.date(1900, 1, 1), date_end)
    else:
        hits += count_hits(date_start, date_end)
    hits += cycles * cycle_hits
    print(hits)
