import numpy as np
a, b, d = list(map(int, input().split()))
d = np.radians(d)
kaiten = np.array([[np.cos(d), -np.sin(d)],
                   [np.sin(d), np.cos(d)]])

vec = np.array([a, b])

ans = np.dot(kaiten, vec)

print(*ans)
