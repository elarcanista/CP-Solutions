def foo(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    head1 = head2 = 0
    while True:
        if max(head1, head2) >= min(len(s1), len(s2)):
            return False
        if s1[head1] == s2[head2]:
            return True
        if s1[head1] < s2[head2]:
            head1+=1
        elif s1[head1] > s2[head2]:
            head2+=1
        
n = int(input())
for i in range(n):
    s1 = input()
    s2 = input()
    if foo(s1, s2):
        print("YES")
    else:
        print("NO")
