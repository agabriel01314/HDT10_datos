import unittest
import Graph

class TestGraphMethods(unittest.TestCase):
    def setUp(self):
        self.graph_obj = Graph.Graph(5)
        self.graph_obj.add_edge(0, 1, 10)
        self.graph_obj.add_edge(1, 2, 20)
        self.graph_obj.add_edge(2, 3, 30)
        self.graph_obj.add_edge(3, 4, 40)

    def test_floyd_warshall(self):
        self.graph_obj.floyd_warshall()
        self.assertEqual(self.graph_obj.graph[0][4], 100)

    def test_get_shortest_path(self):
        self.graph_obj.floyd_warshall()
        path = self.graph_obj.get_shortest_path(0, 4)
        self.assertEqual(path, [0, 1, 2, 3, 4])

    def test_get_center(self):
        self.graph_obj.floyd_warshall()
        center = self.graph_obj.get_center()
        self.assertEqual(center, 2)

if __name__ == "__main__":
    unittest.main()