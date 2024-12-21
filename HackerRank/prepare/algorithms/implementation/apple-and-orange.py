# https://www.hackerrank.com/challenges/apple-and-orange/
house_a, house_b = map(int, input().split())
apple_tree, orange_tree = map(int, input().split())
input()
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

total_apples = 0
for a in apples:
    if apple_tree + a >= house_a and apple_tree + a <= house_b:
        total_apples += 1

total_oranges = 0
for a in oranges:
    if orange_tree + a >= house_a and orange_tree + a <= house_b:
        total_oranges += 1
    
print(total_apples)
print(total_oranges)
