from room import Room
from player import Player
from world import World
from collections import deque
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# print(f"line 48: {player.current_room.id}")
# print(f"line 49: {player.current_room.get_exits()}")
# print(f"line 50: {player.travel(traversal_path[0])}")

def bfs(self, starting_vertex):
        visited = set()
        queue = deque()
        queue.append([starting_vertex])

        while len(queue) > 0:
            current_path = queue.popleft()
            current_node = current_path[-1]

            if current_node == "?":
                return current_path
            
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in player.current_room.get_exits():
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    queue.append(new_path)


graph = {}
stack = deque()
stack.append(player.current_room.id)

while len(stack) > 0:
    current_loc = stack.pop()
    if current_loc not in graph:
        graph[current_loc] = {}
        for path in player.current_room.get_exits():
            graph[current_loc][path] = "?"

    for k, v in graph[current_loc].items():
        if v == "?":
            player.travel(k)
            traversal_path.append(k)
            graph[current_loc][k] = player.current_room.id
            if player.current_room.id not in graph:
                stack.append(player.current_room.id)
                break
            else:
                continue


print(traversal_path)
print(graph)


# TRAVERSAL TEST - DO NOT MODIFY
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
