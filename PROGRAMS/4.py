from itertools import permutations

word1 = "SEND"
word2 = "MORE"
result = "MONEY"

letters = set(word1 + word2 + result)

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    if d[word1[0]] == 0 or d[word2[0]] == 0 or d[result[0]] == 0:
        continue

    n1 = int("".join(str(d[c]) for c in word1))
    n2 = int("".join(str(d[c]) for c in word2))
    n3 = int("".join(str(d[c]) for c in result))

    if n1 + n2 == n3:
        print(n1, "+", n2, "=", n3)
        break
