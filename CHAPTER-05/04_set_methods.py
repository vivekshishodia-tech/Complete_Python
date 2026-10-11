A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

A.add(7)
print(A)

A.remove(7)
print(A)