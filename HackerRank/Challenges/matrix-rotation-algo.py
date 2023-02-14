def matrix_to_rings(M, R, C):
    rings = []
    for n_ring in range(min(R//2, C//2)):
        corners = [
            n_ring         + (n_ring) * 1j,
            C - 1 - n_ring + (n_ring) * 1j,
            C - 1 - n_ring + (R - 1 - n_ring) * 1j,
            n_ring         + (R - 1 - n_ring) * 1j
        ]
        last = None
        curr = n_ring + n_ring * 1j
        dir = -1j
        curr_ring = []
        while last != corners[0]:
            curr_ring.append(M[int(curr.imag)][int(curr.real)])
            if curr in corners:
                dir *= 1j
            curr += dir
            last = curr
        rings.append(curr_ring)
    return rings

def rings_to_matrix(rings, R, C):
    M = [[0]*C for _ in range(R)]
    for n_ring, r in enumerate(rings):
        corners = [
            n_ring         + (n_ring) * 1j,
            C - 1 - n_ring + (n_ring) * 1j,
            C - 1 - n_ring + (R - 1 - n_ring) * 1j,
            n_ring         + (R - 1 - n_ring) * 1j
        ]
        last = None
        curr = n_ring + n_ring * 1j
        dir = -1j
        i = 0
        while last != corners[0]:
            M[int(curr.imag)][int(curr.real)] = r[i]
            if curr in corners:
                dir *= 1j
            curr += dir
            i += 1
            last = curr
    return M

def rotate(rings, N):
    ans = []
    for r in rings:
        ans.append(r[N%len(r):] + r[:N%len(r)])
    return ans

R, C, N = map(int, input().split())
M = []

for _ in range(R):
    M.append(list(map(int, input().split())))

M2 = rings_to_matrix(rotate(matrix_to_rings(M, R, C), N), R, C)
for r in M2:
    print(*r)
