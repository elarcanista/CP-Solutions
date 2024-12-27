# https://www.hackerrank.com/challenges/count-strings/
def parse(text):
    stack = [[]]
    for c in text:
        if c == "(":
            head = []
            stack[-1].append(head)
            stack.append(head)
        elif c == ")":
            if len(stack[-1]) == 3 or stack[-1][-1] == "*":
                stack[-1][0], stack[-1][1] = stack[-1][1], stack[-1][0]
            else:
                stack[-1].insert(0, "c")
            stack.pop()
        else:
            stack[-1].append(c)
    return stack.pop()

def shift_vertices(nfa, shift):
    new_nfa = {}
    for source, edges in nfa.items():
        new_nfa[source + shift] = []
        for char, target in edges:
            new_nfa[source + shift].append((char, target + shift))
    return new_nfa

def join_nfa(nfa1, nfa2):
    for key, value in nfa2.items():
        if key in nfa1:
            nfa1[key] += value
        else:
            nfa1[key] = value
    return nfa1

def nfa_concat(fst, snd):
    snd = shift_vertices(snd, max(fst.keys()))
    return join_nfa(fst, snd)

def nfa_or(left, right):
    left = shift_vertices(left, 1)
    left_end = max(left.keys())
    right = shift_vertices(right, left_end + 1)
    right_end = max(right.keys())
    ans = {0: [("e", 1), ("e", left_end + 1)], right_end + 1: []}
    left[left_end].append(("e", right_end + 1))
    right[right_end].append(("e", right_end + 1))
    ans = join_nfa(ans, left)
    ans = join_nfa(ans, right)
    return ans

def nfa_star(nfa):
    nfa = shift_vertices(nfa, 1)
    last = max(nfa.keys()) + 1
    nfa[0] = [("e", 1), ("e", last)]
    nfa[last - 1].append(("e", 1))
    nfa[last - 1].append(("e", last))
    nfa[last] = []
    return nfa

def to_nfa(ast):
    automata = {}
    if len(ast) == 1 and type(ast[0]) == list:
        ast = ast[0]
    if ast[0] == "c":
        automata = nfa_concat(to_nfa(ast[1]), to_nfa(ast[2]))
    elif ast[0] == "|":
        automata = nfa_or(to_nfa(ast[1]), to_nfa(ast[2]))
    elif ast[0] == "*":
        automata = nfa_star(to_nfa(ast[1]))
    else:
        automata = {0: [(ast[0], 1)], 1: []}
    return automata

def to_dict(nfa):
    ans = {}
    for (source, edges) in nfa.items():
        if source not in ans:
            ans[source] = {}
        for (char, target) in edges:
            if char not in ans[source]:
                ans[source][char] = []
            ans[source][char].append(target)
    return ans

def lsb(x):
    return x&-x

def to_powers(x):
    ans = []
    while x > 0:
        curr = lsb(x)
        x -= curr
        count = 0
        while curr != 1:
            curr >>= 1
            x >>= 1
            count += 1
        if len(ans) > 0:
            count += ans[-1]
        ans.append(count)
    return ans

def kleene_closure_single(state, nfa, memo_nfa):
    if state in memo_nfa:
        return memo_nfa[state]
    ans = 0
    stack = [state]
    while len(stack) > 0:
        source = stack.pop()
        if ((1 << source) | ans) == ans:
            continue
        ans |= 1 << source
        if "e" not in nfa[source]:
            continue
        for target in nfa[source]["e"]:
            stack.append(target)
    memo_nfa[state] = ans
    return ans

def kleene_closure_set(state, nfa, memo_nfa, memo_dfa):
    if state in memo_dfa:
        return memo_dfa[state]
    ans = 0
    for p in to_powers(state):
        ans |= kleene_closure_single(p, nfa, memo_nfa)
    memo_dfa[state] = ans
    return ans

def to_dfa(nfa):
    memo_kleene_nfa = {}
    memo_kleene_dfa = {}
    initial_state = kleene_closure_single(0, nfa, memo_kleene_nfa)
    terminal_states = []
    dfa = {}
    stack = [initial_state]
    while len(stack) > 0:
        source = stack.pop()
        if source in dfa:
            continue
        powers = to_powers(source)
        if len(powers) > 0 and powers[-1] == max(nfa.keys()):
            terminal_states.append(source)
        dfa[source] = {}
        for char in "ab":
            target = 0
            for s in powers:
                if char not in nfa[s]:
                    continue
                for t in nfa[s][char]:
                    target |= 1 << t
            target = kleene_closure_set(target, nfa, memo_kleene_nfa, memo_kleene_dfa)
            dfa[source][char] = target
            stack.append(target)
    return dfa, initial_state, terminal_states

def to_matrix(dfa, initial_state, terminal_states):
    vertices = list(dfa.keys())
    translation = {}
    for i, v in enumerate(vertices):
        translation[v] = i
    matrix = []
    new_initial_state = translation[initial_state]
    new_terminal_states = [translation[v] for v in terminal_states]
    for source in range(len(translation)):
        matrix.append([0] * len(vertices))
        for char, target in dfa[vertices[source]].items():
            matrix[-1][translation[target]] += 1
    return matrix, new_initial_state, new_terminal_states

def matrix_mult(left, right, modulo):
    ans = []
    for r in range(len(left)):
        ans.append([])
        for c in range(len(right[r])):
            ans[-1].append(0)
            for k in range(len(right)):
                ans[-1][-1] += (left[r][k] * right[k][c]) % modulo
                ans[-1][-1] %= modulo
    return ans

def matrix_pow(matrix, power, modulo):
    if power == 1:
        return matrix
    ans = matrix_pow(matrix, power // 2, modulo)
    ans = matrix_mult(ans, ans, modulo)
    if power % 2 == 1:
        ans = matrix_mult(ans, matrix, modulo)
    return ans

def count_strings(matrix, initial_state, terminal_states, modulo):
    ans = 0
    for s in terminal_states:
        ans += matrix[initial_state][s]
        ans %= modulo
    return ans

modulo = 10**9 + 7
for _ in range(int(input())):
    text, length = input().split()
    length = int(length)
    ast = parse(text)
    nfa = to_nfa(ast)
    nfa = to_dict(nfa)
    dfa, initial_state, terminal_states = to_dfa(nfa)
    matrix, initial_state, terminal_states = to_matrix(dfa, initial_state, terminal_states)
    matrix_n_steps = matrix_pow(matrix, length, modulo)
    strings_length_n = count_strings(matrix_n_steps, initial_state, terminal_states, modulo)
    print(strings_length_n)
