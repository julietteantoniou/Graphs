"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print('vertex already exists')
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        queue = Queue()
        # Add the starting vetex_id to the queue
        queue.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        #while the queue is not empty-
        while queue.size() > 0:
            #Dequeue the first vertex
            first_vert = queue.dequeue()
            # Check if it's been visited
            # If it has NOT been visted-
            if not first_vert in visited:
                # Mark it as visited
                print(first_vert)
                visited.add(first_vert)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(first_vert):
                    queue.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        stack = Stack()
        # Push the starting vetex_id to the top of the stack
        stack.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        #while the stack is not empty-
        while stack.size() > 0:
            #Pop the first vertex
            first_vert = stack.pop()
            # Check if it's been visited
            # If it has NOT been visted-
            if not first_vert in visited:
                # Mark it as visited
                print(first_vert)
                visited.add(first_vert)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(first_vert):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)

        visited.add(starting_vertex)
        edges = self.get_neighbors(starting_vertex)
    
        if len(edges) == 0:
            return

        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            current_path = queue.dequeue()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                # print(current_path)
                return current_path
            elif not current_node in visited:
                visited.add(current_node)
                for v in self.get_neighbors(current_node):
                    path_dup = list(current_path)
                    path_dup.append(v)
                    queue.enqueue(path_dup)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited=set()
        while stack.size() > 0:
            current_path = stack.pop()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path
            elif not current_node in visited:
                visited.add(current_node)
                for node in self.get_neighbors(current_node):
                    path_dup = list(current_path)
                    path_dup.append(node)
                    stack.push(path_dup)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print(starting_vertex)
        edges = self.get_neighbors(starting_vertex)
        path = list([starting_vertex])
        print(visited)
        if starting_vertex == destination_vertex:
            return
        if not starting_vertex in visited:
            visited.add(starting_vertex)
            for vertex in edges:
                self.dfs_recursive(vertex, destination_vertex, visited)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    #graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    #print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
