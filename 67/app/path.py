class Path(object):

    triangle = []
    path_length = 0

    def init(self, triangle):
        self.triangle = triangle
        self.path_length = len(triangle)

    def importFromFile(self, filename):
        triangle = []
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip('\n')
                row = []
                for num in line.split(' '):
                    row.append(int(num))
                triangle.append(row)
            self.triangle = triangle

    def requiredBits(self):
        triangle = self.triangle
        return len(triangle)

    def nodeMax(self, i, j):
        triangle = self.triangle
        if (i >= 0) and (i <= len(triangle) - 1):
            if (j >= 0) and (j <= len(triangle[i]) - 1):
                if (i == len(triangle) - 1):
                    return triangle[i][j]
                else:
                    l = self.nodeMax(i+1, j)
                    r = self.nodeMax(i+1, j+1)
                    if l >= r:
                        max_child = l
                    else:
                        max_child = r
                    return triangle[i][j] + max_child
            else:
                raise IndexError
        else:
            raise IndexError

    def max(self):
        return self.nodeMax(0, 0)

    def quickMax(self):
        triangle = self.triangle
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
