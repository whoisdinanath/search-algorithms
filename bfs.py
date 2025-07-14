import time
from collections import deque
from maze import get_neighbors


# BFS search algorithm that returns the path, final maze, search steps, and statistics
def search(maze, start, goal):
    start_time = time.time()
    maze_final = maze.copy()
    queue = deque([(start, [start])])
    visited = set()
    search_steps = []
    nodes_visited = 0

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_visited += 1

        if current != start and current != goal:
            maze_final[current] = 4  # visited

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
            return path, final_maze, search_steps, {
                'nodes_visited': nodes_visited,
                'path_length': len(path),
                'execution_time': time.time() - start_time
            }

        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, maze_final, search_steps, {
        'nodes_visited': nodes_visited,
        'path_length': 0,
        'execution_time': time.time() - start_time
    }
