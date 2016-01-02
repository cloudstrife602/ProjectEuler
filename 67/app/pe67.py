import os
from path import Path

p = Path()
p.init([])
p.importFromFile(os.path.abspath('./app/p067_triangle.txt'))
# print(p.max())
print(p.quickMax())
