import numpy as np
from maze import *
import a_star
import bfs
import dfs


if __name__ == "__main__":
    algorithm = input(
        "Enter the search algorithm (A* / DFS / BFS): ").strip().upper()
    if algorithm not in ['A*', 'DFS', 'BFS']:
        print("Invalid algorithm choice. Please choose A*, DFS, or BFS.")
        exit(1)
    rows = int(input("Enter the number of rows (odd number): "))
    cols = int(input("Enter the number of columns (odd number): "))
    if rows % 2 == 0 or cols % 2 == 0:
        print("Rows and columns must be odd numbers.")
        exit(1)
    maze = generate_maze(rows, cols)
    maze_with_sg, start_pos, goal_pos = place_start_goal(maze)
    print("Generated Maze with Start and Goal:")

    if algorithm == 'A*':
        path, final_maze, search_steps, stats = a_star.search(
            maze_with_sg, start_pos, goal_pos)
    elif algorithm == 'DFS':
        path, final_maze, search_steps, stats = dfs.search(
            maze_with_sg, start_pos, goal_pos)
    elif algorithm == 'BFS':
        path, final_maze, search_steps, stats = bfs.search(
            maze_with_sg, start_pos, goal_pos)

    run_pygame_visualization(search_steps, maze_with_sg.shape)
    print("Search completed.")
    print(f"Nodes visited: {stats['nodes_visited']}")
    print(f"Path length: {stats['path_length']}")
    print(f"Execution time: {stats['execution_time']:.4f} seconds")
