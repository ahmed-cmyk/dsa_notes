# Graphs

A graph is a non-linear data structure consisting of a finite set of vertices (or nodes) and a set of edges that connect pairs of vertices. Graphs are used to model many real-world systems, such as social networks, road networks, and the World Wide Web.

## Key Characteristics:
- **Vertices (Nodes):** The fundamental entities in a graph.
- **Edges:** Connections between vertices.
- **Directed vs. Undirected:**
    - **Undirected Graph:** Edges have no direction (e.g., A-B means B-A).
    - **Directed Graph (Digraph):** Edges have a direction (e.g., A->B means you can go from A to B, but not necessarily B to A).
- **Weighted vs. Unweighted:**
    - **Weighted Graph:** Edges have associated numerical values (weights/costs).
    - **Unweighted Graph:** Edges have no associated values.
- **Cyclic vs. Acyclic:**
    - **Cyclic Graph:** Contains at least one cycle (a path that starts and ends at the same vertex).
    - **Acyclic Graph:** Contains no cycles.
- **Connected vs. Disconnected:**
    - **Connected Graph:** There is a path between every pair of vertices.
    - **Disconnected Graph:** Not all vertices are reachable from each other.

## Common Representations:
- **Adjacency Matrix:** A 2D array where `matrix[i][j]` is 1 (or weight) if there's an edge from `i` to `j`, and 0 otherwise.
- **Adjacency List:** An array or hash map where each index/key represents a vertex, and its value is a list of its adjacent vertices.

## Implementations (Adjacency List Example):

### Python
```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, is_directed=False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        if not is_directed:
            self.graph[v].append(u)

    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")

# Example Usage:
# g = Graph()
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'E')
# g.display()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'E']
# D: ['B']
# E: ['C']
```

### PHP
```php
<?php

class Graph {
    private $graph = [];

    public function addVertex($vertex) {
        if (!isset($this->graph[$vertex])) {
            $this->graph[$vertex] = [];
        }
    }

    public function addEdge($u, $v, $isDirected = false) {
        $this->addVertex($u);
        $this->addVertex($v);
        $this->graph[$u][] = $v;
        if (!$isDirected) {
            $this->graph[$v][] = $u;
        }
    }

    public function display() {
        foreach ($this->graph as $vertex => $neighbors) {
            echo "{$vertex}: " . implode(", ", $neighbors) . "\n";
        }
    }
}

// Example Usage:
// $g = new Graph();
// $g->addEdge('A', 'B');
// $g->addEdge('A', 'C');
// $g->addEdge('B', 'D');
// $g->addEdge('C', 'E');
// $g->display();
/* Output:
A: B, C
B: A, D
C: A, E
D: B
E: C
*/

?>
```

### JavaScript
```javascript
class Graph {
    constructor() {
        this.graph = {};
    }

    addVertex(vertex) {
        if (!this.graph[vertex]) {
            this.graph[vertex] = [];
        }
    }

    addEdge(u, v, isDirected = false) {
        this.addVertex(u);
        this.addVertex(v);
        this.graph[u].push(v);
        if (!isDirected) {
            this.graph[v].push(u);
        }
    }

    display() {
        for (const vertex in this.graph) {
            console.log(`${vertex}: ${this.graph[vertex].join(", ")}`);
        }
    }
}

// Example Usage:
// const g = new Graph();
// g.addEdge('A', 'B');
// g.addEdge('A', 'C');
// g.addEdge('B', 'D');
// g.addEdge('C', 'E');
// g.display();
/* Output:
A: B, C
B: A, D
C: A, E
D: B
E: C
*/
```

## Tips for LeetCode Amateurs:
- **Traversal Algorithms:** Master Breadth-First Search (BFS) and Depth-First Search (DFS). These are fundamental for almost all graph problems.
- **Shortest Path Algorithms:** Learn Dijkstra's algorithm (for non-negative weights) and Bellman-Ford (for negative weights). For unweighted graphs, BFS finds the shortest path.
- **Minimum Spanning Tree (MST):** Understand Prim's and Kruskal's algorithms for finding an MST in a weighted, undirected graph.
- **Topological Sort:** Essential for directed acyclic graphs (DAGs) to find a linear ordering of vertices.
- **Disjoint Set Union (DSU):** Useful for problems involving connected components and cycles.
- **Practice:** Graph problems can be challenging. Start with basic traversals and gradually move to more complex algorithms.
