import itertools
import random

class User:
    def __init__(self, name):
        self.name = name

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.friendships[vertex_id]

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

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        for i in range(num_users):
            self.add_user(f"User {self.last_id + 1}")
        possible_friendships = list(itertools.combinations(range(1, num_users + 1), 2))
  
        total_friendships = num_users * avg_friendships // 2

        random.shuffle(possible_friendships)
        for j in range(total_friendships):
            self.add_friendship(possible_friendships[j][0], possible_friendships[j][1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for user in self.friendships:
            path = self.bfs(user_id, user)
            if path is not None:
                visited[user] = path
        return visited

# print(random.randrange(0, 5))
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
