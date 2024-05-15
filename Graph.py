class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[float('inf') for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def floyd_warshall(self):
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

    def print_matrix(self):
        for row in self.graph:
            print(' '.join(str(round(val, 2)) for val in row))

    def get_shortest_path(self, u, v):
        path = []
        temp = self.graph[u][v]
        while temp != float('inf'):
            path.append(v)
            for k in range(self.V):
                if self.graph[u][k] + self.graph[k][v] == temp:
                    v = k
                    break
            temp = self.graph[u][v]
        path.append(u)
        return list(reversed(path))

    def get_center(self):
        min_distance = float('inf')
        center = None
        for i in range(self.V):
            max_distance = max(self.graph[i])
            if max_distance < min_distance:
                min_distance = max_distance
                center = i
        return center