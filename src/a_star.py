import numpy as np
import random
import heapq
import time
from .maze import get_neighbors
from .utils import manhattan_distance

random.seed(42)
np.random.seed(42)


# A* search algorithm that returns the path, final maze, search steps, and statistics
def search(maze, start, goal):
    start_time = time.time()
    maze_final = maze.copy()

    heap = [(0, 0, start, [start])]

    visited = set()
    g_costs = {start: 0}
    search_steps = []

    nodes_visited = 0

    while heap:
        f_cost, g_cost, current, path = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)
        nodes_visited += 1

        if current != start and current != goal:
            maze_final[current] = 4

        search_steps.append({
            'maze': maze_final.copy(),
            'current': current,
            'path': path.copy()
        })
        if current == goal:
            final_maze = maze_final.copy()
            for pos in path:
                if pos != start and pos != goal:
                    final_maze[pos] = 5
            end_time = time.time()

            stats = {
                'nodes_visited': nodes_visited,
                'path_length': len(path),
                'execution_time': end_time - start_time
            }

            return path, final_maze, search_steps, stats

        for neighbor in get_neighbors(current, maze):
            if neighbor in visited:
                continue

            tentative_g_cost = g_cost + 1

            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(heap, (f_cost, tentative_g_cost,
                               neighbor, path + [neighbor]))

    end_time = time.time()
    stats = {
        'nodes_visited': nodes_visited,
        'path_length': 0,
        'execution_time': end_time - start_time
    }
    return None, maze_final, search_steps, stats
