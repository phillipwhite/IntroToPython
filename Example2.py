s1 = set()
s2 = {1, 3, 5}

print(s2)

s4 = set( [2, 4, 4])
l1 = [1, 1, 2, 2, 3, 3, 4, 5, 6]
s1 = set(l1)
print(s1)
l2 = list(s1)
print(l2)
t1 = tuple(s1)
print(t1)
print(len(s1))
print(len(l1) - len(set(l1)))

def dupeCount(l):
    len(l) - len(set(l))

s1.add(33453)
s1.remove(6)
print(s1)
print({1,2,3}.issubset({1,2,3,4}))
print({1,2,3, 7}.issubset({1,2,3,4}))
print({1,2,3, 7}.issuperset({1,2,3}))
print({1,2,3, 7}.issuperset({1,2,3, 8}))

print({1,2,3} | { 2,3,4})
print({1,2,3} & { 2,3,4})
print({1,2,3} - { 2,3,4})
print({1,2,3}.symmetric_difference({ 2,3,4}))