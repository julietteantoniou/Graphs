from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from graph import Graph

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

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def traverse_rooms():

    graph = Graph()

    for room in world.rooms:
        graph.add_vertex(room)
    # print("**************************", graph.vertices[400]['n'])

    for room in world.rooms:
        room_id= world.rooms[room].id
        # exits = world.rooms[room].get_exits()
        n_room = world.rooms[room].get_room_in_direction('n')
        if n_room is not None:
            n = n_room.id
            graph.vertices[room_id]['n'] = n
        else:
            del graph.vertices[room_id]['n']
        e_room = world.rooms[room].get_room_in_direction('e')
        if e_room is not None:
            e = e_room.id
            graph.vertices[room_id]['e'] = e
        else:
            del graph.vertices[room_id]['e']
        s_room = world.rooms[room].get_room_in_direction('s')
        if s_room is not None:
            s = s_room.id
            graph.vertices[room_id]['s'] = s
        else:
            del graph.vertices[room_id]['s']
        w_room = world.rooms[room].get_room_in_direction('w')
        if w_room is not None:
            w = w_room.id
            graph.vertices[room_id]['w'] = w
        else:
            del graph.vertices[room_id]['w']
        # graph.vertices[room_id]['n'] = n
        # graph.vertices[room_id]['e'] = e
        # graph.vertices[room_id]['w'] = w
        # graph.vertices[room_id]['s'] = s
    print(graph.vertices)
    # print(room_graph)
    global traversal_path
    current_id = world.starting_room.id
    while len(graph.visited) < len(room_graph):
        last_walk = graph.dft_shortest(current_id)
        current_id =last_walk[0]
        for i in last_walk[2]:
            traversal_path.append(i)
    print(traversal_path)



    # current_room = player.current_room
    # for room in graph.vertices[current_room].id:
    #     room_id= world.rooms[room].id
    #     # exits = world.rooms[room].get_exits()
    # if graph.vertices
    #     n_room = world.rooms[room].get_room_in_direction('n')
    #     if n_room is not None:
    #         n = n_room.id
    #         graph.vertices[room_id]['n'] = n
    #         player.travel('n')
    #     else:
    #         del graph.vertices[room_id]['n']
    #     e_room = world.rooms[room].get_room_in_direction('e')
    #     if e_room is not None:
    #         e = e_room.id
    #         graph.vertices[room_id]['e'] = e
    #     else:
    #         del graph.vertices[room_id]['e']
    #     s_room = world.rooms[room].get_room_in_direction('s')
    #     if s_room is not None:
    #         s = s_room.id
    #         graph.vertices[room_id]['s'] = s
    #     else:
    #         del graph.vertices[room_id]['s']
    #     w_room = world.rooms[room].get_room_in_direction('w')
    #     if w_room is not None:
    #         w = w_room.id
    #         graph.vertices[room_id]['w'] = w
    #     else:
    #         del graph.vertices[room_id]['w']

    # player

        


traverse_rooms()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# print('rooms', world.rooms)
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