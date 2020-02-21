from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# # Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited_master = []

last_room = world.starting_room

visited_rooms = set()

def dft(graph, start):
    stack = Stack()

    stack.push([start])
    print(stack.stack)

    visited = set()

    traveled = Stack()

    traveled.push([])
    longest = 500

    while stack.size() > 0:
        current_path = stack.pop()
        current_node = current_path[-1]
        neighbors = set()
        directions = set()

        traveled_path = traveled.pop()
        
        global visited_master
        print('current', current_node.id)
        if not current_node.id in visited:
            visited.add(current_node.id)
            avail_moves = current_node.get_exits()
            for move in avail_moves:
                if move is not None and current_node is not None:
                  
                    neighbors.add(current_node.get_room_in_direction(move))
                    directions.add(move)
                
            for room in neighbors:
                path_dup = list(current_path)
                path_dup.append(room)
                stack.push(path_dup)
                #print(stack.stack)
             
            for move in directions:
                travel_dup = list(traveled_path)
                travel_dup.append(move)
                traveled.push(travel_dup)
                # print(traveled.stack)
                if len(travel_dup) < longest:
                    index = traveled.stack.index(travel_dup)
                    print(index)
                    # print(stack.stack[index])
                    if stack.stack[index] not in visited_master:
                        longest = len(travel_dup)
                        longest_list = travel_dup
                        rooms_list = stack.stack[index]
    global visited_rooms
    for i in rooms_list:
        visited_rooms.add(i)
    visited_master.append(visited_rooms)
    print(visited_master, visited_rooms)
    global last_room
    last_room = longest_list[1:]
    return (rooms_list[-1], longest_list[1:])

# def find_next(graph, starting_room):
#     global visited_rooms
#     all_rooms = []
#     for i in range(500):
#         if i not in visited_rooms:
#             return dft(graph, starting_room)
#         else:
#             return traversal_path

def get_path():
    while len(visited_rooms) < 300:
        dft(world, last_room)

    

print(get_path())
print(visited_rooms)


# find_next()


print('here', dft(world, world.starting_room))

# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
