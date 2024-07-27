d= {}
print(type(set({})))
print(type(dict({})))
print(type({}))
d = {'a':9, "b": 2}
print(d['a'])

k = d.keys()
v = d.values()
print(k)
print(v)
print([0,1,2, [3,4,5]])
# print(set({0,1,2, "abvcs"  }))
# print(set({0,1,2, [3,4,5] }))

i= d.items()
print(i)

for i in d:
    print(i)