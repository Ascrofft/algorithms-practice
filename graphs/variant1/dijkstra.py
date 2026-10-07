import heapq
from math import inf

adjacency_list = {
    # From city 'a', there are flights to cities 'b', 'd' and 'm'. These
    # flights cost 3, 11 and 11 respectively:
    'a': {'b': 3, 'd': 11, 'm': 11},
    # Similarly for the rest of the cities:
    'b': {'a': 3, 'c': 19, 'e': 3, 'h': 1},
    'c': {'g': 7, 'j': 5, 'q': 3},
    'd': {'h': 7, 'i': 5},
    'e': {'b': 3, 'm': 1, 'r': 11},
    'f': {'k': 3, 'q': 3},
    'g': {'c': 7, 'l': 3},
    'h': {'b': 1, 'p': 3, 'd': 7},
    'i': {'p': 3, 'd': 5, 'o': 3},
    'j': {'c': 5, 'o': 1},
    'k': {'f': 3, 'l': 1},
    'l': {'g': 3, 'k': 1, 'r': 11, 's': 3},
    'm': {'a': 11, 'e': 1, 'n': 1},
    'n': {'m': 1, 'o': 3},
    'o': {'i': 3, 'j': 1, 'n': 3},
    'p': {'c': 11, 'h': 3, 'i': 3},
    'q': {'c': 3, 'f': 3, 's': 11},
    'r': {'e': 11, 'l': 11},
    's': {'l': 3, 'q': 11}
}


def solve(adjacency_list: dict, origin: str, destination: str):
    distances = {}

    for vertex in adjacency_list:
        distances[vertex] = inf

    distances[origin] = 0

    previous = {}

    queue = []
    heapq.heappush(queue, (0, origin))

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == destination:
            break

        for neighbor, edge_cost in adjacency_list[current_vertex].items():
            new_distance = current_distance + edge_cost

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex
                heapq.heappush(queue, (new_distance, neighbor))

    if distances[destination] == inf:
        return None
    
    path = []
    current = destination

    while current != origin:
        path.append(current)
        current = previous[current]
    
    path.append(origin)
    path.reverse()
    
    return path


if __name__ == '__main__':
    print(solve(adjacency_list, 'a', 's') or "No path found...")
